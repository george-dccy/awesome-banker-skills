#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json


REFERENCE_INDICATORS = [
    "视角",
    "判断框架",
    "表达结构",
    "优先级规则",
    "关键对象",
    "误区",
    "framework",
    "lens",
]
ACTION_INDICATORS = [
    "最低输入",
    "输入字段",
    "动作顺序",
    "输出结构",
    "检查点",
    "失败场景",
    "场景编排",
    "workflow",
    "action",
]
KNOWLEDGE_INDICATORS = ["公开知识", "公开产品", "faq", "sources", "来源", "知识包", "knowledge"]


def has_any(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def classify(text: str) -> dict[str, str]:
    lowered = text.lower()
    if has_any(text, ACTION_INDICATORS) or "input" in lowered:
        return {
            "asset_kind": "action-skill",
            "recommended_root": "skills/action",
            "reason": "内容更像具体任务的输入、步骤、输出或检查点。",
        }
    if has_any(text, REFERENCE_INDICATORS) or "reference" in lowered:
        return {
            "asset_kind": "reference-skill",
            "recommended_root": "skills/reference",
            "reason": "内容更像专业视角、判断框架或表达结构。",
        }
    if has_any(text, KNOWLEDGE_INDICATORS):
        return {
            "asset_kind": "knowledge",
            "recommended_root": "knowledge/common",
            "reason": "内容更像公开事实、公开产品说明或可引用来源。",
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
    result["draft_root"] = "workspace/private" if args.mode == "private-first" else result["recommended_root"]
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
