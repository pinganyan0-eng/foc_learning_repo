#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
SKIP_PULL=0
SKIP_TESTS=0

for arg in "$@"; do
  case "$arg" in
    --skip-pull) SKIP_PULL=1 ;;
    --skip-tests) SKIP_TESTS=1 ;;
    *)
      echo "Usage: bash tools/start_learning_session.sh [--skip-pull] [--skip-tests]" >&2
      exit 1
      ;;
  esac
done

py() {
  if command -v python3 >/dev/null 2>&1; then
    python3 "$@"
  else
    python "$@"
  fi
}

echo "FOC learning session start"
echo "Repository: $REPO_ROOT"
echo

if [[ "$SKIP_PULL" -eq 0 ]]; then
  if [[ -n "$(git -C "$REPO_ROOT" status --porcelain)" ]]; then
    echo "Working tree has local changes; skipping pull to avoid mixing edits."
  else
    git -C "$REPO_ROOT" pull --ff-only
  fi
else
  echo "Skipping pull."
fi

if [[ -f "$REPO_ROOT/tools/install_project_skill.sh" ]]; then
  echo "Installing repo-managed project skill..."
  bash "$REPO_ROOT/tools/install_project_skill.sh"
fi

(cd "$REPO_ROOT" && py tools/normalize_learning_loop.py)

if [[ "$SKIP_TESTS" -eq 0 ]]; then
  (cd "$REPO_ROOT" && py -m unittest discover -s tests)
fi

echo
echo "Current status anchors:"
grep -A 5 -E '^## 当前阶段|^## 下一步最小动作|^## 安全红线' "$REPO_ROOT/CURRENT_STATUS.md" || true

echo
echo "Next review items:"
grep -E '^\| next learning turn \|' "$REPO_ROOT/learning/review_queue.md" | head -n 5 || true

echo
echo "Safety reminder: no 24V, power board, motor, PWM gate checks, or STDRIVE101 protection changes without the phase-gate evidence."
git -C "$REPO_ROOT" status --short --branch
