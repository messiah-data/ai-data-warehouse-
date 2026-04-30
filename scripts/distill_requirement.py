#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
from ai_dw.requirement_distiller import distill_requirement


def main():
    if len(sys.argv) < 2:
        print("usage: python scripts/distill_requirement.py <requirement.md>")
        raise SystemExit(2)
    p = Path(sys.argv[1])
    result = distill_requirement(p.read_text(encoding="utf-8"), title=p.stem)
    print(yaml.safe_dump(result, allow_unicode=True, sort_keys=False))

if __name__ == "__main__":
    main()
