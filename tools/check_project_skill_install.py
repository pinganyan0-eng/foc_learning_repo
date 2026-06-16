from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILL_NAME = "stm32g474-foc-assistant"
IGNORED_PARTS = {"__pycache__"}
IGNORED_SUFFIXES = {".pyc", ".pyo"}


@dataclass(frozen=True)
class FileDigest:
    relative_path: str
    sha256: str
    size: int


def normalize_path(path: Path) -> str:
    return path.as_posix()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def should_include(path: Path) -> bool:
    if any(part in IGNORED_PARTS for part in path.parts):
        return False
    if path.suffix.lower() in IGNORED_SUFFIXES:
        return False
    return path.is_file()


def build_manifest(root: Path) -> dict[str, FileDigest]:
    manifest: dict[str, FileDigest] = {}
    for path in sorted(root.rglob("*")):
        if not should_include(path):
            continue
        relative = normalize_path(path.relative_to(root))
        manifest[relative] = FileDigest(
            relative_path=relative,
            sha256=sha256_file(path),
            size=path.stat().st_size,
        )
    return manifest


def default_installed_path(skill_name: str) -> Path:
    return Path.home() / ".codex" / "skills" / skill_name


def manifest_to_json(manifest: dict[str, FileDigest]) -> list[dict[str, object]]:
    return [
        {"path": item.relative_path, "sha256": item.sha256, "size": item.size}
        for item in manifest.values()
    ]


def compare_manifests(
    repo_manifest: dict[str, FileDigest],
    installed_manifest: dict[str, FileDigest],
) -> tuple[list[str], list[str], list[str]]:
    repo_paths = set(repo_manifest)
    installed_paths = set(installed_manifest)
    missing = sorted(repo_paths - installed_paths)
    extra = sorted(installed_paths - repo_paths)
    changed = sorted(
        path
        for path in repo_paths & installed_paths
        if repo_manifest[path].sha256 != installed_manifest[path].sha256
        or repo_manifest[path].size != installed_manifest[path].size
    )
    return missing, extra, changed


def check_skill(
    *,
    skill_name: str,
    installed_path: Path | None,
    repo_only: bool,
) -> dict[str, object]:
    repo_path = ROOT / "codex_skills" / skill_name
    errors: list[str] = []

    if not repo_path.is_dir():
        errors.append(f"Repo-local project Skill directory is missing: {repo_path}")
        repo_manifest: dict[str, FileDigest] = {}
    else:
        repo_manifest = build_manifest(repo_path)

    for required in (
        "SKILL.md",
        "agents/openai.yaml",
        "references/project-navigation.md",
        "references/no-power-boundary.md",
        "references/learning-feedback.md",
        "references/workflow-maintenance.md",
    ):
        if required not in repo_manifest:
            errors.append(f"Repo-local project Skill missing required file: {required}")

    report: dict[str, object] = {
        "ok": not errors,
        "mode": "repo_only" if repo_only else "installed_compare",
        "skill_name": skill_name,
        "repo_path": str(repo_path),
        "installed_path": str(installed_path or default_installed_path(skill_name)),
        "repo_files": manifest_to_json(repo_manifest),
        "missing_installed_files": [],
        "extra_installed_files": [],
        "changed_installed_files": [],
        "errors": errors,
    }

    if repo_only:
        return report

    target = installed_path or default_installed_path(skill_name)
    if not target.is_dir():
        errors.append(f"Installed project Skill directory is missing: {target}")
        report["ok"] = False
        return report

    installed_manifest = build_manifest(target)
    missing, extra, changed = compare_manifests(repo_manifest, installed_manifest)
    errors.extend(f"Installed project Skill missing file: {path}" for path in missing)
    errors.extend(f"Installed project Skill has extra file: {path}" for path in extra)
    errors.extend(f"Installed project Skill differs from repo source: {path}" for path in changed)

    report["missing_installed_files"] = missing
    report["extra_installed_files"] = extra
    report["changed_installed_files"] = changed
    report["installed_files"] = manifest_to_json(installed_manifest)
    report["ok"] = not errors
    return report


def print_text_report(report: dict[str, object]) -> None:
    if report["ok"]:
        if report["mode"] == "repo_only":
            print("project Skill source check: ok")
        else:
            print("project Skill install drift check: ok")
        print(f"skill: {report['skill_name']}")
        print(f"repo: {report['repo_path']}")
        print(f"installed: {report['installed_path']}")
        print(f"repo files: {len(report['repo_files'])}")
        if "installed_files" in report:
            print(f"installed files: {len(report['installed_files'])}")
        return

    print("project Skill install drift check: failed")
    for error in report["errors"]:
        print(f"- {error}")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Check repo-local project Skill source and optional installed Skill drift."
    )
    parser.add_argument("--skill-name", default=DEFAULT_SKILL_NAME)
    parser.add_argument("--installed-path", type=Path)
    parser.add_argument(
        "--repo-only",
        action="store_true",
        help="Validate only the repo-local Skill source; do not inspect ~/.codex/skills.",
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    report = check_skill(
        skill_name=args.skill_name,
        installed_path=args.installed_path,
        repo_only=args.repo_only,
    )

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_text_report(report)

    if not report["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
