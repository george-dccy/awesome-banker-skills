#!/usr/bin/env python3
"""Validate output structure for corp-relationship-manager."""

import argparse
import sys


REQUIRED_SECTIONS = ["场景判断", "机会假设", "建议切入口", "下一步推进动作", "风险与边界"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True, help="Output text to validate")
    args = parser.parse_args()

    missing = [section for section in REQUIRED_SECTIONS if section not in args.text]
    if missing:
        print("FAIL: missing sections -> " + ", ".join(missing))
        sys.exit(1)
    print("PASS: output structure is complete")


if __name__ == "__main__":
    main()
