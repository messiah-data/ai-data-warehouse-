#!/usr/bin/env python3
from pathlib import Path
import sys
from rich.console import Console
from ai_dw.metric_registry import MetricRegistry

console = Console()


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("knowledge/metrics")
    registry = MetricRegistry.from_path(path)
    errors = registry.validate()
    if errors:
        console.print("[red]metric registry validation failed[/red]")
        for e in errors:
            console.print(f"- {e}")
        raise SystemExit(1)
    console.print(f"[green]ok[/green] loaded {len(registry.metrics)} metrics")

if __name__ == "__main__":
    main()
