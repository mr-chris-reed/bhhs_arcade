# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.

import pygame
from pygame.locals import *
from Asset_Reader import Asset_Reader
# from End_Screen import End_Screen
from Start_Screen import Start_Screen
from Background import Background

# initialize pygame and pygame joystick
pygame.init()
pygame.joystick.init()

# creating the clock
clock = pygame.time.Clock()

# constants
WIDTH = 1280
HEIGHT = 1024
FPS = 30

# global variables
temp_screen = None
running = True
game_start = False
joysticks = []
counter = 0
leaderboard = [['CMC', "7.5"], ['CWJ', "7.8"], ['TGP', "8.1"]]

# canvas
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
#CANVAS = pygame.display.set_mode((0, 0), FULLSCREEN)

# object creation
start_screen = Start_Screen("assets/start_screen.png", leaderboard, 1, 0, 0, HEIGHT, WIDTH)
#background = Background("assets/forest_path_background.png", 1, 0, 0, 1.0, 100, 100, 1080, 820, 700, 500, 100, 100, 100, 100, 100, 100, False, False)

# main game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False

    # start screen implementation
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)

    
    for joystick in joysticks:
        if joysticks[0].get_button(11):
            game_start = True

    #if game_start == True:
        
        ### implement blitting of the Background.py class here
    
    if game_start == False:
        temp_screen = start_screen.generate_return_surface(counter)
        CANVAS.blit(temp_screen, (0, 0))

    if counter >= 600:
        counter = 0
    else: counter += 1
    # end of start screen implementation

    pygame.display.flip()
    clock.tick(FPS)
