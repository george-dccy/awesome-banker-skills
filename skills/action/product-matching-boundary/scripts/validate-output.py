#!/usr/bin/env python3
"""
validate-output.py
校验 product-matching-boundary skill 输出的结构完整性与承诺风险
"""

import sys
import json
import re
from pathlib import Path


def validate_output(output_text: str) -> tuple[bool, list[str]]:
    """校验输出是否满足质量门槛"""
    issues = []

    # 检查点1：是否包含产品候选列表
    if not re.search(r"产品候选", output_text):
        issues.append("缺少产品候选列表")

    # 检查点2：是否包含边界提示
    if not re.search(r"边界提示|边界", output_text):
        issues.append("缺少边界提示")

    # 检查点3：是否避免定价/费率承诺
    forbidden_patterns = [
        (r"费率[是为]?\d", "费率承诺"),
        (r"利率[是为]?\d", "利率承诺"),
        (r"承诺.*放款", "放款承诺"),
        (r"保证.*通过", "审批通过承诺"),
        (r"一定能.*办理", "办理承诺"),
    ]
    for pattern, label in forbidden_patterns:
        if re.search(pattern, output_text):
            issues.append(f"包含禁止内容：{label}")

    # 检查点4：是否有协同需求判断
    if not re.search(r"协同|跨条线|条线", output_text):
        issues.append("缺少协同需求判断")

    # 检查点5：是否有下一轮动作建议
    if not re.search(r"下一轮|建议动作|下一步", output_text):
        issues.append("缺少下一轮动作建议")

    return len(issues) == 0, issues


def main():
    if len(sys.argv) < 2:
        print("Usage: validate-output.py <output_file>")
        sys.exit(1)

    output_file = Path(sys.argv[1])
    if not output_file.exists():
        print(f"File not found: {output_file}")
        sys.exit(1)

    output_text = output_file.read_text(encoding="utf-8")
    valid, issues = validate_output(output_text)

    if valid:
        print("PASS: 输出结构完整，无承诺风险")
        sys.exit(0)
    else:
        print("FAIL: 发现以下问题：")
        for issue in issues:
            print(f"  - {issue}")
        sys.exit(1)


if __name__ == "__main__":
    main()
