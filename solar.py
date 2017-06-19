#Alejandro Cuan-Martinez, CS1, 10/23/16
#This simulates the solar system by drawing the sun and a few planets
#I worked with Sean Hawkins and Lessley Hernandez where we discussed about the calulcation_acceleration function

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 10000000         # real seconds per simulation second
PIXELS_PER_METER = .5 / 1e9  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

AU = 1.49598e11
EM = 5.9736e24

def main():

    set_clear_color(0, 0, 0) # black background

    clear()

    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)


sun = Body(1.98892e30, 0, 0, 0, 0, 24, 1, .7, 0) # yellow sun
mercury = Body(.055 * EM, .3871 * AU, 0, 0, 48000, 4, .5, .5, .5)   # grey mercury
venus = Body(.81 * EM, .7233 * AU, 0, 0, 35000, 3, 1, .8, 0) #yello venus
earth = Body(EM, AU, 0, 0, 29790, 4, 0, 0, 1) #blue earth
mars = Body(.108 * EM, 1.524 * AU, 0, 0, 24140, 3, 1, .5, 0) #orange mars

solar_system = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE)