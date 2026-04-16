#!/usr/bin/env python3
"""Validate output structure for report-to-leader."""

import argparse
import sys


REQUIRED_SECTIONS = ["一句话结论", "关键事实", "当前卡点", "建议动作", "需要领导拍板项"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True, help="Output text to validate")
    args = parser.parse_args()
    missing = [section for section in REQUIRED_SECTIONS if section not in args.text]
    if missing:
        print("FAIL: missing sections -> " + ", ".join(missing))
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()
