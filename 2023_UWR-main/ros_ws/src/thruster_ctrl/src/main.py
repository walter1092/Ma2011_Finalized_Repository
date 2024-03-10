#!/usr/bin/python3

import rospy
import json
import serial
import time
from geometry_msgs.msg import Twist
from thruster_control_class import ThrusterControl

serial_port = input("Enter serial port (Default is /dev/ttyUSB0): ") or "/dev/ttyUSB0"
ser = serial.Serial(serial_port, baudrate=9600, bytesize=8, stopbits=1, write_timeout=0.1)

# Instantiate class ThrusterControl
thruster_ctrl = ThrusterControl()


# Transform PWM-Signal in for PWM-Transceiver usabale data and send it in JSON format
def send_pwm():

    json_pwmsignals = json.dumps(thruster_ctrl.pwmsignals)
    try:
        ser.write(json_pwmsignals.encode('utf-8'))
        return print(f"""PWM sent succsessfully: \n
                 {thruster_ctrl.pwmsignals}""")
    
    except serial.SerialException as e:
        print(f"Failed to send PWM signal due to signal error: {e}")
    except TypeError as e:
        print(f"Failed to encode PWM signals to JSON due to type error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def callback(twist_msg):
    # Extracting relevant fields from the message
    surge = twist_msg.linear.x
    sway = twist_msg.linear.y
    yaw = twist_msg.angular.z

    thruster_ctrl.set_pwm(surge, sway, yaw)

    # Send the pwm signal in JSON format
    send_pwm()

    # Log the duty cycle values
    rospy.loginfo(f"""Thruster 1: {thruster_ctrl.thruster_1}, Thruster 2: {thruster_ctrl.thruster_2},
                  Thruster 3: {thruster_ctrl.thruster_3}, Thruster 4: {thruster_ctrl.thruster_4}""")


# Main function to initialize node and subscriber
def listener():

    rospy.init_node("thruster_keyb_ctrl")

    rospy.Subscriber("/cmd_vel", Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        rospy.loginfo(f"{time.asctime()}")
        listener()
        ser.write(json.dumps({"R": 1}))
        ser.close

    except rospy.ROSInterruptException:
        pass


