#!/bin/bash
# SPDX-FileCopyrightText: 2025 Kai Nonaka
# SPDX-License-Identifier: BSD-3-Clause:

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc 
cd $dir/ros2_ws/src/mypkg/mypkg/
timeout 20 python3 test_listener.py > /tmp/mypkg.log &
timeout 20 python3 similality_images.py

cat /tmp/mypkg.log
echo "Log content:"
