#!/usr/bin/env python3
"""Validate output structure for corp-relationship-manager."""

import argparse
import sys


REQUIRED_SECTIONS = ["场景判断", "机会假设", "建议切入口", "下一步推进动作", "风险与边界"]
DEMO_SECTIONS = ["客户可能会问的3个问题", "建议应答话术"]
FORBIDDEN_PROMISE_PATTERNS = [
    "保证通过",
    "确保通过",
    "肯定能批",
    "可以批",
    "直接给额度",
    "费率就是",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True, help="Output text to validate")
    parser.add_argument(
        "--mode",
        default="routine-consulting",
        choices=["routine-consulting", "first-touch", "meeting-demo"],
        help="Output mode from build-context",
    )
    args = parser.parse_args()

    missing = [section for section in REQUIRED_SECTIONS if section not in args.text]
    if args.mode == "meeting-demo":
        missing.extend(section for section in DEMO_SECTIONS if section not in args.text)
    if missing:
        print("FAIL: missing sections -> " + ", ".join(missing))
        sys.exit(1)
    forbidden = [pattern for pattern in FORBIDDEN_PROMISE_PATTERNS if pattern in args.text]
    if forbidden:
        print("FAIL: found risky promise words -> " + ", ".join(forbidden))
        sys.exit(1)
    print("PASS: output structure is complete")


if __name__ == "__main__":
    main()
