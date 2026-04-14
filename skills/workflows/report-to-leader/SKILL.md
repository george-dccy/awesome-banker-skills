---
name: report-to-leader
description: 向领导汇报的标准化流程技能。把业务事实、进展、问题和决策诉求整理为可拍板的输出。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  banker_kind: workflow
  display_name_zh: 向领导汇报
  orchestration_focus: 银行汇报场景编排
  related_methods:
    - method.communication-reporting.leader-decision-brief
  related_packs:
    - pack.banks.ceb.corporate-settlement.basic-settlement
    - pack.banks.ceb.transaction-banking.yangguang-e-pay
    - pack.banks.ceb.trade-finance.yangguang-electricity-certificate
    - pack.common.banker-thinking.top-performer
    - pack.common.economics.business-basics
    - pack.common.psychology.business-communication
  related_prompts:
    - prompt.workflow.report-to-leader
  references_dir: references
  scripts_dir: scripts
---

# 向领导汇报 Skill

## Scope

这个 workflow 是“银行汇报场景编排器”，负责组织汇报所需事实、调用 `leader-decision-brief` 方法，并输出可拍板结果。

## Required Reads

1. `references/report-structure.md`
2. `references/decision-signals.md`
3. `references/knowledge-routing.md`
4. `method.communication-reporting.leader-decision-brief`

## Knowledge Link

当汇报涉及产品事实时，从 `references/knowledge-routing.md` 路由到对应 knowledge pack。

## Input Contract

最低输入：

- 汇报类型
- 当前进展
- 当前卡点
- 期望领导拍板或支持的事项

## Orchestration Rule

1. 先采集当前阶段的关键事实和变化
2. 再用 `leader-decision-brief` 组织成可拍板结构
3. 涉及公开产品事实时，再补充对应 knowledge pack 依据

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
