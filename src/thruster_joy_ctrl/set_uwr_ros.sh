#!/bin/bash

#$
catkin_make
source devel/setup.bash

# Set the ROS_MASTER_URI to the IP of Master-Device (UWR-RPi)
export ROS_MASTER_URI=http://192.168.254.151:11311/
export ROS_IP=192.168.254.151

echo "ROS_MASTER_URI set to $ROS_MASTER_URI"
echo "ROS_IP set $ROS_IP"

rosrun thruster_joy_ctrl thruster_joy_ctrl.py
