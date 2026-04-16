#!/usr/bin/env python3
"""Validate output structure for market-corporate-client."""

import argparse
import sys


REQUIRED_SECTIONS = ["客户场景初判", "推荐切入口", "首次会谈目标", "不宜过早触达的话题", "会后推进动作"]
DEMO_SECTION = "客户常见追问与建议回答"
FORBIDDEN_PROMISE_PATTERNS = [
    "保证通过",
    "肯定能批",
    "可以直接批",
    "额度肯定",
    "费率就是",
    "马上能办",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True, help="Output text to validate")
    parser.add_argument(
        "--mode",
        default="routine-marketing",
        choices=["routine-marketing", "first-touch", "meeting-demo"],
        help="Output mode from build-context",
    )
    args = parser.parse_args()
    missing = [section for section in REQUIRED_SECTIONS if section not in args.text]
    if args.mode == "meeting-demo" and DEMO_SECTION not in args.text:
        missing.append(DEMO_SECTION)
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
