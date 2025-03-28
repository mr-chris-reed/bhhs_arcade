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
hell_background = Background("assets/hell_background.png", 1, 0, 0, 1.0, 100, 100, 1080, 820, 300, 300, 100, 100, 100, 100, 100, 100, False, False)
forest_path_background = Background("assets/forest_path_background.png", 1, 0, 0, 1.0, 100, 100, 1080, 820, 300, 300, 100, 100, 100, 100, 100, 100, False, False)
castle_background = Background("assets/castle_background.png", 1, 0, 0, 1.0, 100, 100, 1080, 820, 300, 300, 100 ,100, 100, 100, 100, 100, False, False)
capybarda = Player(
    200, 200,
    "assets/CapybardaRun_back.png", "assets/CapybardaRun_front.png", "assets/CapybardaRun_Side2.png", "assets/CapybardaRun_side.png", "assets/CapybardaIdle_front.png", "assets/CapybardaIdle_back.png",
    "assets/CapybardaIdle_back.png", "assets/CapybardaIdle_front.png", "assets/CapybardaIdle_side2.png", "assets/CapybardaIdle_side.png",
    6, 4, 4, 6, 4, 4, 4, 4, 4, 4,
    0.5, 0.5, 0.5, 0.5, 0.5,
    10, 10
)

backgrounds = [forest_path_background, hell_background, castle_background]
current_background = forest_path_background

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
    
    if game_start == True:

        if (joysticks[0].get_axis(0) > 0.5):
            capybarda.up(counter)
        if (joysticks[0].get_axis(0) < -0.5):
            capybarda.down(counter)
        if (joysticks[0].get_axis(1) > 0.5):
            capybarda.right(counter)
        if (joysticks[0].get_axis(1) < -0.5):
            capybarda.left(counter)

        Background.change_next_flag(backgrounds, capybarda.x_coord, capybarda.y_coord)
        Background.change_prev_flag(backgrounds, capybarda.x_coord, capybarda.y_coord)

        print(str(Background.background_index))
        CANVAS.blit(backgrounds[Background.background_index].generate_background_surface(backgrounds, WIDTH, HEIGHT), (0, 0))
        CANVAS.blit(capybarda.last_sprite, (capybarda.x_coord, capybarda.y_coord))


    #if game_start == True:
        
        ### implement blitting of the Background.py class here
    
    if game_start == False:
        current_background = start_screen.generate_return_surface(counter)
        CANVAS.blit(current_background, (0, 0))

    if counter >= 600:
        counter = 0
    else: counter += 1
    # end of start screen implementation

    pygame.display.flip()
    clock.tick(FPS)
