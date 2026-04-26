"""Verification module for fincap agent-loop post-run checks.

This module orchestrates all post-run verification steps and generates
verification reports that are included in run reports.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from fincap.guards import (
    GuardResult,
    git_diff_check,
    public_repo_dirty_check,
    registry_json_parse_check,
    route_conflict_keyword_check,
    compliance_stop_check,
    format_guard_results,
    workspace_dirty_check,
)


@dataclass
class VerificationReport:
    """Complete verification report for an agent run."""

    pre_run_guards: list[GuardResult] = field(default_factory=list)
    post_run_guards: list[GuardResult] = field(default_factory=list)
    public_repo_changed: bool = False
    public_repo_status: str = ""

    @property
    def all_passed(self) -> bool:
        """Return True if all critical guards passed."""
        return all(r.passed for r in self.pre_run_guards + self.post_run_guards)

    @property
    def stop_required(self) -> bool:
        """Return True if any guard requires stopping."""
        critical_guards = self.pre_run_guards + self.post_run_guards
        return any(not r.passed for r in critical_guards)

    def format_summary(self) -> str:
        """Format a human-readable summary for run reports."""
        lines = ["## 验证门禁结果", ""]
        lines.append("### Pre-run Guards")
        lines.append(format_guard_results(self.pre_run_guards) or "- (none run)")
        lines.append("")
        lines.append("### Post-run Guards")
        lines.append(format_guard_results(self.post_run_guards) or "- (none run)")
        lines.append("")
        if self.public_repo_changed:
            lines.append(f"### Public Repo Changed\n- Yes (status):\n  ```\n  {self.public_repo_status}\n  ```")
        else:
            lines.append("### Public Repo Changed\n- No")
        return "\n".join(lines)


def run_post_verification(
    root: Path,
    workspace: Path,
    agent_output: str = "",
) -> list[GuardResult]:
    """Run all post-run guards.

    Args:
        root: Public repo root path
        workspace: Workspace path
        agent_output: Raw agent output text to check for drift/compliance issues

    Returns:
        List of GuardResults from post-run checks
    """
    results: list[GuardResult] = []

    # Git diff check
    results.append(git_diff_check(root))

    # Public repo dirty check (should be clean before run, any change after run needs review)
    pub_status = public_repo_dirty_check(root)
    if not pub_status.passed:
        results.append(pub_status)

    # Check agent output for route conflict keywords
    if agent_output:
        results.append(route_conflict_keyword_check(agent_output))
        results.append(compliance_stop_check(agent_output))

    # Workspace dirty check is informational
    results.append(workspace_dirty_check(workspace))

    return results


def generate_verification_report(
    root: Path,
    workspace: Path,
    pre_run_guards: list[GuardResult],
    agent_output: str = "",
) -> VerificationReport:
    """Generate a complete verification report.

    Args:
        root: Public repo root path
        workspace: Workspace path
        pre_run_guards: Results from pre-run guard checks
        agent_output: Agent output text to check

    Returns:
        VerificationReport with all guard results
    """
    post_run_guards = run_post_verification(root, workspace, agent_output)

    # Get public repo status for report
    from fincap.guards import git_status_short

    pub_status = git_status_short(root)

    return VerificationReport(
        pre_run_guards=pre_run_guards,
        post_run_guards=post_run_guards,
        public_repo_changed=bool(pub_status),
        public_repo_status=pub_status,
    )
