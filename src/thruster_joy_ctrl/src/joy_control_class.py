#!/usr/bin/python3

class JoyControl:

    def __init__(self):
        self.thruster_1 = 0
        self.thruster_2 = 0
        self.thruster_3 = 0
        self.thruster_4 = 0
        self.vel_ctrl = 1
        self.pwmsignals = {
                    "A": self.thruster_1,
                    "B": self.thruster_2,
                    "C": self.thruster_3,
                    "D": self.thruster_4,
                    "E": 0,
                    "F": 0,
                    "G": 0,
                    "H": 0,
                    "R": 0}


    # Sets the maximum for increase of the velocity to factor 10, which is the PWM duty cycle of 100%
    def adjust_vel(self, value):
        if value > 0:
           self.vel_ctrl += 1
        elif value < 0:
            self.vel_ctrl -= 1
        self.vel_ctrl = max(1, min(self.vel_ctrl, 10))
        return self.vel_ctrl

    # This function sets the bits for the PWM duty cycles that are sent to the PWM transceiver
    # via the serial port.
    def set_pwm(self, msgs):
    
        if msgs['rb_btn'] != 0:
            if abs(msgs['surge']) > abs(msgs['sway']) and msgs['yaw'] == 0:
                if msgs['surge'] > 0:
                    self.thruster_1 = self.thruster_2 = 0
                    self.thruster_3 = self.thruster_4 = int((6.4*abs(msgs['surge'])*self.vel_ctrl)+1)
                elif msgs['surge'] < 0:
                    self.thruster_1 = self.thruster_2 = int((6.4*abs(msgs['surge'])*self.vel_ctrl)+1)
                    self.thruster_3 = self.thruster_4 = 0

            elif abs(msgs['sway']) > abs(msgs['surge']) and msgs['yaw'] == 0:
                if msgs['sway'] > 0:
                    self.thruster_1 = self.thruster_3 = int((6.4*abs(msgs['sway'])*self.vel_ctrl)+1)
                    self.thruster_2 = self.thruster_4 = 0
                elif msgs['sway'] < 0:
                    self.thruster_1 = self.thruster_3 = 0
                    self.thruster_2 = self.thruster_4 = int((6.4*abs(msgs['sway'])*self.vel_ctrl)+1)
        
            elif abs(msgs['yaw']) !=0:
                if msgs['yaw'] > 0:
                    self.thruster_1 = self.thruster_4 = int((6.4*abs(msgs['yaw'])*self.vel_ctrl)+1)
                    self.thruster_2 = self.thruster_3 = 0
                elif msgs['yaw'] < 0:
                    self.thruster_1 = self.thruster_4 = 0
                    self.thruster_2 = self.thruster_3 = int((6.4*abs(msgs['yaw'])*self.vel_ctrl)+1)       
        else:
            self.thruster_1 = self.thruster_2 = self.thruster_3 = self.thruster_4 = 0

        self.pwmsignals["A"] = self.thruster_1
        self.pwmsignals["B"] = self.thruster_2
        self.pwmsignals["C"] = self.thruster_3
        self.pwmsignals["D"] = self.thruster_4
    
        return self.pwmsignals