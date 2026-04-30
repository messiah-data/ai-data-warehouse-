# AGENTS.md

## 项目目标

本仓库存放 AI 大数据分析与 AI 数仓构建相关 Skills、业务知识、指标口径和辅助脚本。

## Codex 工作规则

- 保持 `SKILL.md` 简洁，把长内容放到 `references/`。
- 不要提交数据库密码、MCP token、生产环境连接串。
- 所有 SQL 默认只读。
- 查询分区表必须包含分区过滤条件，例如 `dt = ...` 或 `dt between ...`。
- 所有指标口径必须来自 `knowledge/metrics/`。
- 修改指标 YAML 后运行：`python scripts/validate_metric_registry.py knowledge/metrics`。
- 修改 SQL 审核逻辑后运行：`pytest`。

## 输出规范

分析报告必须包含：结论摘要、指标口径、查询 SQL、数据发现、可能原因、待验证问题、风险与限制。
