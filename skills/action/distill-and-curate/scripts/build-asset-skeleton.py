#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


TEMPLATES = {
    "reference-skill": ["SKILL.md", "skill.json", "references/", "scripts/"],
    "action-skill": ["SKILL.md", "references/", "scripts/"],
    "knowledge": ["README.md", "pack.json", "faq.md", "sources.md", "modules/"],
}


def build_path(kind: str, slug: str, mode: str, category: str, institution: str) -> str:
    prefix = Path("workspace/private") if mode == "private-first" else Path(".")

    if kind == "reference-skill":
        return str(prefix / "skills" / "reference" / slug)
    if kind == "action-skill":
        return str(prefix / "skills" / "action" / slug)
    if kind == "knowledge":
        base = prefix / "knowledge"
        if institution:
            return str(base / "banks" / institution / category / slug)
        return str(base / "common" / category / slug)
    raise ValueError(f"Unsupported kind: {kind}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a recommended asset skeleton.")
    parser.add_argument("--kind", required=True, choices=["reference-skill", "action-skill", "knowledge"])
    parser.add_argument("--slug", required=True)
    parser.add_argument("--mode", default="private-first", choices=["private-first", "public-candidate"])
    parser.add_argument("--category", default="reusable")
    parser.add_argument("--institution", default="")
    parser.add_argument("--create", action="store_true")
    args = parser.parse_args()

    path = Path(build_path(args.kind, args.slug, args.mode, args.category, args.institution))
    files = TEMPLATES[args.kind]

    if args.create:
        path.mkdir(parents=True, exist_ok=True)
        for entry in files:
            target = path / entry
            if entry.endswith("/"):
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.touch(exist_ok=True)

    print(
        json.dumps(
            {
                "kind": args.kind,
                "mode": args.mode,
                "path": path.as_posix(),
                "files": files,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
