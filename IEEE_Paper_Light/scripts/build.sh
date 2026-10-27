#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p build
for executable in xelatex bibtex; do
  command -v "$executable" >/dev/null || { echo "Missing required program: $executable" >&2; exit 1; }
done
run_logged() {
  local log_path="$1"
  shift
  if "$@" >"$log_path" 2>&1; then
    return 0
  else
    local command_status=$?
    cat "$log_path" >&2
    return "$command_status"
  fi
}
run_logged build/main-pass1.console.txt xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
run_logged build/bibtex.console.txt bibtex build/main
for pass in 2 3; do
  run_logged "build/main-pass${pass}.console.txt" xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
done
for pass in 1 2; do
  run_logged "build/supplement-pass${pass}.console.txt" xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build supplement.tex
done
cp build/main.pdf main.pdf
cp build/supplement.pdf supplement.pdf
echo 'Compiled main.pdf and supplement.pdf. Logs are in build/.'
