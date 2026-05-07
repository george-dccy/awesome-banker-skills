---
name: skill.action.branch-operating-diagnosis
description: Use when you need to collect branch or frontline operating goals and key figures through dialogue, then generate a structured operating diagnosis with highlights, shortfalls, initial causes, and missing data.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: analyze
  display_name_zh: 经营分析
  audience: [bank-practitioner, manager]
  support_files:
    - README.md
    - input-contract.md
    - workflow.md
    - output-template.md
    - checkpoints.md
    - related-assets.md
  related_skills:
    - skill.reference.branch-operating-diagnosis-lens
    - skill.action.operating-recommendation-brief
    - skill.action.report-decision-brief
    - skill.reference.executive-briefing-decision-support
  related_prompts:
    - prompt.skill.action.branch-operating-diagnosis
---

# 经营分析 Skill

## Scope

这是一个 action skill。
它负责通过对话收集目标、关键经营数据和自我评价，然后输出一版轻量、结构化、可继续补数的经营分析结论。

## When To Use

- 需要快速判断分支行、网点或团队当前经营状态
- 手上只有 3-8 个关键指标，需要先给出一版经营分析
- 需要在正式汇报前先形成初判
- 需要先找亮点、短板和待补数项，再进入经营建议阶段

## Required Reads

1. `README.md`
2. `input-contract.md`
3. `workflow.md`
4. `output-template.md`
5. `checkpoints.md`
6. `related-assets.md`
7. `skill.reference.branch-operating-diagnosis-lens`

## Execution Rule

1. 先按 `input-contract.md` 收集最低输入
2. 如果关键对比口径缺失，先标记待补数，不假装完成判断
3. 按 `workflow.md` 先做结果判断，再做结构判断和初步归因
4. 输出必须使用固定结构，不写成散文式汇报
5. 明确哪些结论暂时只能初判、哪些必须人工复核

## Input Contract

最低输入：

- 当前阶段目标
- 3-8 个关键经营数据
- 至少一个对比维度（同比、环比、上期、目标、去年同期之一）
- 使用者自我评价或现场判断

可选补充：

- 客群结构
- 产品结构
- 区域结构
- 近期重大变化
- 已知约束

## Output Contract

必须包含：

1. **当前初判**
2. **做得好的地方**
3. **做得不好的地方**
4. **主要判断依据**
5. **初步归因**
6. **还需补充的信息**
7. **边界提示**

禁止在输出中：

- 冒充正式考核结论
- 编造口径不一致的数据解释
- 承诺内部经营动作已正确
- 写真实客户敏感信息

## Quality Gate

- 是否先看结果，再讲结构和原因
- 是否把亮点和短板拆开写
- 是否明确标出待补数项
- 是否避免把轻量经营分析写成内部经营例会纪要
