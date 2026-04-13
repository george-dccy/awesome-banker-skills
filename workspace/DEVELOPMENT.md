# DEVELOPMENT

## 项目北极星

这个项目要帮助银行人少踩坑、少重复劳动、少加班，让优秀经验可以被安装、传承和复用。

第一阶段不是做“大而全”的银行 AI 产品，而是先证明一件事：

`岗位方法论 + 流程打法 + 公开知识包` 可以组成一条真实可用的对公业务推进链路。

## 资产分层原则

### 1. roles 只写岗位方法论

- 写判断框架、沟通方式、推进节奏、常见失误
- 不写机构事实库
- 不复制 knowledge pack 内容

### 2. workflows 只写工作动作

- 写输入、动作、输出、检查点、失败场景
- 不写成岗位人格故事
- 不沉淀机构知识细节

### 3. knowledge-packs 只写公开知识

- 只收录公开、稳定、可引用、适合外部传播的内容
- 必须带 `sources.md`
- 优先官方来源，必要时补充公开二手来源

### 4. prompts 只是轻量入口

- 不新增独立知识
- 只是把 role、workflow 或 knowledge pack 变成可直接复制的 prompt
- prompt 必须指向目标 skill 或 pack

### 5. registry 是唯一机器索引

- 新增任何资产都要更新对应 registry
- registry 中的 path 必须是仓库内真实存在的路径
- 所有 id 使用英文 slug，不使用中文 id

### 6. workspace 是长期协作上下文

- 给未来切换模型或切换 Agent 的开发者用
- 记录“为什么这样设计”，而不是重复 README 文案

## 命名规则

- 目录名：英文 slug，小写，单词用 `-` 连接
- display name：中文
- skill `name`：必须等于父目录名
- pack id 建议格式：`pack.banks.<institution>.<pack-slug>`
- role id 建议格式：`role.<slug>`
- workflow id 建议格式：`workflow.<slug>`
- prompt id 建议格式：`prompt.<kind>.<slug>`

## 目录契约

```text
skills/<roles|workflows>/<slug>/SKILL.md
prompts/<roles|workflows|knowledge-packs>/<slug>.md
knowledge-packs/banks/<institution>/<pack-slug>/
registry/<skills|prompts|knowledge-packs>.json
workspace/<DEVELOPMENT|PROGRESS|AGENT_PROMPT>.md
```

## 内容红线

严禁写入以下内容：

- 真实客户数据
- 内部制度原文
- 内部审批口径
- 授信、定价、审批或受理结论
- 敏感参数、账号、证件号、合同号、发票号、流水

所有技能和知识包都要明确：

- 这是前期理解与准备辅助
- 不是正式业务受理入口
- 不是审批或授信结论输出器

## 第一阶段边界

第一阶段只做以下资产：

- `corp-relationship-manager`
- `report-to-leader`
- `market-corporate-client`
- `accompany-corporate-client`
- `banks/ceb/corporate-settlement/basic-settlement`
- `banks/ceb/transaction-banking/yangguang-e-pay`
- `banks/ceb/trade-finance/yangguang-electricity-certificate`

第一阶段不做：

- 前端 demo
- 安装脚本
- 包管理器
- 多银行并行扩张
- `branch-manager`

## 第二阶段优先 backlog

- `branch-manager`
- 更多银行或金融机构的公开知识包
- 蒸馏贡献流程自动化与模板增强
- registry 校验脚本
- 轻量安装辅助脚本
- README 英文版

## 专业目录约定

每个 skill 目录必须包含：

- `SKILL.md`
- `references/`
- `scripts/*.py`

知识关联必须同时体现在：

- `SKILL.md` 的 `metadata.related_packs`
- `references/knowledge-routing.md`
- `registry/skills.json` 的 `related_packs`

## 技能联动机制（必须执行）

每新增一个 role 或 workflow skill，至少完成以下联动：

1. 关联 1 个机构业务知识包（`knowledge-packs/banks/*`）
2. 关联 1 到 2 个通用能力包（`knowledge-packs/common/*`）
3. 在 `references/knowledge-routing.md` 写清楚关键词路由规则
4. 在 `scripts/build-context.py` 落地同样的路由逻辑
5. 在 `scripts/validate-output.py` 体现结构化输出要求

推荐联动顺序：

- 先机构业务包（事实底座）
- 再通用能力包（方法增强）
- 最后 workflow 输出结构（可执行建议）

### 新增 skill 标准流程（7 步）

1. 明确 skill 类型（`role` 或 `workflow`）与边界
2. 选择 1 个机构业务包（必须）+ 1 到 2 个通用能力包（必须）
3. 在 `SKILL.md` 的 `metadata.related_packs` 填入关联 id
4. 在 `references/knowledge-routing.md` 写清触发关键词、优先级和回退逻辑
5. 在 `scripts/build-context.py` 实现同样路由与上下文拼装
6. 在 `scripts/validate-output.py` 校验输出结构与合规边界
7. 同步更新 `registry/skills.json`、`README.md`、`workspace/PROGRESS.md`

### 新增 skill Definition of Done（DoD）

- `SKILL.md`、`references/`、`scripts/*.py` 完整存在
- 至少关联 2 类知识：机构业务包 + 通用能力包
- registry 记录可追溯到真实路径，且 id 关联一致
- 有最小可复用示例（输入示例 + 输出结构示例）
- 明确“不替代审批/授信/定价结论”的边界说明
- `workspace/PROGRESS.md` 的 `Now/Done` 已同步

## 通用能力包使用规范

当前通用能力包包含：

- `pack.common.banker-thinking.top-performer`
- `pack.common.economics.business-basics`
- `pack.common.sales.consultative-b2b`
- `pack.common.psychology.business-communication`

使用原则：

- 不把通用能力写成空泛鸡汤
- 必须落到具体业务动作与沟通场景
- 先给业务判断，再补能力解释，不反客为主

## 内容深度标准（持续补充）

后续补充知识内容时，每个包至少持续增强这三类内容：

1. 场景深度：覆盖更细分的银行业务场景与边界
2. 方法深度：给出可执行的判断框架、问题清单、动作模板
3. 反例深度：补充常见误区、失败模式与修正建议

写作标准：

- 专业但易懂，适合银行一线使用
- 有结构、有步骤、有边界
- 不造概念，不堆术语

## 开发质量要求

- 先读 `README.md` 与 `workspace/*`
- 新增内容时保持“方法论”和“公开知识”分离
- 每次改动同步更新 `registry/`、`README.md`、`workspace/PROGRESS.md`
- 如果引用公开知识，必须把来源放进对应 pack 的 `sources.md`

## 持续专业化迭代节奏

- 每次新增或改造 skill，至少补充 1 条“银行真实场景”案例
- 每周优先补强一个薄弱模块：业务理解、沟通推进、风险边界三选一
- 每月做一次“通用能力包 -> 技能输出质量”回看，淘汰空泛表述
