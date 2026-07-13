# 长期记忆

## 用户
- 姓名：贾若，称呼"老贾"
- 城市：北京
- 核心项目：my-llm-wiki（个人知识库）
- 之前用 Claude Code 维护知识库，2026-07-12 起由知微接替

## 知识库约定
- 所有操作遵循 CLAUDE.md 契约（INGEST 12 步 / QUERY 4 步 / REFLECT 4 阶段 / LINT 9 项 / MERGE）
- raw/ 只读不写；wiki/ 完全读写；pre-commit 门禁钩子已挂载
- Wikilink 必须英文小写连字符；中文名走 aliases
- MERGE 必须等老贾确认，不得自动合并
- INGEST 收尾必须跑 lint --gate 自检 + 更新 index/overview/log

## 偏好
- 老贾偏好务实、不废话的交流风格
- 对知识库质量敏感（SHA 完整性、断链、置信度标注）

## 多助手并行维护
- 其他电脑上的 Claude Code 也在维护本知识库
- CLAUDE.md 已加入"多助手并行维护约定"（6 条），两边共同遵守
- 知微这边的关键实践：开始工作前 git pull + 扫 log.md，完成后及时 push
