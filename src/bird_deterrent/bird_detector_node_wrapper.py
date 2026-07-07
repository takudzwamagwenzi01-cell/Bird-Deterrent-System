#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PREFIX="$(cd "$SCRIPT_DIR/../../.." >/dev/null 2>&1 && pwd)"
exec "$PREFIX/bin/bird_detector_node" "$@"
