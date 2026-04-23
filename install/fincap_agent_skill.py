#!/usr/bin/env python3
"""Install the Financial Capability Kit resolver skill into local agent skill dirs."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


TARGET_DIRS = {
    "claude": Path.home() / ".claude" / "skills" / "financial-capability-kit",
    "codex": Path.home() / ".codex" / "skills" / "financial-capability-kit",
    "agents": Path.home() / ".agents" / "skills" / "financial-capability-kit",
}


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def selected_targets(target: str) -> list[tuple[str, Path]]:
    if target == "all":
        return list(TARGET_DIRS.items())
    return [(target, TARGET_DIRS[target])]


def copy_skill(source: Path, destination: Path, repo_path: Path, dry_run: bool) -> None:
    if not (source / "SKILL.md").exists():
        raise FileNotFoundError(f"找不到源 skill：{source}")

    if dry_run:
        print(f"[dry-run] 安装 {source} -> {destination}")
        print(f"[dry-run] 写入 repository-path.txt = {repo_path}")
        return

    destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)
    (destination / "repository-path.txt").write_text(str(repo_path), encoding="utf-8")
    print(f"已安装 Financial Capability Kit resolver skill -> {destination}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="安装 Fincap 常驻 resolver skill。")
    parser.add_argument(
        "--target",
        choices=["claude", "codex", "agents", "all"],
        default="all",
        help="安装目标。默认 all。",
    )
    parser.add_argument(
        "--repo-path",
        default=None,
        help="Financial Capability Kit 仓库路径。默认自动使用当前脚本所在仓库。",
    )
    parser.add_argument("--dry-run", action="store_true", help="只展示将执行的安装动作。")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repo_path = Path(args.repo_path).expanduser().resolve() if args.repo_path else repo_root_from_script()
    source = repo_path / "agent-skills" / "financial-capability-kit"

    try:
        for _, destination in selected_targets(args.target):
            copy_skill(source, destination, repo_path, args.dry_run)
    except Exception as exc:
        print(f"安装失败：{exc}", file=sys.stderr)
        return 1

    if not args.dry_run:
        print("")
        print("请重启或新开一个 Agent session，让 skill 索引重新加载。")
        print("之后在银行/金融工作上下文中，Fincap resolver skill 应能自动触发。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
