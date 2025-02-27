# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.

import pygame
from Asset_Reader import Asset_Reader

# constants
WIDTH = 1106
HEIGHT = 1021
FPS = 30

# global variables
running = True

# canvas
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()

# main game loop
while running:
    pass