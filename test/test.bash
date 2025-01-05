#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc 
cd $dir/ros2_ws/src/mypkg/mypkg/
python3 test_listener.py > /tmp/mypkg.log
python3 similality_images.py

grep 'Received similarity data' /tmp/mypkg.log
grep 'Received filenames' /tmp/mypkg.log

# cat /tmp/mypkg.log |
# grep 'Received similarity data'
# cat /tmp/mypkg.log |
# grep 'Received filenames'
