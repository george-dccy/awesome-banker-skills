#!/usr/bin/env python3
"""Build routing context for market-corporate-client."""

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
        pattern=r"结算|账户|收付|回单|对账",
        pack_id="pack.banks.ceb.corporate-settlement.basic-settlement",
        priority=95,
        reason="命中基础结算场景关键词",
    ),
    PackRule(
        pattern=r"e付通|订单|账单|开票|协同",
        pack_id="pack.banks.ceb.transaction-banking.yangguang-e-pay",
        priority=110,
        reason="命中交易协同场景关键词",
    ),
    PackRule(
        pattern=r"电费证|电费|电网|国内证|福费廷",
        pack_id="pack.banks.ceb.trade-finance.yangguang-electricity-certificate",
        priority=110,
        reason="命中电费场景融资关键词",
    ),
    PackRule(
        pattern=r"思维|复盘|优先级|执行节奏",
        pack_id="pack.common.banker-thinking.top-performer",
        priority=35,
        reason="命中推进方法关键词",
    ),
    PackRule(
        pattern=r"利率|通胀|周期|宏观|现金流",
        pack_id="pack.common.economics.business-basics",
        priority=30,
        reason="命中经营环境解释关键词",
    ),
    PackRule(
        pattern=r"销售|异议|洞察|推进|开场",
        pack_id="pack.common.sales.consultative-b2b",
        priority=45,
        reason="命中营销沟通关键词",
    ),
    PackRule(
        pattern=r"心理|信任|偏差|沟通摩擦",
        pack_id="pack.common.psychology.business-communication",
        priority=30,
        reason="命中信任与沟通关键词",
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
                "reason": "未命中特定关键词，默认先走基础结算场景",
            }
        )
    scored.sort(key=lambda item: int(item["priority"]), reverse=True)
    return scored


def infer_mode(question: str) -> str:
    if DEMO_PATTERN.search(question):
        return "meeting-demo"
    if re.search(r"首次|第一次|拜访|开场|触达", question):
        return "first-touch"
    return "routine-marketing"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", required=True, help="Question text")
    args = parser.parse_args()
    routed = route_packs(args.question)
    primary = routed[0]["pack_id"]
    payload = {
        "skill": "market-corporate-client",
        "mode": infer_mode(args.question),
        "recommended_packs": [item["pack_id"] for item in routed],
        "primary_pack": primary,
        "backup_pack": routed[1]["pack_id"] if len(routed) > 1 else None,
        "routing_reasons": routed,
        "reading_order": [
            "references/pre-call-diagnosis.md",
            "references/opening-playbook.md",
            "references/knowledge-routing.md",
            f"{primary} -> README.md / modules/* / faq.md / sources.md",
        ],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
