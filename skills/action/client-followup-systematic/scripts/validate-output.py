#!/usr/bin/env python3
"""Validate client-followup-systematic skill output structure."""

import json
import sys
from pathlib import Path

def validate_output(output_text: str) -> tuple[bool, list[str]]:
    """Validate that output contains required sections."""
    errors = []
    required = ["事项状态评估", "优先级排序", "下一步动作", "协同需求", "风险信号"]
    for req in required:
        if req not in output_text:
            errors.append(f"Missing required section: {req}")

    # Check for prohibited content
    prohibited = ["承诺.*时间", "保证.*完成", "授信.*通过", "审批.*通过"]
    import re
    for pattern in prohibited:
        if re.search(pattern, output_text):
            errors.append(f"Potential commitment risk detected: {pattern}")

    return len(errors) == 0, errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate-output.py <output_text_file>")
        sys.exit(1)

    output_file = Path(sys.argv[1])
    if not output_file.exists():
        print(f"File not found: {output_file}")
        sys.exit(1)

    output_text = output_file.read_text(encoding="utf-8")
    valid, errors = validate_output(output_text)

    if valid:
        print("Validation passed.")
        sys.exit(0)
    else:
        print("Validation failed:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
