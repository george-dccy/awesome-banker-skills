# DEVELOPMENT

## 项目定位

这个项目是面向银行人、聊天模型和 Agent 的 repo-first 能力底座。

目标不是做银行客服，而是公开沉淀：

- 银行岗位共识技能
- 银行业务可公开知识
- 可复用的方法框架

同时天然支持每个用户在本地继续生长自己的 private overlay。

## 当前阶段重点

### 1. 明确 public / private overlay

- public base：公开仓库中的 `skills`、`knowledge-packs`、`methods`、`prompts`、`registry`
- private overlay：`workspace/private/*`
- 公共更新不覆盖 private
- private 内容可整理为公共贡献候选

### 2. 建立 methods 层

- 经营方法论
- 管理方法论
- 沟通 / 汇报方法论
- 其他可复用方法论

### 3. 建立豆包优先入口

至少支持：

- 豆包公开咨询入口
- 豆包银行员工入口
- 豆包基层管理者入口
- 豆包总行领导层入口
- 豆包自动路由入口

### 4. 建立维护型蒸馏协作能力

新增 `distill-and-contribute` workflow skill，用于：

- 从公开材料提炼 asset
- 自动判断该放哪一层
- 先生成到 private，再由用户决定是否公开
- 从已有资产做增量更新

## 内容边界

- 不放真实客户数据
- 不放内部制度原文
- 不放内部审批、授信、定价、时效承诺
- 不要求用户提供真实敏感信息

## 当前版本不做

- 前端
- 行内内网接口实现
- 自动无审查覆写
- 大规模多银行同步扩张
