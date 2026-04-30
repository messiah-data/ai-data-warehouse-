#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
from ai_dw.model_generator import generate_model_spec


def main():
    if len(sys.argv) < 2:
        print("usage: python scripts/generate_model_spec.py <requirement.md>")
        raise SystemExit(2)
    p = Path(sys.argv[1])
    result = generate_model_spec(p.read_text(encoding="utf-8"))
    print(yaml.safe_dump(result, allow_unicode=True, sort_keys=False))

if __name__ == "__main__":
    main()
