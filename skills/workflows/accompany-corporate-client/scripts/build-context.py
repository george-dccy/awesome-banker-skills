#!/usr/bin/env python3
"""Build routing context for accompany-corporate-client."""

import argparse
import json
import re


PACK_RULES = [
    (r"结算|账户|收付|回单|对账", "pack.banks.ceb.corporate-settlement.basic-settlement"),
    (r"e付通|订单|账单|开票|协同", "pack.banks.ceb.transaction-banking.yangguang-e-pay"),
    (r"电费证|电费|电网|国内证|福费廷", "pack.banks.ceb.trade-finance.yangguang-electricity-certificate"),
    (r"复盘|关系经营|优先级|执行节奏", "pack.common.banker-thinking.top-performer"),
    (r"销售|异议|推进|顾问式", "pack.common.sales.consultative-b2b"),
    (r"心理|信任|偏差|沟通摩擦|冲突", "pack.common.psychology.business-communication"),
]


def route_packs(question: str) -> list[str]:
    hits: list[str] = []
    for pattern, pack_id in PACK_RULES:
        if re.search(pattern, question):
            hits.append(pack_id)
    if not hits:
        hits.append("pack.banks.ceb.corporate-settlement.basic-settlement")
    return hits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", required=True, help="Question text")
    args = parser.parse_args()
    payload = {"skill": "accompany-corporate-client", "recommended_packs": route_packs(args.question)}
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
