"""Tests for fincap/verification.py."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from fincap.guards import GuardResult
from fincap.verification import (
    VerificationReport,
    generate_verification_report,
    run_post_verification,
)


class TestVerificationReport:
    """Tests for VerificationReport."""

    def test_all_passed_true_when_no_guards(self):
        report = VerificationReport()
        assert report.all_passed is True
        assert report.stop_required is False

    def test_all_passed_false_when_pre_run_fails(self):
        report = VerificationReport(
            pre_run_guards=[
                GuardResult(passed=False, guard_name="test", reason="failed"),
            ]
        )
        assert report.all_passed is False
        assert report.stop_required is True

    def test_all_passed_false_when_post_run_fails(self):
        report = VerificationReport(
            post_run_guards=[
                GuardResult(passed=False, guard_name="test", reason="failed"),
            ]
        )
        assert report.all_passed is False
        assert report.stop_required is True

    def test_stop_not_required_when_all_pass(self):
        report = VerificationReport(
            pre_run_guards=[
                GuardResult(passed=True, guard_name="test"),
            ],
            post_run_guards=[
                GuardResult(passed=True, guard_name="test2"),
            ],
        )
        assert report.stop_required is False

    def test_format_summary_shows_public_repo_changed(self):
        report = VerificationReport(
            public_repo_changed=True,
            public_repo_status=" M file.txt",
        )
        summary = report.format_summary()
        assert "Public Repo Changed" in summary
        assert "Yes" in summary

    def test_format_summary_shows_public_repo_clean(self):
        report = VerificationReport(public_repo_changed=False)
        summary = report.format_summary()
        assert "No" in summary


class TestRunPostVerification:
    """Tests for run_post_verification."""

    def test_returns_list_of_results(self, tmp_path):
        (tmp_path / ".git").mkdir()
        results = run_post_verification(tmp_path, tmp_path)
        assert isinstance(results, list)
        assert all(isinstance(r, GuardResult) for r in results)

    def test_agent_output_checked_for_drift(self, tmp_path):
        (tmp_path / ".git").mkdir()
        results = run_post_verification(
            tmp_path,
            tmp_path,
            agent_output="这是一个银行客服项目",
        )
        drift_result = next(
            (r for r in results if r.guard_name == "route_conflict_keyword_check"),
            None,
        )
        assert drift_result is not None
        assert drift_result.passed is False

    def test_agent_output_checked_for_compliance(self, tmp_path):
        (tmp_path / ".git").mkdir()
        results = run_post_verification(
            tmp_path,
            tmp_path,
            agent_output="我们可以保证完成授信审批",
        )
        compliance_result = next(
            (r for r in results if r.guard_name == "compliance_stop_check"),
            None,
        )
        assert compliance_result is not None
        assert compliance_result.passed is False

    def test_clean_agent_output_passes(self, tmp_path):
        (tmp_path / ".git").mkdir()
        results = run_post_verification(
            tmp_path,
            tmp_path,
            agent_output="Financial Capability Kit 帮助提升专业金融能力",
        )
        for r in results:
            if r.guard_name in ("route_conflict_keyword_check", "compliance_stop_check"):
                assert r.passed is True


class TestGenerateVerificationReport:
    """Tests for generate_verification_report."""

    def test_generates_complete_report(self, tmp_path):
        (tmp_path / ".git").mkdir()
        pre_guards = [
            GuardResult(passed=True, guard_name="public_repo_dirty_check"),
            GuardResult(passed=True, guard_name="queue_status_check"),
        ]
        report = generate_verification_report(tmp_path, tmp_path, pre_guards)
        assert isinstance(report, VerificationReport)
        assert len(report.pre_run_guards) == 2
        assert report.public_repo_changed is False

    def test_stops_when_pre_run_fails(self, tmp_path):
        (tmp_path / ".git").mkdir()
        pre_guards = [
            GuardResult(passed=False, guard_name="queue_status_check", reason="not ready"),
        ]
        report = generate_verification_report(tmp_path, tmp_path, pre_guards)
        assert report.stop_required is True
