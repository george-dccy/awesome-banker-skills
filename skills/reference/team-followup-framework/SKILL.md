---
name: team-followup-framework
description: Use when you need a reusable framework to manage owners, checkpoints, signals, and retrospectives across multiple people.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: execute
  display_name_zh: 团队跟进框架
  audience: [finance-learner, bank-practitioner, manager]
  support_files:
    - README.md
    - frameworks.md
    - examples.md
    - anti-patterns.md
    - related-assets.md
---

# 团队跟进框架 Skill

## Scope

这是一个 reference skill。
它帮助你把多人协同事项拆清楚、盯住信号、形成复盘闭环。

## When To Use

- 需要多人协同推进事项
- 需要避免“大家都知道但没人负责”
- 需要形成固定检查点和复盘节奏

## Required Reads

1. `README.md`
2. `frameworks.md`
3. `examples.md`
4. `anti-patterns.md`
5. `related-assets.md`

## Core Output Rule

每个重点事项至少应有：

- 事项名称
- 负责人
- 截止时间
- 当前状态
- 卡点
- 下次检查点

## Not For

- 替代客户场景 action skill
- 只做口头表态，不形成可跟踪板
