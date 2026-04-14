# Methods 层说明

## 为什么单独引入 methods

如果没有 `methods` 层，很多高价值内容会出现两种坏结果：

- 被硬塞进 `skills`，导致岗位 skill 过厚、过泛
- 被写进 `knowledge-packs`，把经验框架伪装成事实知识

因此，`methods` 单独作为一层存在。

## 定义

`methods` 是跨岗位、跨流程、跨银行复用的判断与推进框架。

它回答的问题是：

- 怎么拆解
- 怎么判断
- 怎么推进
- 怎么复盘
- 怎么汇报
- 怎么组织团队动作

## 与其他层的边界

- `skills`：谁来做、通常怎么做
- `knowledge-packs`：公开事实是什么
- `methods`：遇到这类问题时，用什么框架处理

`methods` 不是：

- 岗位人格
- 工作流清单的替代品
- 事实知识库

## 目录结构

```text
methods/
├─ business-operations/
├─ management/
├─ communication-reporting/
└─ reusable/
```

## 单个 method 的最小契约

```text
methods/<category>/<slug>/
├─ README.md
├─ method.json
├─ frameworks.md
├─ examples.md
├─ anti-patterns.md
└─ related-assets.md
```

第一版至少应包含：

- `README.md`
- `method.json`
- `frameworks.md`
- `examples.md`

## 推荐首批 methods

- `problem-opportunity-scan`
- `client-advance-map`
- `leader-decision-brief`
- `team-followup-loop`

## 使用原则

- 先给业务判断，再给方法框架
- methods 默认是增强层，不应喧宾夺主
- 任何 method 都应附带银行场景示例，避免空泛
