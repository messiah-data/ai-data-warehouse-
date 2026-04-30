from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


class StarRocksMcpTransport(Protocol):
    def call_tool(self, name: str, arguments: dict[str, Any]) -> Any: ...


@dataclass
class StarRocksMcpClient:
    """Thin wrapper around a StarRocks MCP transport supplied by the runtime."""

    transport: StarRocksMcpTransport

    def list_databases(self) -> Any:
        return self.transport.call_tool("list_databases", {})

    def list_tables(self, database: str) -> Any:
        return self.transport.call_tool("list_tables", {"database": database})

    def describe_table(self, database: str, table: str) -> Any:
        return self.transport.call_tool("describe_table", {"database": database, "table": table})

    def execute_readonly(self, sql: str) -> Any:
        return self.transport.call_tool("read_query", {"sql": sql})
