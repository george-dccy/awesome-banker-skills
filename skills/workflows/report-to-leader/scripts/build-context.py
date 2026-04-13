#!/usr/bin/env python3
"""Build routing context for report-to-leader."""

import argparse
import json
import re


PACK_RULES = [
    (r"结算|账户|收付|回单|对账", "pack.banks.ceb.corporate-settlement.basic-settlement"),
    (r"e付通|订单|账单|开票|协同", "pack.banks.ceb.transaction-banking.yangguang-e-pay"),
    (r"电费证|国内证|福费廷|电网", "pack.banks.ceb.trade-finance.yangguang-electricity-certificate"),
]


def route_packs(topic: str) -> list[str]:
    hits: list[str] = []
    for pattern, pack_id in PACK_RULES:
        if re.search(pattern, topic):
            hits.append(pack_id)
    if not hits:
        hits.append("pack.banks.ceb.corporate-settlement.basic-settlement")
    return hits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True, help="Topic for leader report")
    args = parser.parse_args()
    payload = {"skill": "report-to-leader", "recommended_packs": route_packs(args.topic)}
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
