#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-check}"
MESSAGE="${2:-}"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

run_tests() {
  if command -v python3 >/dev/null 2>&1; then
    (cd "$REPO_ROOT" && python3 -m unittest discover -s tests)
  else
    (cd "$REPO_ROOT" && python -m unittest discover -s tests)
  fi
}

install_project_skill() {
  local installer="$REPO_ROOT/tools/install_project_skill.sh"
  if [[ -f "$installer" ]]; then
    echo "Installing repo-managed project skill..."
    bash "$installer"
  fi
}

echo "Repository: $REPO_ROOT"
git -C "$REPO_ROOT" status --short --branch

case "$MODE" in
  check)
    echo
    echo "Remote:"
    git -C "$REPO_ROOT" remote -v
    run_tests
    ;;

  pull)
    if [[ -n "$(git -C "$REPO_ROOT" status --porcelain)" ]]; then
      echo "Working tree has local changes. Commit or stash them before pulling." >&2
      exit 1
    fi
    git -C "$REPO_ROOT" pull --ff-only
    install_project_skill
    run_tests
    ;;

  push)
    if [[ -z "$MESSAGE" ]]; then
      echo "Push mode requires a commit message:" >&2
      echo "  bash tools/sync_project.sh push \"update project state\"" >&2
      exit 1
    fi
    run_tests
    git -C "$REPO_ROOT" add -A
    if [[ -z "$(git -C "$REPO_ROOT" diff --cached --name-only)" ]]; then
      echo "No staged changes to commit."
      git -C "$REPO_ROOT" pull --ff-only
      exit 0
    fi
    git -C "$REPO_ROOT" commit -m "$MESSAGE"
    git -C "$REPO_ROOT" pull --rebase --autostash
    git -C "$REPO_ROOT" push
    git -C "$REPO_ROOT" status --short --branch
    ;;

  *)
    echo "Usage:" >&2
    echo "  bash tools/sync_project.sh check" >&2
    echo "  bash tools/sync_project.sh pull" >&2
    echo "  bash tools/sync_project.sh push \"commit message\"" >&2
    exit 1
    ;;
esac
