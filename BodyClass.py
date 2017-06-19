#Alejandro Cuan-Martinez, 10/23/16, CS1, This is the Body class which will simulate the earth and moon/ solar system


from cs1lib import *

class Body:

    #This is the constructor for the body class
    def __init__(self, mass, x, y , vx, vy, pixel_radius, r, g, b):
        self.body_mass = mass
        self.position_x = x
        self.position_y = y
        self.velocity_x = vx
        self.velocity_y = vy
        self.body_radius = pixel_radius
        self.red = r
        self.green = g
        self.blue = b

        #This will update the position according to the input of timestep and the velocity of the body
        #object
    def update_position(self, timestep):

        self.position_x = self.position_x + self.velocity_x * timestep
        self.position_y = self.position_y + self.velocity_y * timestep

        #This will update the velocity according to the input of timestep and the accelteration of the
        #body
    def update_veloctiy(self, ax, ay, timestep):
        self.velocity_x = self.velocity_x + timestep * ax
        self.velocity_y = self.velocity_y + timestep * ay

    #This is used to draw the body object
    def draw(self, cx, cy ,pixels_per_meter):
        set_fill_color(self.red, self.green, self.blue)
        draw_circle(cx + self.position_x * pixels_per_meter, cy + self.position_y * pixels_per_meter, self.body_radius)

    def get_mass(self):
        return self.body_mass


