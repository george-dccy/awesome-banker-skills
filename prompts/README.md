# Prompts Usage

## 推荐入口

当前仓库优先推荐豆包专项入口：

- `prompts/entrypoints/doubao/public-consulting.md`
- `prompts/entrypoints/doubao/bank-staff.md`
- `prompts/entrypoints/doubao/frontline-manager.md`
- `prompts/entrypoints/doubao/head-office-leadership.md`
- `prompts/entrypoints/doubao/auto.md`

这些入口会要求模型：

1. 先读取 `registry/*.json`
2. 回答前先列出准备读取的文件路径
3. 先识别场景，再选择对应 workflow
4. 由 workflow 调用 methods 和 knowledge packs
5. 显式说明调用了哪些 `workflow skills / methods / knowledge packs`
6. 把“方法/判断依据”和“公开知识依据”分层表达
7. 在覆盖不足时明确写出“当前仓库未覆盖”

推荐路由层级：

`scene -> workflow -> method -> knowledge pack`

这里的 `workflow skill` 应理解为 scene-specific playbook，也就是场景化编排资产；`method` 则是被 workflow 调用的可复用框架。

## 兼容入口

以下入口仍然保留，适合已有使用习惯：

- `prompts/entrypoints/ceb-customer-consulting.md`
- `prompts/entrypoints/auto.md`

## 专项 Prompt

当你明确只做某一类任务时，再使用：

- `prompts/roles/*`
- `prompts/workflows/*`
- `prompts/knowledge-packs/*`
