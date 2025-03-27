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
FPS = 60


# global variables
running = True
game_state = "start_screen"

# canvas
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()
pygame.joystick.init()
joysticks = []
# testing object creation
end_screen = End_Screen(1,1,1,1,1,1,"assets/gameover.png")


# main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
            print("joy")
        if event.type == QUIT: 
            running = False
    end_screen.drawEndScreen(CANVAS, joysticks)
