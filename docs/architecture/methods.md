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

- `skills/roles`：这个岗位通常先看什么、先判断什么、先避开什么
- `skills/workflows`：场景化编排层，也可以理解为 scene-specific playbook
- `knowledge-packs`：公开事实是什么
- `methods`：遇到这类问题时，用什么框架处理

## 与 workflow skill 的新边界

- `workflow skill`：场景化编排层，负责识别输入、组织步骤、调用 `methods`、路由 `knowledge-packs`
- `method`：可复用框架层，负责提供判断、推进、复盘、汇报的通用框架

可以用下面的三问法判断内容应该放哪里：

1. 脱离当前场景是否还能复用
2. 这是在讲“怎么思考/判断/推进”，还是在讲“这次任务怎么组织”
3. 换一个岗位或流程后是否仍然自然

更具体地说：

- 应优先放进 `workflow skill` 的，是某个场景的最低输入、编排顺序、输出契约、边界约束
- 应优先放进 `method` 的，是跨多个 workflow 仍可复用的判断框架、推进方法、复盘方法、汇报框架

推荐路由层级是：

`scene -> workflow -> method -> knowledge pack`

`methods` 不是：

- 岗位人格
- workflow 场景编排的替代品
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

- 先识别场景，再进入 workflow，再调用方法框架
- methods 默认是增强层，不应喧宾夺主
- 任何 method 都应附带银行场景示例，避免空泛
