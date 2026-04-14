#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json


ROLE_TITLES = ["岗位", "客户经理", "理财经理", "产品经理", "管理者", "领导层", "支行长"]
ROLE_STRONG_INDICATORS = [
    "岗位视角",
    "岗位使命",
    "默认视角",
    "优先级规则",
    "关键对象",
    "常见误区",
    "角色边界",
    "调用规则",
]
WORKFLOW_INDICATORS = [
    "最低输入",
    "输入字段",
    "动作顺序",
    "输出结构",
    "检查点",
    "失败场景",
    "编排",
    "workflow",
]
KNOWLEDGE_INDICATORS = ["公开知识", "公开产品", "faq", "sources", "来源", "知识包", "pack"]
METHOD_INDICATORS = [
    "方法论",
    "框架",
    "推进法",
    "复盘法",
    "汇报法",
    "管理法",
    "可复用",
    "跨岗位",
    "跨场景",
    "method",
]
STAKEHOLDER_INDICATORS = ["老板", "财务", "业务负责人", "内部协同", "怎么沟通", "沟通差异"]


def has_any(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def classify(text: str) -> dict[str, str]:
    lowered = text.lower()
    if has_any(text, WORKFLOW_INDICATORS) or "input" in lowered:
        return {
            "asset_kind": "workflow",
            "recommended_root": "skills/workflows",
            "reason": "内容更像场景最低输入、动作顺序、输出结构或检查点。",
        }
    if has_any(text, ROLE_STRONG_INDICATORS) or (
        has_any(text, ROLE_TITLES) and has_any(text, STAKEHOLDER_INDICATORS)
    ) or "role" in lowered:
        return {
            "asset_kind": "role",
            "recommended_root": "skills/roles",
            "reason": "内容更像岗位视角、优先级规则、关键对象沟通差异或调用规则。",
        }
    if has_any(text, KNOWLEDGE_INDICATORS) or "knowledge" in lowered:
        return {
            "asset_kind": "knowledge-pack",
            "recommended_root": "knowledge-packs/common",
            "reason": "内容更像公开事实、公开产品说明或可引用来源。",
        }
    if has_any(text, METHOD_INDICATORS) or "method" in lowered:
        return {
            "asset_kind": "method",
            "recommended_root": "methods/reusable",
            "reason": "内容更像可跨岗位复用的方法论或框架。",
        }
    if has_any(text, ROLE_TITLES):
        return {
            "asset_kind": "role",
            "recommended_root": "skills/roles",
            "reason": "内容直接围绕某个岗位展开，默认优先归入岗位视角层。",
        }
    return {
        "asset_kind": "unknown",
        "recommended_root": "workspace/private",
        "reason": "暂时无法判断资产边界，建议先写到 private 再细分。",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Recommend where a new asset should live.")
    parser.add_argument("--text", default="", help="Source text or task summary to classify.")
    parser.add_argument(
        "--mode",
        default="private-first",
        choices=["private-first", "public-candidate"],
        help="Preferred drafting mode.",
    )
    args = parser.parse_args()

    if not args.text:
        print(
            json.dumps(
                {
                    "default_mode": "private-first",
                    "private_root": "workspace/private",
                    "message": "Provide --text to classify the target asset.",
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    result = classify(args.text)
    result["mode"] = args.mode
    if args.mode == "private-first":
        result["draft_root"] = "workspace/private"
    else:
        result["draft_root"] = result["recommended_root"]
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
