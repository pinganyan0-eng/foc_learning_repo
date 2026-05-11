#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
TOPIC=""
SUMMARY=""
WEAK=""
NEXT=""
EVIDENCE="L1"
CONFIDENCE="medium"
DUE="next learning turn"
SKIP_VECTOR_STORE=0
SKIP_TESTS=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --topic) TOPIC="${2:-}"; shift 2 ;;
    --summary) SUMMARY="${2:-}"; shift 2 ;;
    --weak) WEAK="${2:-}"; shift 2 ;;
    --next) NEXT="${2:-}"; shift 2 ;;
    --evidence) EVIDENCE="${2:-L1}"; shift 2 ;;
    --confidence) CONFIDENCE="${2:-medium}"; shift 2 ;;
    --due) DUE="${2:-next learning turn}"; shift 2 ;;
    --skip-vector-store) SKIP_VECTOR_STORE=1; shift ;;
    --skip-tests) SKIP_TESTS=1; shift ;;
    *)
      echo "Unknown argument: $1" >&2
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

echo "FOC learning session end"
echo "Repository: $REPO_ROOT"

if [[ -n "$TOPIC" && -n "$SUMMARY" ]]; then
  args=(tools/record_learning_session.py --topic "$TOPIC" --summary "$SUMMARY" --evidence "$EVIDENCE" --confidence "$CONFIDENCE")
  if [[ -n "$WEAK" ]]; then
    args+=(--weak "$WEAK")
  fi
  if [[ -n "$NEXT" ]]; then
    args+=(--next "$NEXT" --due "$DUE")
  fi
  (cd "$REPO_ROOT" && py "${args[@]}")
else
  echo "No learning note recorded. To record one, pass --topic and --summary."
fi

(cd "$REPO_ROOT" && py tools/normalize_learning_loop.py)

if [[ "$SKIP_VECTOR_STORE" -eq 0 ]]; then
  (cd "$REPO_ROOT" && py tools/build_vector_store.py)
fi

if [[ "$SKIP_TESTS" -eq 0 ]]; then
  (cd "$REPO_ROOT" && py -m unittest discover -s tests)
fi

echo
echo "Open review items:"
grep -E '\| open \|' "$REPO_ROOT/learning/review_queue.md" | head -n 8 || true

echo
git -C "$REPO_ROOT" status --short --branch
