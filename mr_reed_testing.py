# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.

import pygame
from pygame.locals import *
from Asset_Reader import Asset_Reader
from End_Screen import End_Screen
from Start_Screen import Start_Screen

# constants
WIDTH = 1280
HEIGHT = 1024
FPS = 30

# global variables
running = True
game_state = "start_screen"

# canvas
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()
# testing object creation
start_screen = Start_Screen("GO!!!", "assets/CapyBarda_Start_Screen.png", "CapyBarda", "Leaderboard", "Arial", 1, 0, 0)

# main game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False

    pygame.blit(start_screen[0], (start_screen[0].x, start_screen[0].y))
    pygame.display.update()

pygame.exit()
sys.exit()