#!/usr/bin/env python3
"""Validate output structure for accompany-corporate-client."""

import argparse
import sys


REQUIRED_SECTIONS = ["客户关系温度", "待回应问题清单", "本次跟进动作", "内部协同清单", "下一次触达计划"]


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
