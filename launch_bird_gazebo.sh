#!/usr/bin/env bash
set -e

cd /home/bird_deterrent_system/ros2_ws
set +u
source /opt/ros/humble/setup.bash
set -u
export GAZEBO_MODEL_PATH="${GAZEBO_MODEL_PATH:-}:$(pwd)/models"

pkill -f 'gzserver' >/dev/null 2>&1 || true
pkill -f 'gazebo' >/dev/null 2>&1 || true

exec gazebo worlds/bird_deterrent_field.world
