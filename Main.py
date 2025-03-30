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
from Player import Player

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
current_background = None
running = True
game_start = False
joysticks = []
counter = 0
leaderboard = [['CMC', "7.5"], ['CWJ', "7.8"], ['TGP', "8.1"]]

# canvas
CANVAS = pygame.display.set_mode((0, 0), FULLSCREEN)

# object creation
start_screen = Start_Screen("assets/start_screen.png", leaderboard, 1, 0, 0, HEIGHT, WIDTH)
forest_path = Background("assets/forest_path_background.png", 1, 1, 0, 0, 50, WIDTH - 50, 50, HEIGHT - 50)
capybarda = Player(
    200, 200,
    "assets/CapybardaRun_back.png", "assets/CapybardaRun_front.png", "assets/CapybardaRun_Side2.png", "assets/CapybardaRun_side.png", "assets/CapybardaIdle_front.png", "assets/CapybardaIdle_back.png",
    "assets/CapybardaIdle_back.png", "assets/CapybardaIdle_front.png", "assets/CapybardaIdle_side2.png", "assets/CapybardaIdle_side.png",
    6, 4, 4, 6, 4, 4, 4, 4, 4, 4,
    0.75, 0.75, 0.75, 0.75, 0.75,
    10, 10
)

backgrounds = [forest_path]
current_background = start_screen

# main game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False

    # start screen implementation
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)

    if joysticks[0].get_button(11):
        game_start = True
    
    if not(game_start):
        current_background = start_screen
        CANVAS.blit(current_background.generate_return_surface(counter), (0, 0))
    elif game_start:
        current_background = backgrounds[Background.background_index]
        CANVAS.blit(current_background.generate_return_surface(), (0, 0))
        if joysticks[0].get_axis(0) > 0.50:
            print(joysticks[0].get_axis(0))
            capybarda.up(counter)
        CANVAS.blit(capybarda.last_idle_sprite, (400, 400))

    if counter >= 600:
        counter = 0
    else: counter += 1
    # end of start screen implementation

    pygame.display.flip()
    clock.tick(FPS)
