#Alejandro Cuan-Martinez, 10/19/16, CS1, This is the System Class and will utilize the Body class

from math import sqrt
from body import *
class System:

    #This is the constructor of the System class and uses a list this input by the user
    def __init__(self, body_list):
        self.body_list = body_list

    #This computes the acceleration of the entire system by going through the entire list and computing accleration
    #together
    def compute_acceleration(self, n):
        G = 6.6738e-11
        for i in range (0, len(self.body_list)):
            if n != self.body_list[i]:
                body_mass = self.body_list[i].get_mass()
                dx = self.body_list[i].position_x - n.position_x
                dy = self.body_list[i].position_y - n.position_y
                r = sqrt((dx * dx) + (dy * dy))
                a = (G * body_mass) / (r * r)
                ax = (a * dx) / r
                ay = (a * dy) / r
                return ax, ay

    # This updates the body's input into the list that was defined in the constructor based on the
    #update_position and update_velocity functions in the Body class
    def update(self, timestep):

        for i in range (0,len(self.body_list)):
            (ax, ay) = self.compute_acceleration(self.body_list[i])
            self.body_list[i].update_veloctiy(ax, ay, timestep)
            self.body_list[i].update_position(timestep)




    #This draws the entire system that will draw the bodies
    def draw(self, cx, cy, pixels_per_meter):
        for i in range(0, len(self.body_list)):
            self.body_list[i].draw(cx,cy,pixels_per_meter)









