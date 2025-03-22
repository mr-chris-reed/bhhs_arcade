# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.

import pygame
from pygame.locals import *
from Asset_Reader import Asset_Reader
#from End_Screen import End_Screen
from Start_Screen import Start_Screen

# constants
WIDTH = 1280
HEIGHT = 1024
FPS = 30

# global variables
running = True

# canvas
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))

# initialize pygame and pygame joystick
pygame.init()
pygame.joystick.init()

# testing object creation
start_screen = Start_Screen(
    "assets/capy_start_screen_NEW.png",
    [],
    1,
    0,
    0,
    HEIGHT,
    WIDTH,
)

# main game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
