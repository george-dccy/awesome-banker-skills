---
name: client-followup-systematic
description: Use when needing to systematically push outstanding items forward, assess status, prioritize next actions, and drive closure after client interactions.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: execute
  display_name_zh: 客户事项系统跟进
  audience: [bank-practitioner]
  related_skills:
    - skill.reference.client-advance-framework
    - skill.reference.team-followup-framework
    - skill.reference.corporate-client-coverage-lens
  related_knowledge:
    - knowledge.common.sales.consultative-b2b
    - knowledge.common.banker-thinking.top-performer
    - knowledge.common.psychology.business-communication
  related_prompts:
    - prompt.skill.action.client-followup-systematic
  references_dir: references
  scripts_dir: scripts
---

# 客户事项系统跟进 Skill

## Scope

这是一个 action skill。
它聚焦"事项推动"，负责评估跟进事项状态、判断优先级、决定下一步动作、识别协同需求，并推动闭环。

与 `skill.action.accompany-corporate-client` 的边界：

- `accompany-corporate-client`：陪伴式跟进，核心是关系维护和触达节奏，输出侧重客户关系温度、待回应问题清单、下一次触达计划
- `client-followup-systematic`：主动式跟进，核心是事项闭环和动作推动，输出侧重事项状态评估、优先级排序、动作推动、风险信号

简单说：`accompany-corporate-client` 告诉你"怎么跟"，`client-followup-systematic` 告诉你"怎么推"。

## When To Use

- 拜访或沟通后，有待办事项需要推动
- 客户承诺的事项没有进展，需要评估状态
- 多个事项并行，需要判断优先级
- 事项遇到阻力，需要决定是继续推还是上提
- 需要把跟进结论结构化沉淀

## Required Reads

1. `references/item-assessment.md`
2. `references/priority-matrix.md`
3. `references/action-push-model.md`
4. `references/knowledge-routing.md`
5. `skill.reference.client-advance-framework`
6. `skill.reference.team-followup-framework`

## Execution Rule

1. 先用 `references/item-assessment.md` 评估每个事项的当前状态
2. 再用 `references/priority-matrix.md` 判断优先级和资源分配
3. 然后用 `references/action-push-model.md` 设计下一步推动动作
4. 需要补充公开知识时，按 `references/knowledge-routing.md` 调用对应 knowledge
5. 最后调用 `skill.reference.team-followup-framework` 组织协同闭环

## Input Contract

最低输入：

- 客户名称（可用代号，不含敏感信息）
- 事项清单（每个事项：承诺内容、承诺方、承诺时间、当前状态）
- 本次跟进目标

可选补充：

- 内部协同需求
- 历史跟进记录摘要

## Output Contract

必须包含：

1. **事项状态评估**：每个事项当前处于哪一阶段（待对方回应 / 进行中 / 遇阻 / 已闭环 / 已失效）
2. **优先级排序**：按紧迫度和影响度排列的事项处理顺序
3. **下一步动作**：针对每个未闭环事项的具体推动动作
4. **协同需求**：需要内部或外部配合的事项及配合方向
5. **风险信号**：事项搁置、时间窗口风险、需要上提的情况

禁止在输出中：

- 承诺具体完成时间
- 承诺授信、审批、费率结果
- 写入客户敏感信息
- 写内部审批流转细节

## Quality Gate

- 是否区分"在推"和"在等"
- 是否对每个未闭环事项给出明确下一步
- 是否标注时间窗口风险
- 是否判断哪些事项需要上提
- 是否避免承诺未核实的事实

## Boundary With Accompany Corporate Client

| 维度 | accompany-corporate-client | client-followup-systematic |
|------|---------------------------|---------------------------|
| 核心逻辑 | 陪伴式跟进，关系维护 | 主动式跟进，事项推动 |
| 输出重心 | 客户关系温度、触达计划 | 事项状态、优先级、动作 |
| 适用场景 | 会后关系经营、持续陪伴 | 事项跟踪、闭环推动 |
| 协同视角 | 内部协同配合关系推进 | 内部协同配合事项完成 |
| 风险维度 | 关系断点风险 | 时间窗口风险、搁置风险 |

两者可并行使用：`accompany-corporate-client` 管触达节奏，`client-followup-systematic` 管事项闭环。

## Script Hooks

- `scripts/validate-output.py`：校验结构完整性与承诺风险
