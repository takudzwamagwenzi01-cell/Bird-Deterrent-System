#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

export PYTHONPATH="$SCRIPT_DIR/install/bird_deterrent/lib/python3.10/site-packages${PYTHONPATH:+:$PYTHONPATH}"
export LD_LIBRARY_PATH="$SCRIPT_DIR/install/bird_deterrent/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export AMENT_PREFIX_PATH="$SCRIPT_DIR/install/bird_deterrent${AMENT_PREFIX_PATH:+:$AMENT_PREFIX_PATH}"
export ROS_PACKAGE_PATH="$SCRIPT_DIR/src${ROS_PACKAGE_PATH:+:$ROS_PACKAGE_PATH}"

exec python3 "$SCRIPT_DIR/install/bird_deterrent/bin/bird_motion_node"
