#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p build qa/skills
if python3 -B scripts/skill_tools/latex_compile.py main.tex --compiler xelatex --outdir build >qa/skills/compile.txt 2>&1; then
  cp build/main.pdf main.pdf
  echo 'Compiled main.pdf through the supplied LaTeX skill runner (shell escape disabled).'
else
  result=$?
  tail -50 qa/skills/compile.txt >&2
  exit "$result"
fi
