#!/usr/bin/env python3
"""
validate-scenario.py

校验普惠金融场景判断输出的完整性和合规性。
运行方式：python validate-scenario.py <output_file.md>
"""

import sys
import re

REQUIRED_FIELDS = [
    "场景判断结论",
    "适用客群分类",
    "政策依据层级",
    "产品候选方向",
    "边界提示",
]

RISK_PATTERNS = [
    (r"可以.*办理", "承诺办理"),
    (r"保证.*放款", "承诺放款"),
    (r"一定.*额度", "承诺额度"),
    (r"肯定.*批", "承诺审批"),
    (r".*授信.*没问题", "承诺授信"),
    (r"费率.*没问题", "承诺费率"),
    (r"利率.*没问题", "承诺利率"),
    (r".*批.*没问题", "承诺批核"),
    (r"肯定.*通过", "承诺通过"),
]

INCLUSIVE_FINANCE_PHRASES = [
    "普惠",
    "小微",
    "三农",
    "阳光普惠",
    "阳光兴农",
    "小微企业贷款",
    "个体工商户",
    "涉农贷款",
]

def validate_scenario(content: str) -> dict:
    """Validate inclusive finance scenario judgment output."""
    issues = []
    warnings = []

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in content:
            issues.append(f"缺少必需字段：{field}")

    # Check scenario judgment conclusion
    if "场景判断结论" in content:
        judgment_match = re.search(r"场景判断结论[：:]\s*(属于普惠|可能属于普惠|不属于普惠|待核实)", content)
        if not judgment_match:
            warnings.append("场景判断结论未标注明确结论（属于普惠/可能属于普惠/不属于普惠/待核实）")
        else:
            judgment = judgment_match.group(1)
            # If "不属于普惠", should have clear reason
            if judgment == "不属于普惠":
                reason_section = re.search(r"场景判断结论.*?(?=\n##|\n#|\Z)", content, re.DOTALL)
                if reason_section and len(reason_section.group(0)) < 30:
                    warnings.append("判断为不属于普惠但原因说明不足")

    # Check policy level field
    if "政策依据层级" in content:
        policy_section = re.search(r"政策依据层级[：:](.*?)(?=\n##|\n#|\Z)", content, re.DOTALL)
        if policy_section:
            policy_text = policy_section.group(1)
            # Should mention at least one policy level
            level_mentioned = any(
                level in policy_text for level in ["国家级", "监管", "行内", "地方"]
            )
            if not level_mentioned:
                warnings.append("政策依据层级未标注具体来源级别")

    # Check risk patterns
    for pattern, risk_type in RISK_PATTERNS:
        if re.search(pattern, content):
            issues.append(f"检测到{risk_type}相关表述，需确认是否符合合规要求")

    # Check for customer sensitive info (basic check)
    sensitive_patterns = [
        r"\d{18}",  # ID number
        r"622202\d{13}",  # Bank card (partial)
        r"\*\*\*\*",  # Masked info followed by unmasked
    ]
    for pattern in sensitive_patterns:
        if re.search(pattern, content):
            issues.append("检测到疑似客户敏感信息，请确认已脱敏")

    # Check if scene judgment has meaningful content
    if "场景判断结论" in content:
        judgment_section = re.search(r"场景判断结论[：:].*?(?=\n##|\n#|\Z)", content, re.DOTALL)
        if judgment_section:
            judgment_text = judgment_section.group(0)
            if len(judgment_text.strip()) < 15:
                issues.append("场景判断结论内容过少")

    # Check if product recommendation is present
    if "产品候选方向" in content:
        product_section = re.search(r"产品候选方向[：:](.*?)(?=\n##|\n#|\Z)", content, re.DOTALL)
        if product_section:
            product_text = product_section.group(1)
            # Should mention at least one product direction
            product_mentioned = any(
                product in product_text for product in ["阳光普惠", "阳光兴农", "灵工通", "安居通", "物流通"]
            )
            if not product_mentioned:
                warnings.append("产品候选方向未标注具体产品方向")

    # Check boundary tips
    if "边界提示" in content:
        boundary_section = re.search(r"边界提示[：:](.*?)(?=\n##|\n#|\Z)", content, re.DOTALL)
        if boundary_section:
            boundary_text = boundary_section.group(1)
            if len(boundary_text.strip()) < 10:
                warnings.append("边界提示内容过少")
    else:
        warnings.append("未找到边界提示部分")

    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "warnings": warnings,
    }

def main():
    if len(sys.argv) < 2:
        print("用法: python validate-scenario.py <output_file.md>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误：文件不存在 {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"错误：读取文件失败 {e}")
        sys.exit(1)

    result = validate_scenario(content)

    print("=" * 50)
    print("普惠金融场景判断输出校验结果")
    print("=" * 50)

    if result["valid"]:
        print("✓ 校验通过")
    else:
        print("✗ 校验失败")
        for issue in result["issues"]:
            print(f"  - {issue}")

    if result["warnings"]:
        print("\n⚠ 警告")
        for warning in result["warnings"]:
            print(f"  - {warning}")

    sys.exit(0 if result["valid"] else 1)

if __name__ == "__main__":
    main()
