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


# Transform PWM-Signal in for PWM-Transceiver readable JSON format.
def send_pwm():

    json_pwmsignals = json.dumps(thruster_ctrl.pwmsignals)
    try:
        ser.write(json_pwmsignals.encode('utf-8'))
        return print(f"""PWM sent successfully""")
    
    except serial.SerialException as e:
        print(f"Failed to send PWM signal due to signal error: {e}")
    except TypeError as e:
        print(f"Failed to encode PWM signals to JSON due to type error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Subscribes to /cmd_vel topic and safes the velocity values in arguments surge,
# sway and yaw and transforms and send them to the PWM transceiver.
def callback(twist_msg):
    # Extracting relevant fields from the message
    surge = twist_msg.linear.x
    sway = twist_msg.linear.y
    yaw = twist_msg.angular.z

    thruster_ctrl.set_pwm(surge, sway, yaw)

    # Send the pwm signal in JSON format
    send_pwm()

    # Log the duty cycle values
    rospy.loginfo(f"""{time.asctime()}
                   {thruster_ctrl.pwmsignals}""")


# Main function to initialize node and subscribe until it is shut down. 
def listener():

    rospy.init_node("thruster_keyb_ctrl")

    rospy.Subscriber("/cmd_vel", Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        rospy.loginfo(f"")
        listener()
        # Set all thrusters to no movement and reset the thrusters
        ser.write(json.dumps({"A": 0, "B": 0, "C": 0,"D": 0,"E": 0,"F": 0,"G": 0,"H": 0,"R": 1}))
        ser.close

    except rospy.ROSInterruptException:
        pass


