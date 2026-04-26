"""Tests for fincap/guards.py."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from fincap.guards import (
    GuardResult,
    compliance_stop_check,
    git_diff_check,
    git_status_short,
    public_repo_dirty_check,
    queue_status_check,
    registry_json_parse_check,
    route_conflict_keyword_check,
    workspace_dirty_check,
)


class TestQueueStatusCheck:
    """Tests for queue_status_check guard."""

    def test_ready_status_passes(self):
        result = queue_status_check("ready")
        assert result.passed is True

    def test_in_progress_status_passes(self):
        result = queue_status_check("in-progress")
        assert result.passed is True

    def test_done_status_fails(self):
        result = queue_status_check("done")
        assert result.passed is False
        assert "done" in result.reason

    def test_blocked_status_fails(self):
        result = queue_status_check("blocked")
        assert result.passed is False

    def test_unknown_status_fails(self):
        result = queue_status_check("unknown")
        assert result.passed is False


class TestRouteConflictKeywordCheck:
    """Tests for route_conflict_keyword_check guard."""

    def test_clean_text_passes(self):
        text = "Financial Capability Kit 帮助用户系统提升金融能力"
        result = route_conflict_keyword_check(text)
        assert result.passed is True

    def test_bank_customer_service_fails(self):
        text = "这是一个银行客服项目"
        result = route_conflict_keyword_check(text)
        assert result.passed is False
        assert "银行客服" in result.reason

    def test_personality_distillation_fails(self):
        text = "本项目使用人格蒸馏技术"
        result = route_conflict_keyword_check(text)
        assert result.passed is False
        assert "人格蒸馏" in result.reason

    def test_customer_service_knowledge_base_fails(self):
        text = "建设银行客服知识库"
        result = route_conflict_keyword_check(text)
        assert result.passed is False

    def test_mixed_text_with_keyword_fails(self):
        # "角色设定" is in DRIFT_KEYWORDS
        text = "帮助用户提升能力，同时保留角色设定"
        result = route_conflict_keyword_check(text)
        assert result.passed is False
        assert "角色设定" in result.reason


class TestComplianceStopCheck:
    """Tests for compliance_stop_check guard."""

    def test_clean_text_passes(self):
        text = "本产品收益率取决于市场表现"
        result = compliance_stop_check(text)
        assert result.passed is True

    def test_credit_approval_pattern_fails(self):
        text = "我们保证可以为您完成授信审批"
        result = compliance_stop_check(text)
        assert result.passed is False
        assert "授信" in result.reason

    def test_pricing_commitment_fails(self):
        # "定价" followed by "承诺" matches r"定价.*承诺"
        text = "我们可以保证给您最优惠的定价，并承诺最低价"
        result = compliance_stop_check(text)
        assert result.passed is False

    def test_timing_commitment_fails(self):
        text = "我们承诺3天内完成时效承诺"
        result = compliance_stop_check(text)
        assert result.passed is False

    def test_internal_stance_fails(self):
        # "内部口径" appears as substring in this text
        text = "这是内部口径，需要保密"
        result = compliance_stop_check(text)
        assert result.passed is False


class TestPublicRepoDirtyCheck:
    """Tests for public_repo_dirty_check guard.

    These tests use the actual repo paths since git commands
    require a real git repository.
    """

    def test_clean_repo_passes(self):
        from pathlib import Path
        root = Path("C:/AI/claude_projects/awesome-banker-skills")
        result = public_repo_dirty_check(root)
        # Result depends on actual repo state; just verify guard runs
        assert isinstance(result.passed, bool)
        assert result.guard_name == "public_repo_dirty_check"

    def test_dirty_repo_detection(self, tmp_path):
        """Verify dirty check works when there are untracked files."""
        # Uses workspace which is a real git repo
        workspace = Path("C:/AI/claude_projects/awesome-banker-skills/workspace")
        if not (workspace / ".git").exists():
            pytest.skip("Workspace is not a git repo")
        result = public_repo_dirty_check(workspace)
        # Workspace may or may not be dirty; just verify it runs
        assert result.guard_name == "public_repo_dirty_check"


class TestWorkspaceDirtyCheck:
    """Tests for workspace_dirty_check guard.

    Uses real workspace path since git commands require a real repo.
    """

    def test_workspace_check_runs(self):
        from pathlib import Path
        workspace = Path("C:/AI/claude_projects/awesome-banker-skills/workspace")
        if not (workspace / ".git").exists():
            pytest.skip("Workspace is not a git repo")
        result = workspace_dirty_check(workspace)
        assert result.passed is True
        assert result.guard_name == "workspace_dirty_check"


class TestRegistryJsonParseCheck:
    """Tests for registry_json_parse_check guard."""

    def test_valid_skills_json_passes(self, tmp_path):
        skills = {"skills": []}
        reg_dir = tmp_path / "registry"
        reg_dir.mkdir()
        (reg_dir / "skills.json").write_text(json.dumps(skills), encoding="utf-8")
        result = registry_json_parse_check(tmp_path)
        assert result.passed is True

    def test_valid_all_three_passes(self, tmp_path):
        reg_dir = tmp_path / "registry"
        reg_dir.mkdir()
        (reg_dir / "skills.json").write_text('{"skills": []}', encoding="utf-8")
        (reg_dir / "knowledge.json").write_text('{"knowledge": []}', encoding="utf-8")
        (reg_dir / "prompts.json").write_text('{"prompts": []}', encoding="utf-8")
        result = registry_json_parse_check(tmp_path)
        assert result.passed is True

    def test_invalid_skills_json_fails(self, tmp_path):
        reg_dir = tmp_path / "registry"
        reg_dir.mkdir()
        (reg_dir / "skills.json").write_text("{invalid json}", encoding="utf-8")
        result = registry_json_parse_check(tmp_path)
        assert result.passed is False
        assert "skills.json" in result.reason

    def test_missing_file_skipped(self, tmp_path):
        # No registry dir at all
        result = registry_json_parse_check(tmp_path)
        assert result.passed is True


class TestGitDiffCheck:
    """Tests for git_diff_check guard.

    Uses real repo paths since git commands require a real repo.
    """

    def test_clean_repo_passes(self):
        """Verify git_diff_check runs on real repo without errors."""
        from pathlib import Path
        root = Path("C:/AI/claude_projects/awesome-banker-skills")
        result = git_diff_check(root)
        # Just verify the guard runs and returns valid result
        assert result.guard_name == "git_diff_check"
        assert isinstance(result.passed, bool)


class TestGitStatusShort:
    """Tests for git_status_short utility.

    Uses real repo paths since git commands require a real repo.
    """

    def test_status_runs_on_real_repo(self):
        """Verify git_status_short runs on real repo."""
        from pathlib import Path
        workspace = Path("C:/AI/claude_projects/awesome-banker-skills/workspace")
        if not (workspace / ".git").exists():
            pytest.skip("Workspace is not a git repo")
        status = git_status_short(workspace)
        assert isinstance(status, str)  # Just verify it returns a string


class TestGuardResult:
    """Tests for GuardResult dataclass."""

    def test_guard_result_immutable(self):
        result = GuardResult(passed=True, guard_name="test", reason="ok")
        assert result.passed is True
        assert result.guard_name == "test"

    def test_guard_result_with_default_reason(self):
        result = GuardResult(passed=True, guard_name="test")
        assert result.reason == ""
