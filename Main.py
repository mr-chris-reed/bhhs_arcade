# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.

import pygame
from pygame.locals import *
from Asset_Reader import Asset_Reader
from Start_Screen import Start_Screen
from Background import Background
from Player import Player
from End_Screen import End_Screen

# initialize pygame and pygame joystick
pygame.init()
pygame.joystick.init()

# constants
WIDTH = 1280
HEIGHT = 1024
FPS = 30

# game clock
clock = pygame.time.Clock()

# global variables
running = True
showStartScreen = True
playGame = False
showEndScreen = False
currentFrame = None
counter = 0
joysticks = []
character_1 = None
backgrounds = []
backgrounds_index = 0

# canvas
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))

# start screen object
start_screen = Start_Screen(
    "assets/capy_start_screen_NEW.png",
    [],
    1,
    125,
    0,
    HEIGHT,
    WIDTH,
)

# background 1 object
background_1 = Background(
    "assets/forest_path_background.png",
    1,
    0,
    0,
    1,
    50,
    WIDTH - 50,
    50,
    HEIGHT - 50,
    WIDTH,
    HEIGHT,
)
background_2 = Background(
    "assets/Castle.png",
    1,
    0,
    0,
    1,
    50,
    WIDTH - 50,
    50,
    HEIGHT - 50,
    WIDTH,
    HEIGHT,
)
background_3 = Background(
    "assets/hell_background.png",
    1,
    0,
    0,
    1,
    50,
    WIDTH - 50,
    50,
    HEIGHT - 50,
    WIDTH,
    HEIGHT,
)
backgrounds.append(background_1)
backgrounds.append(background_2)
backgrounds.append(background_3)

# player object
player = Player(
    WIDTH // 2,
    HEIGHT // 2,
    "assets/badger_walking_RIGHT.png",
    "assets/badger_walking_LEFT.png",
    "assets/badger_walking_LEFT.png",
    "assets/badger_walking_RIGHT.png",
    "assets/badger_slashing_LEFT.png",
    "assets/badger_slashing_RIGHT.png",
    23,
    23,
    23,
    23,
    9,
    9,
    3,
    3,
    3,
    3,
    3,
    20,
    20,
)

# end screen
end_screen = End_Screen(
    0,
    0,
    1,
    None,
    None,
    "GAME OVER",
    "assets/gameover.png",
)

# sounds
background_1_sound = pygame.mixer.Sound("sounds/Forest_Scene_Concept.mp3")
background_1_sound.set_volume(0.1)
background_2_sound = pygame.mixer.Sound("sounds/Castle_Scene_Concept.mp3")
background_2_sound.set_volume(0.1)
background_3_sound = pygame.mixer.Sound("sounds/Boss_Intro_Concept.mp3")
background_3_sound.set_volume(0.1)

# main game loop
while running:

    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
        if event.type == JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
    
    for joystick in joysticks:
        if joystick.get_button(11):
            showStartScreen = False
            playGame = True

        # joystick control
        if joystick.get_axis(1) < -0.50:
            if backgrounds[backgrounds_index].check_can_move_left(player):
                player.left(counter)
        if joystick.get_axis(1) > 0.50:
            if backgrounds_index == 2 and player.x_coord == WIDTH: # end game for alpha version
                playGame = False
                showEndScreen = True
            player.right(counter)
        if joystick.get_axis(0) > 0.50:
            if backgrounds[backgrounds_index].check_can_move_up(player):
                player.up(counter)
        if joystick.get_axis(0) < -0.50:
            if backgrounds[backgrounds_index].check_can_move_down(player):
                player.down(counter)

    # WASD control
    """
    keys = pygame.key.get_pressed()

    if keys[K_a]:
        if backgrounds[backgrounds_index].check_can_move_left(player):
            player.left(counter)
    if keys[K_d]:
        player.right(counter)
    if keys[K_w]:
        if backgrounds[backgrounds_index].check_can_move_up(player):
            player.up(counter)
    if keys[K_s]:
        if backgrounds[backgrounds_index].check_can_move_down(player):
            player.down(counter)
    """

    # check for correct background, if player off screen on
    # righthand side, switch backgrounds
    if playGame and player.x_coord > WIDTH:
        if backgrounds_index < len(backgrounds) - 1:
            backgrounds_index += 1
        player.x_coord= 0

    if showStartScreen:
        currentFrame = start_screen.generate_return_surface(counter)
        CANVAS.blit(currentFrame, (0, 0))
    elif playGame:
        currentFrame = backgrounds[backgrounds_index].generate_return_surface()
        character_1 = player.get_sprite()
        CANVAS.blit(currentFrame, (0, 0))
        CANVAS.blit(character_1, (player.x_coord, player.y_coord))
        if backgrounds_index == 0:
            background_1_sound.play(-1)
        elif backgrounds_index == 1:
            background_1_sound.stop()
            background_2_sound.play(-1)
        else:
            background_2_sound.stop()
            background_3_sound.play(-1)
    else:
        CANVAS.blit(end_screen.drawEndScreen(CANVAS, joysticks), (0, 0))

    pygame.display.flip()
    
    if counter > (60 * 10):
        counter = 0
    else:
        counter += 1

    clock.tick(FPS)
