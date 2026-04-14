# Public / Private Overlay

## 目标

让公开仓库持续更新，同时不破坏本地私有资产。

## 读取顺序

Agent 统一按以下顺序读取：

1. `registry/skills.json`
2. `registry/knowledge-packs.json`
3. `registry/methods.json`
4. `registry/prompts.json`
5. 如果存在，再读取：
   - `workspace/private/registry/skills.json`
   - `workspace/private/registry/knowledge-packs.json`
   - `workspace/private/registry/methods.json`
   - `workspace/private/registry/prompts.json`
6. 合并索引后，再按路由读取具体正文

## 合并规则

- 新 id：直接追加
- 同 id：private 元数据优先
- 正文路径：如果 private 覆盖存在，优先读取 private path
- 增量扩展：可使用 `extends` 或 `base_id` 指向 public base

目标是补丁式增强，不是整包重写。

## 自进化规则

任何“学到的新偏好、新案例、新经验”都要先走 private：

1. 先写入 `workspace/private/memories/` 或 patch proposal
2. 给用户看候选变更摘要
3. 经用户确认后，再更新 private 资产
4. 如用户愿意公开，再整理成 public contribution candidate

严禁无审查自动覆写 public 资产。

## public contribution 流程

推荐走三段式：

1. `private draft`
2. `public candidate`
3. `merge to public`

整理为公开候选时，至少要完成：

- 去敏感化
- 明确边界
- 补齐来源
- 生成变更摘要

## 对未来行内落地的意义

这个 overlay 结构为后续银行内网落地预留了清晰扩展点：

- public registry 可替换为行内 registry
- private overlay 可映射为个人或部门工作区
- repo-first prompt 逻辑可以延续到行内 Agent
- 当前版本先只保留结构，不实现具体内网接口
