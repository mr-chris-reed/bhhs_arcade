# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.

import pygame
from Asset_Reader import Asset_Reader
from Start_Screen import Start_Screen

# constants
WIDTH = 1106
HEIGHT = 1021
FPS = 30

# global variables
running = True
game_state = "start_screen"

# canvas
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()

#test for objects

Start_Screen = Start_Screen(1, 2, 3, 4, 5,)

# main game loop
while running:
    pass