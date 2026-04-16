---
name: client-advance-framework
description: Use when you need a reusable framework to turn a client conversation into explicit next steps, owners, and timing.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: execute
  display_name_zh: 客户推进框架
  audience: [finance-learner, bank-practitioner]
  support_files:
    - README.md
    - frameworks.md
    - examples.md
    - anti-patterns.md
    - related-assets.md
---

# 客户推进框架 Skill

## Scope

这是一个 reference skill。
它负责把“聊过了”变成“下一步谁做什么、什么时候做、怎样算往前走”。

## When To Use

- 需要把一次沟通推进成明确动作
- 害怕事情停在“保持联系”
- 需要设计责任人、时间点和检查点

## Required Reads

1. `README.md`
2. `frameworks.md`
3. `examples.md`
4. `anti-patterns.md`
5. `related-assets.md`

## Core Output Rule

每次至少明确：

1. 这一步的目标
2. 谁负责
3. 何时推进
4. 如何判断是否真的往前走

## Not For

- 替代 action skill 的场景编排
- 只做概念解释不做推进设计
