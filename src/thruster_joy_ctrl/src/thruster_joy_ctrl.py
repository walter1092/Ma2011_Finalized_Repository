#!/usr/bin/python3

import rospy
import json
import serial
import time
from sensor_msgs.msg import Joy
from joy_control_class import JoyControl

serial_port = input("Enter serial port (Default is /dev/ttyUSB0): ") or "/dev/ttyUSB0"
ser = serial.Serial(serial_port, baudrate=9600, bytesize=8, stopbits=1, write_timeout=0.1)

joy_ctrl = JoyControl()

# Transform PWM-Signal in for PWM-Transceiver readable JSON format.
def send_pwm():

    json_pwmsignals = json.dumps(joy_ctrl.pwmsignals)
    try:
        ser.write(json_pwmsignals.encode('utf-8'))
        return print(f"""PWM sent successfully""")
    
    except serial.SerialException as e:
        print(f"Failed to send PWM signal due to signal error: {e}")
    except TypeError as e:
        print(f"Failed to encode PWM signals to JSON due to type error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def callback (sensor_msgs):

    #extracting states from msg
    sensor_data = {
        'surge': sensor_msgs.axes[1],
        'sway': sensor_msgs.axes[0],
        'yaw': sensor_msgs.axes[3],
        'rb_btn': sensor_msgs.buttons[5],
        'dpad_btn_vert': sensor_msgs.axes[7],
        'view_btn': sensor_msgs.buttons[6]
    }

    joy_ctrl.adjust_vel(sensor_data['dpad_btn_vert'])
    joy_ctrl.set_pwm(sensor_data)

    send_pwm()

    rospy.loginfo(f"""{time.asctime()}
                 {joy_ctrl.pwmsignals}""")
    
    # Check for shutdown condition
    if sensor_data["view_btn"] == 1:
        rospy.signal_shutdown("View Button is pressed. Nodes are now shut down")
    
def listener():
    rospy.init_node("thruster_joy_ctrl")
    rospy.Subscriber("/joy", Joy, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        rospy.loginfo(f"")
        listener()
        # Set all thrusters to no movement and reset the thrusters
        ser.write(json.dumps({"A": 0, "B": 0, "C": 0,"D": 0,"E": 0,"F": 0,"G": 0,"H": 0,"R": 1}))
        ser.close()

    except rospy.ROSInterruptException:
        pass
