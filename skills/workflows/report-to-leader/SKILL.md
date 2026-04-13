---
name: report-to-leader
description: 向领导汇报的标准化流程技能。把业务事实、进展、问题和决策诉求整理为可拍板的输出。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  banker_kind: workflow
  display_name_zh: 向领导汇报
  related_packs:
    - pack.banks.ceb.corporate-settlement.basic-settlement
    - pack.banks.ceb.transaction-banking.yangguang-e-pay
    - pack.banks.ceb.trade-finance.yangguang-electricity-certificate
  related_prompts:
    - prompt.workflow.report-to-leader
  references_dir: references
  scripts_dir: scripts
---

# 向领导汇报 Skill

## Scope

把“信息汇报”升级成“决策支持”，输出必须支持领导快速判断是否继续推进。

## Required Reads

1. `references/report-structure.md`
2. `references/decision-signals.md`
3. `references/knowledge-routing.md`

## Knowledge Link

当汇报涉及产品事实时，从 `references/knowledge-routing.md` 路由到对应 knowledge pack。

## Output Contract

必须包含：

1. 一句话结论
2. 本周/本阶段关键事实
3. 当前卡点
4. 建议动作
5. 需要领导拍板项

## Script Hooks

- `scripts/build-context.py`：按主题推荐需要引用的知识包
- `scripts/validate-output.py`：校验汇报结构与决策字段
