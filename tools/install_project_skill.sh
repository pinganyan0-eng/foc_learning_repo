#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="${1:-stm32g474-foc-assistant}"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
SOURCE="$REPO_ROOT/codex_skills/$SKILL_NAME"
TARGET_ROOT="$HOME/.codex/skills"
TARGET="$TARGET_ROOT/$SKILL_NAME"

if [[ ! -f "$SOURCE/SKILL.md" ]]; then
  echo "Project skill source not found: $SOURCE" >&2
  exit 1
fi

mkdir -p "$TARGET_ROOT"
rm -rf "$TARGET"
rsync -a "$SOURCE/" "$TARGET/"

echo "Installed $SKILL_NAME to $TARGET"
echo "Restart Codex if the updated skill does not appear immediately."
