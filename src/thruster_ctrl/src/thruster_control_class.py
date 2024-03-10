#!/usr/bin/python3

class ThrusterControl:
    def __init__(self):
        self.thruster_1 = 0
        self.thruster_2 = 0
        self.thruster_3 = 0
        self.thruster_4 = 0
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

    def set_pwm(self, surge, sway, yaw):

        # Setting PWM duty cycles for surge movement
        if surge != 0 and sway == 0 and yaw == 0:
            if surge > 0:
                self.thruster_3 = self.thruster_4 = (0.128*(surge*50))+1
            elif surge < 0:
                self.thruster_1 = self.thruster_2 = (0.128*(surge*50))+1

        # Setting PWM duty cycles for sway movement
        elif sway != 0 and surge == 0 and yaw == 0:
            if sway > 0:
                self.thruster_2 = self.thruster_4 = (0.128*(sway*50))+1
            elif sway < 0:
                self.thruster_1 = self.thruster_3 = (0.128*(sway*50))+1

        # Setting PWM duty cycles for yaw movement
        elif yaw != 0 and surge == 0 and sway == 0:
            if yaw > 0:
                self.thruster_2 = self.thruster_3 = (0.128*(yaw*50))+1
            elif yaw < 0:
                self.thruster_1 = self.thruster_4 = (0.128*(yaw*50))+1

        else:
            self.thruster_1 = self.thruster_2 = self.thruster_3 = self.thruster_4 = 0

        self.pwmsignals["A"] = self.thruster_1
        self.pwmsignals["B"] = self.thruster_2
        self.pwmsignals["C"] = self.thruster_3
        self.pwmsignals["D"] = self.thruster_4
    
        return self.pwmsignals