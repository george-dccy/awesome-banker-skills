---
name: market-corporate-client
description: 对公客户营销流程技能。用于营销前诊断、切入口设计、会谈目标定义和会后推进动作。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  banker_kind: workflow
  display_name_zh: 对公客户营销
  related_packs:
    - pack.banks.ceb.corporate-settlement.basic-settlement
    - pack.banks.ceb.transaction-banking.yangguang-e-pay
    - pack.banks.ceb.trade-finance.yangguang-electricity-certificate
    - pack.common.banker-thinking.top-performer
    - pack.common.economics.business-basics
    - pack.common.sales.consultative-b2b
    - pack.common.psychology.business-communication
  related_prompts:
    - prompt.workflow.market-corporate-client
  references_dir: references
  scripts_dir: scripts
---

# 对公客户营销 Skill

## Scope

这个 workflow 聚焦“营销前”和“首次接触”，目标是形成可执行的切入口与下一步动作。

## Required Reads

1. `references/pre-call-diagnosis.md`
2. `references/opening-playbook.md`
3. `references/knowledge-routing.md`

## Output Contract

输出至少包含：

1. 客户场景初判
2. 推荐切入口（1-3 个）
3. 首次会谈目标
4. 不宜过早触达的话题
5. 会后推进动作

## Script Hooks

- `scripts/build-context.py`
- `scripts/validate-output.py`
