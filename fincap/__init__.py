"""Financial Capability Kit -无人值守循环验证门禁.

子模块:
    guards: 验证门禁函数
    verification: 验证报告生成
"""

from fincap.guards import (
    GuardResult,
    DRIFT_KEYWORDS,
    COMPLIANCE_STOP_PATTERNS,
    git_command,
    git_status_short,
    public_repo_dirty_check,
    workspace_dirty_check,
    route_conflict_keyword_check,
    queue_status_check,
    registry_json_parse_check,
    git_diff_check,
    compliance_stop_check,
    run_all_pre_run_guards,
    format_guard_results,
)

from fincap.verification import (
    VerificationReport,
    run_post_verification,
    generate_verification_report,
)

__all__ = [
    "GuardResult",
    "DRIFT_KEYWORDS",
    "COMPLIANCE_STOP_PATTERNS",
    "git_command",
    "git_status_short",
    "public_repo_dirty_check",
    "workspace_dirty_check",
    "route_conflict_keyword_check",
    "queue_status_check",
    "registry_json_parse_check",
    "git_diff_check",
    "compliance_stop_check",
    "run_all_pre_run_guards",
    "format_guard_results",
    "VerificationReport",
    "run_post_verification",
    "generate_verification_report",
]
