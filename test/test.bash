#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc 
timeout 10 ros2 run mypkg test_listener > /tmp/mypkg.log
cd $dir/ros2_ws/src/mypkg/mypkg/
timeout 10 python3 similality_images.py

cat /tmp/mypkg.log |
grep 'Received similarity data: array'
grep 'Received filenames'
