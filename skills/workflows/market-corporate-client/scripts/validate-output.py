#!/usr/bin/env python3
"""Validate output structure for market-corporate-client."""

import argparse
import sys


REQUIRED_SECTIONS = ["客户场景初判", "推荐切入口", "首次会谈目标", "不宜过早触达的话题", "会后推进动作"]


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
