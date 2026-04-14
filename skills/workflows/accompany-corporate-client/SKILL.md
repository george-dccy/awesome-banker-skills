---
name: accompany-corporate-client
description: 对公客户陪伴流程技能。用于会后跟进、问题闭环、跨团队协调和关系持续经营。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  banker_kind: workflow
  display_name_zh: 对公客户陪伴
  orchestration_focus: 客户陪伴场景编排
  related_methods:
    - method.business-operations.client-advance-map
    - method.management.team-followup-loop
  related_packs:
    - pack.banks.ceb.corporate-settlement.basic-settlement
    - pack.banks.ceb.transaction-banking.yangguang-e-pay
    - pack.banks.ceb.trade-finance.yangguang-electricity-certificate
    - pack.common.banker-thinking.top-performer
    - pack.common.sales.consultative-b2b
    - pack.common.psychology.business-communication
  related_prompts:
    - prompt.workflow.accompany-corporate-client
  references_dir: references
  scripts_dir: scripts
---

# 对公客户陪伴 Skill

## Scope

这个 workflow 是“客户陪伴场景编排器”，负责客户关系推进、问题闭环和下一次触达计划，不替代团队管理方法本体。

## Required Reads

1. `references/follow-up-cadence.md`
2. `references/issue-closure-model.md`
3. `references/knowledge-routing.md`
4. `method.business-operations.client-advance-map`
5. `method.management.team-followup-loop`

## Input Contract

最低输入：

- 当前客户关系阶段
- 待回应问题或未闭环事项
- 需要协同的内部角色
- 下一次触达希望达成的目标

## Orchestration Rule

1. 先用 `client-advance-map` 判断当前推进节奏和下一步动作
2. 再用 `team-followup-loop` 组织内部协同闭环
3. 需要补充公开事实时，再按 `knowledge-routing` 调用对应 pack

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
