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

1. 先读取 `registry/*.json` 或 `registry/knowledge-packs.json`
2. 先按问题类型去读对应正文，再形成回答
3. 这套仓库约束适用于整个对话，不只第一轮
4. 默认优先使用仓库，不要拿外部搜索替代仓库
5. 对用户呈现时，优先直接给结论、判断或可执行结果
6. 每个入口末尾都保留问题占位，方便直接复制使用
7. 覆盖不足时明确写出“当前仓库未覆盖”

推荐读取顺序：

`scene -> workflow -> method -> knowledge pack`

如果身份明确，也可以同时读取对应 `role skill`。

其中：

- 豆包/千问等聊天模型入口，重点是“多轮持续用仓库，外部自然表达”
- Agent 入口，重点是“整场会话持续以仓库为底座，先解题，再沉淀资产”

## 专项 Prompt

当你明确只做某一类任务时，再使用更短的专项 prompt：

- `prompts/roles/*`
- `prompts/workflows/*`
- `prompts/knowledge-packs/*`
