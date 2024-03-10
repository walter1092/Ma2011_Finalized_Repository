# Teleop Keyboard Motion Control

This package is to control the movement of the UWR remotely through a notebook or similar, ssh connected to a raspberry pi in the UWR, with keyboard commands with ROS noetic. It is designed to execute single surge, sway and yaw 2D-Movements with the UWR for positioning reasons in a Pool. Two packages are used for this motion control. The ROS BCD-licensed telelop_twist_keyboard package and the self developed thruster_keyb_ctrl package.

![Alt text](rqt_graph.png)

## Prerequisites
- [Ubuntu 20.04](https://releases.ubuntu.com/focal/)
- [ROS Noetic](https://wiki.ros.org/noetic/Installation) (It is recommended to install "desktop-full" version)
- [Git](https://github.com/git-guides/install-git) with SSH key
- [Visual Studio Code](https://code.visualstudio.com/download) (optional)

## Getting started
In order to run the thruster keyboard control the teleop_twist_keyboard package and the 2023_UWR respo have to installed/cloned.

### teleop_twist_keyboard
Installation:
- sudo apt-get install ros-noetic-teleop-twist-keyboard

Teleop_twist_keyboard is a on ROS Wiki published and BSD-licensed generic keyboard teleop package. It reads keyboard inputs and publishes them in twist_msg format to the /cmd_vel topic. The default values for linear and angular velocity are 1 and 0.5. If necessary custom values can be defined in the rosrun command to start the node. For further information about the code of the package, please consult the [ROS-Wiki-teleop_twist_keyboard](https://wiki.ros.org/action/fullsearch/teleop_twist_keyboard?action=fullsearch&context=180&value=linkto%3A%22teleop_twist_keyboard%22).

### thruster_keyb_ctrl

Installation:
- Thruster_keyb_ctrl is part of the 2023_UWR respo. Download this repo with:
    git clone git@github.com:SAAB-NTU/2023_UWR.git

Thruster_keyb_ctrl is a ROS package, which translates twist_msgs into pwm signals to control the UWR thruster for 2D-movement of surge, sway and yaw. When the Thruster_keyb_ctrl.py is run the serial port is opened and configured. The PWM transceiver has the following parameters:
- Bauderate: 9600
- Bytesize: 8
- Stopbits: 1
- CRC: None

The thruster_control_class sets all bit values to be sent of the eight thrusters to zero, the pwm duty cycle of 75%, for no movement when instantiated. This class receives the twist_msgs in the callback function through the arguments surge, sway and yaw and the self.set_pwm function transforms them into bits who are returned through self.pwmsignals in the format: 
```
{"A": self.thruster_1, "B": self.thruster_2, "C": self.thruster_3, "D": self.thruster_4, "E": 0, "F": 0, "G": 0, "H": 0, "R": 0}
```
This dictionary is  transformed into JSON format and send to the pwm transceiver board through the serial port by the send_pwm function. The formula which calculates the pwm duty cycle is shown in the picture below.

![Alt text](pwm_dutycycle_formula.png)

The listener function initializes the node "thruster_keyb_ctrl" and subscribes to the /cmd_vel topic through the callback function and keeps running until the node is shut down.

## Usage
1. Open a terminal in Ubuntu
2. Run in terminal:
 ```
 roscore
 cd 2023_UWR/ros_ws
 source devel/setup.bash
 roslaunch thruster_keyb_ctrl thruster_keyb_ctrl.launch
 ```
5. If the node are connected successfully the second terminal output is:
```
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit

currently:	speed 0.5	turn 1.0 
```
6. Keyboard inputs in second terminal for motion control:
- Surge (i or ,)
- Sway (J or L)
- Yaw (j or l)
- Increase velocity 't'
- Decrease velocity 'b'
- STOP movement 'k' or any other unassigned key
- Aboard program, disconnect node and stop movement 'Ctrl+C'
Note: The movements can just be executed individually. All other keys which have no velocity assigned end up in a stop of the UWR.

7. If your are finished with the motion control input 'Ctrl+C' in the terminal and the nodes and master are closed.