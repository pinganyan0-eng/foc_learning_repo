#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_SRC="$(cd -- "$SCRIPT_DIR/.." && pwd)"
DEFAULT_DEST="$HOME/Documents/Codex/qiansai"
DEST_ROOT="${1:-$DEFAULT_DEST}"
DEST_REPO="$DEST_ROOT/foc_learning_repo"

if [[ ! -f "$PROJECT_SRC/CURRENT_STATUS.md" || ! -f "$PROJECT_SRC/AGENTS.md" ]]; then
  echo "This script must stay inside foc_learning_repo/tools."
  exit 1
fi

mkdir -p "$DEST_ROOT"

if [[ -e "$DEST_REPO" ]]; then
  echo "Destination already exists: $DEST_REPO"
  echo "Move or rename it first, then run this script again."
  exit 1
fi

echo "Creating the Mac project copy at: $DEST_REPO"
rsync -a \
  --exclude '__pycache__/' \
  --exclude '.pytest_cache/' \
  --exclude '.mypy_cache/' \
  --exclude '.venv/' \
  --exclude 'venv/' \
  --exclude 'node_modules/' \
  "$PROJECT_SRC/" "$DEST_REPO/"

if command -v python3 >/dev/null 2>&1; then
  echo "Rebuilding local search index..."
  (cd "$DEST_REPO" && python3 tools/build_vector_store.py)

  echo "Running repository tests..."
  (cd "$DEST_REPO" && python3 -m unittest discover -s tests)
else
  echo "python3 was not found. Install Python 3, then run from the project:"
  echo "  python3 tools/build_vector_store.py"
  echo "  python3 -m unittest discover -s tests"
fi

echo
echo "Done."
echo "Open this folder in Codex on the Mac:"
echo "  $DEST_REPO"
echo
echo "For normal two-computer use, sync project changes through Git after this first setup."
