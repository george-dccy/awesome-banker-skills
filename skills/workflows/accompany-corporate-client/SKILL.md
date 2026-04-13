---
name: accompany-corporate-client
description: 对公客户陪伴流程技能。用于会后跟进、问题闭环、跨团队协调和关系持续经营。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  banker_kind: workflow
  display_name_zh: 对公客户陪伴
  related_packs:
    - pack.banks.ceb.corporate-settlement.basic-settlement
    - pack.banks.ceb.transaction-banking.yangguang-e-pay
    - pack.banks.ceb.trade-finance.yangguang-electricity-certificate
  related_prompts:
    - prompt.workflow.accompany-corporate-client
  references_dir: references
  scripts_dir: scripts
---

# 对公客户陪伴 Skill

## Scope

该 workflow 关注“持续推进”，强调节奏管理、问题闭环和信任维护。

## Required Reads

1. `references/follow-up-cadence.md`
2. `references/issue-closure-model.md`
3. `references/knowledge-routing.md`

## Output Contract

必须包含：

1. 客户关系温度
2. 待回应问题清单
3. 本次跟进动作
4. 内部协同清单
5. 下一次触达计划

## Script Hooks

- `scripts/build-context.py`
- `scripts/validate-output.py`
