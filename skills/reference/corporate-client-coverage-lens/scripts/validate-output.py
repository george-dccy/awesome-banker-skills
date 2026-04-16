#!/usr/bin/env python3
"""Validate output structure for corporate-client-coverage-lens."""

import argparse
import sys


REQUIRED_SECTIONS = ["专业判断", "优先级", "关键对象", "建议补读", "风险与边界"]
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
    args = parser.parse_args()

    missing = [section for section in REQUIRED_SECTIONS if section not in args.text]
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
