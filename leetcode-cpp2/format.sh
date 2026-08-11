#!/usr/bin/env bash
# Format all .cpp files inside _* folders using clang-format

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

files=$(find "$SCRIPT_DIR" -path "$SCRIPT_DIR/_*/*.cpp" -type f)

if [[ -z "$files" ]]; then
    echo "No .cpp files found in _* folders."
    exit 0
fi

count=$(echo "$files" | wc -l | tr -d ' ')
echo "Formatting $count .cpp files..."

echo "$files" | xargs clang-format -i

echo "Done."
