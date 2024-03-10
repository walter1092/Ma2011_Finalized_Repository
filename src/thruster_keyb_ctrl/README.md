# Teleop Keyboard Motion Control

This package is designed to control the movement of the UWR remotely from a notebook or similar, ssh connected to a raspberry pi in the UWR, using keyboard commands with ROS noetic. It is designed to perform simple pitch, roll or yaw 2D movements with the UWR for positioning purposes in a pool. Two packages are used for this motion control. The ROS BCD licensed telelop_twist_keyboard package and the self developed thruster_keyb_ctrl package.

![Alt text](png/rqt_graph.png)

## Prerequisites

- [Ubuntu 20.04](https://releases.ubuntu.com/focal/)
- [ROS Noetic](https://wiki.ros.org/noetic/Installation) (It is recommended to install "desktop-full" version)
- [Git](https://github.com/git-guides/install-git) with SSH key
- [Visual Studio Code](https://code.visualstudio.com/download) (optional) 

## Getting started

In order to run the thruster keyboard control, the teleop_twist_keyboard package and the 2023_UWR repo must be installed/cloned.

### UWR

The UWR has eight different thrusters to control movement. Thrusters 1-4 are used for movements in the X-Y plane and thrusters 5-8 for movements in the X-Z and Y-Z planes. For the purposes of this package, only the 2D movements carried out by thrusters 1-4 are relevant. The rest of the thrusters are set to no motion.  The figure below shows the arrangement of the thrusters, including their orientation (clockwise or counterclockwise) and 2D motion information.

![Alt text](png/uwr_thruster_layout.png)

### teleop_twist_keyboard

Installation:
```
sudo apt-get install ros-noetic-teleop-twist-keyboard
```

Teleop_twist_keyboard is a on ROS Wiki published and BSD-licensed generic keyboard teleop package. It reads keyboard inputs and publishes them in twist_msg format to the /cmd_vel topic. The default values for linear and angular velocity are 1 and 0.5. If necessary custom values can be defined in the rosrun command to start the node. For further information about the code of the package, please consult the [ROS-Wiki-teleop_twist_keyboard](https://wiki.ros.org/action/fullsearch/teleop_twist_keyboard?action=fullsearch&context=180&value=linkto%3A%22teleop_twist_keyboard%22).

### thruster_keyb_ctrl

Installation:
- Thruster_keyb_ctrl is part of the 2023_UWR respo. Download this repo with:
```
git clone git@github.com:SAAB-NTU/2023_UWR.git
```
Thruster_keyb_ctrl is a ROS package that translates twist_msgs into pwm signals to control the UWR thruster for 2D motion of pitch, roll and yaw. Running Thruster_keyb_ctrl.py opens and configures the serial port. The PWM transceiver has the following parameters:
- Bauderate: 9600
- Bytesize: 8
- Stopbits: 1
- CRC: None

The thruster_control_class, when instantiated, sets all bit values to be sent from the eight thrusters to zero, the pwm duty cycle of 75%, for no motion. This class receives the twist_msgs in the callback function via the surge, sway and yaw arguments and the self.set_pwm function converts them into bits which are returned via self.pwmsignals in the format:
```
{"A": self.thruster_1, "B": self.thruster_2, "C": self.thruster_3, "D": self.thruster_4, "E": 0, "F": 0, "G": 0, "H": 0, "R": 0}
```
This dictionary is converted to JSON format and sent to the pwm transceiver board via the serial port using the send_pwm function. Keys 'E' to 'F' control thrusters 5-8 to no motion. The formula used to calculate the PWM duty cycle is shown in the figure below.
```
$$
\text{PWM Duty Cycle} = \left( \frac{191 + \text{value}}{256} \right) \times 100\%
$$
```
The formula used in the code to calculate the bits for the duty cycle change is derived from the formula below. It is set up in such a way that the value x transferred by the controller causes a 2.5% increase in the duty cycle. The Teleop node allows the velocity to increase/decrease by a factor of 0.1.
```
$$
\frac{1500}{2000} \times 100\% + x \times 2.5\% = \frac{(191 + y)}{256} \times 100\%
$$

$$
y = 6.4 \times x + 1
$$
```

The listener function initializes the node "thruster_keyb_ctrl" and subscribes to the /cmd_vel topic through the callback function and keeps running until the node is shut down.

## Usage

1. Open a terminal in Ubuntu
2. SSH from notebook into the UWR-Raspberry Pi
 ```
 ssh user@rpi-ip
 ```
3. Change directory to the ROS workspace
4. Run in SSH terminal:
 ```
 rm -r devel # Just run during the first time setting up. Deletes devel folder in rs_ws because of device specific symbolic links.
 rm -r build # Just run during the first time setting up. Deletes build folder in rs_ws because of device specific symbolic links.
 catkin_make
 source devel/setup.bash
 export ROS_MASTER_URI=http://rpi-ip:11311/
 export ROS_IP=rpi-ip

 ```
5. Open a new ssh terminal and run:
```
roscore
 ```
6. Run in the other ssh  terminal:
 ```
 rosrun thruster_keyb_ctrl thruster_keyb_ctrl.py
 ```
7. Open a new terminal on the notebook change directory to the ROS workspace and run:
 ```
 rm -r devel # Just run during the first time setting up. Deletes devel folder in rs_ws because of device specific symbolic links.
 rm -r build # Just run during the first time setting up. Deletes build folder in rs_ws because of device specific symbolic links.
 catkin_make
 source devel/setup.bash
 export ROS_MASTER_URI=http://rpi-ip:11311/
 export ROS_IP=notebookip
 rosrun teleop_twist_keyboard teleop_twist_keyboard.py
 ```
8. If the node are connected successfully the ssh terminal output is:
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
9. Keyboard inputs in SSH terminal for motion control:
- Surge (i or ,)
- Sway (J or L)
- Yaw (j or l)
- Increase velocity 't'
- Decrease velocity 'b'
- STOP movement 'k' or any other unassigned key
- Aboard program, disconnect node and stop movement 'Ctrl+C'
Note: The movements can just be executed individually. All other keys which have no velocity assigned end up in a stop of the UWR.

10. If your are finished with the motion control input 'Ctrl+C' in the terminals and the nodes are closed.
