#!/usr/bin/env python3
"""Build routing context for corp-relationship-manager."""

import argparse
import json
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class PackRule:
    pattern: str
    pack_id: str
    priority: int
    reason: str


PACK_RULES = [
    PackRule(
        pattern=r"结算|账户|收款|付款|回单|对账|权限",
        pack_id="pack.banks.ceb.corporate-settlement.basic-settlement",
        priority=100,
        reason="命中对公基础结算关键词",
    ),
    PackRule(
        pattern=r"e付通|订单|账单|开票|协同|供应链",
        pack_id="pack.banks.ceb.transaction-banking.yangguang-e-pay",
        priority=110,
        reason="命中交易银行协同关键词",
    ),
    PackRule(
        pattern=r"电费证|电费|电网|国内证|福费廷",
        pack_id="pack.banks.ceb.trade-finance.yangguang-electricity-certificate",
        priority=110,
        reason="命中电费证/国内证场景关键词",
    ),
    PackRule(
        pattern=r"思维|复盘|优先级|执行节奏|长期主义",
        pack_id="pack.common.banker-thinking.top-performer",
        priority=40,
        reason="命中客户经理方法与执行节奏关键词",
    ),
    PackRule(
        pattern=r"利率|通胀|周期|宏观|现金流",
        pack_id="pack.common.economics.business-basics",
        priority=30,
        reason="命中经营与宏观解释关键词",
    ),
    PackRule(
        pattern=r"销售|异议|洞察|推进|开场",
        pack_id="pack.common.sales.consultative-b2b",
        priority=50,
        reason="命中顾问式销售推进关键词",
    ),
    PackRule(
        pattern=r"心理|信任|偏差|沟通摩擦|冲突",
        pack_id="pack.common.psychology.business-communication",
        priority=30,
        reason="命中客户沟通心理关键词",
    ),
]

DEMO_PATTERN = re.compile(r"演示|会上|业务会|汇报|示例|问答")

DEFAULT_PRIMARY_PACK = "pack.banks.ceb.corporate-settlement.basic-settlement"


def route_packs(question: str) -> list[dict[str, object]]:
    scored: list[dict[str, object]] = []
    for rule in PACK_RULES:
        if re.search(rule.pattern, question):
            scored.append(
                {
                    "pack_id": rule.pack_id,
                    "priority": rule.priority,
                    "reason": rule.reason,
                }
            )
    if not scored:
        scored.append(
            {
                "pack_id": DEFAULT_PRIMARY_PACK,
                "priority": 90,
                "reason": "未命中特定关键词，默认先走对公基础结算包",
            }
        )
    scored.sort(key=lambda item: int(item["priority"]), reverse=True)
    return scored


def infer_mode(question: str) -> str:
    if DEMO_PATTERN.search(question):
        return "meeting-demo"
    if re.search(r"首次|第一次|拜访|开场|触达", question):
        return "first-touch"
    return "routine-consulting"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", required=True, help="User question or scenario text")
    args = parser.parse_args()
    routed = route_packs(args.question)
    top_pack = routed[0]["pack_id"]

    payload = {
        "skill": "corp-relationship-manager",
        "mode": infer_mode(args.question),
        "recommended_packs": [item["pack_id"] for item in routed],
        "routing_reasons": routed,
        "reading_order": [
            "references/role-methodology.md",
            "references/knowledge-routing.md",
            "references/output-contract.md",
            f"{top_pack} -> README.md / modules/* / faq.md / sources.md",
        ],
        "references": [
            "references/role-methodology.md",
            "references/knowledge-routing.md",
            "references/output-contract.md",
        ],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
