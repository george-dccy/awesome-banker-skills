# Prompts Usage

## 主入口

当前仓库优先推荐豆包专项入口：

- `prompts/entrypoints/doubao/public-consulting.md`
- `prompts/entrypoints/doubao/bank-staff.md`
- `prompts/entrypoints/doubao/frontline-manager.md`
- `prompts/entrypoints/doubao/head-office-leadership.md`
- `prompts/entrypoints/doubao/auto.md`
- `prompts/entrypoints/agent/general.md`

这些入口已经统一使用以下仓库地址：

`https://gitee.com/georgedccy/awesome-banker-skills.git`

共同约定：

1. 先识别身份、岗位和问题场景
2. 优先直接给结论、判断或可执行结果
3. 必要时再补充岗位经验判断和公开依据
4. 覆盖不足时明确写出“当前仓库未覆盖”

推荐读取顺序：

`scene -> workflow -> method -> knowledge pack`

如果身份明确，也可以同时读取对应 `role skill`。

其中：

- 豆包/千问等聊天模型入口，重点是“先给专业结果，再补依据”
- Agent 入口，重点是“把仓库当长期工作底座，遇到类似问题优先复用已有资产，并把个人经验沉淀成 private 技能/记忆，再整理公开贡献候选”

## 专项 Prompt

当你明确只做某一类任务时，再使用更短的专项 prompt：

- `prompts/roles/*`
- `prompts/workflows/*`
- `prompts/knowledge-packs/*`
