# AI Data Warehouse Skills

面向大数据开发的数据分析与 AI 数仓构建仓库模板，可直接上传到 GitHub 后继续用 Codex 维护。

## 核心能力

- 从需求文档蒸馏业务知识
- 管理指标口径与业务语义
- 通过 StarRocks MCP 生成、审核并执行只读查询
- 输出趋势、归因、漏斗、留存等分析报告
- 根据需求生成 ODS/DWD/DWS/ADS 模型设计
- 生成 StarRocks 建表 SQL、ETL SQL、数据质量规则和验收 SQL

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
python scripts/validate_metric_registry.py knowledge/metrics
python scripts/review_sql.py examples/sql/bad_query.sql
python scripts/distill_requirement.py examples/requirements/member_growth.md
python scripts/generate_model_spec.py examples/requirements/member_growth.md
```

## 目录说明

```text
skills/                 ChatGPT Skills
knowledge/              业务域、指标、表、示例知识库
src/ai_dw/              Python 工具代码
scripts/                命令行脚本入口
tests/                  pytest 测试
examples/               示例需求与分析用例
```

## StarRocks MCP 使用方式

本仓库不保存数据库账号。实际使用时，请在 ChatGPT / Codex / MCP 客户端中配置 StarRocks MCP Server，并暴露 list databases、list tables、describe table、read_query 等能力。

默认策略：只允许 SELECT/WITH/SHOW/DESCRIBE/EXPLAIN。生产库 DDL/DML 必须人工确认。
