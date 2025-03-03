# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.

import pygame
from pygame.locals import *
from Asset_Reader import Asset_Reader
from End_Screen import End_Screen
from Start_Screen import Start_Screen
from Player import Player

# constants
WIDTH = 1280
HEIGHT = 1024
FPS = 30

# global variables
running = True


# canvas
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()
# testing object creation
Capybarda = Player(50,50, )

# main game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
