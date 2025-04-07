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
from Projectile import Projectile

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
previous_background_index = 0
running = True
game_start = False
joysticks = []
counter = 0
previous_counter = 0
leaderboard = [['CMC', "7.5"], ['CWJ', "7.8"], ['TGP', "8.1"]]
notes_left = []
notes_right = []
notes_up = []
notes_down= []

# load sounds
forest_sound = pygame.mixer.Sound("sounds/Forest_Scene_Concept.mp3")
forest_sound.set_volume(0.20)
castle_sound = pygame.mixer.Sound("sounds/Castle_Scene_Concept.mp3")
castle_sound.set_volume(0.20)
hell_sound = pygame.mixer.Sound("sounds/Boss_Intro_Concept.mp3")
hell_sound.set_volume(0.20)

# note image
note_image = Asset_Reader("assets/note.png", 1, 0.5).get_asset_list()[0]

# clearing notes that are off screen
def check_and_clear_notes(list):
    temp = []
    for note in list:
        if note.x > 0 and note.x < WIDTH and note.y > 0 and note.y < HEIGHT:
            temp.append(note)
    return temp

# canvas        if (current_background.check_if_in_prev_box(capybarda)):

CANVAS = pygame.display.set_mode((0, 0), FULLSCREEN)

# object creation
start_screen = Start_Screen("assets/start_screen.png", leaderboard, 1, 0, 0, HEIGHT, WIDTH)
forest_path = Background("assets/forest_path_background.png", 1, 1, 0, 0, -150, WIDTH + 150, 50, HEIGHT - 50)
castle = Background("assets/Castle.png", 1, 1, 0, 0, -150, WIDTH + 150, 50, HEIGHT - 50)
hell = Background("assets/_Hell_.png", 1, 1, 0, 0, -150, WIDTH + 150, 50, HEIGHT - 50)
capybarda = Player(
    200, 200,
    "assets/CapybardaRun_back.png", "assets/CapybardaRun_front.png", "assets/CapybardaRun_Side2.png", "assets/CapybardaRun_side.png", "assets/CapybardaIdle_front.png", "assets/CapybardaIdle_back.png",
    "assets/CapybardaIdle_back.png", "assets/CapybardaIdle_front.png", "assets/CapybardaIdle_side2.png", "assets/CapybardaIdle_side.png",
    6, 4, 4, 6, 4, 4, 4, 4, 4, 4,
    0.6, 0.6, 0.6, 0.6, 0.6,
    10, 10
)
# initial position of capybarda
capybarda.x_coord = 100
capybarda.y_coord = HEIGHT // 2

backgrounds = [forest_path, castle, hell]
current_background = start_screen

# main game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False

    keys = pygame.key.get_pressed()
    game_start = True
    
    if not(game_start):
        current_background = start_screen
        CANVAS.blit(current_background.generate_return_surface(counter), (0, 0))
    elif game_start:
        current_background = backgrounds[Background.background_index]
        CANVAS.blit(current_background.generate_return_surface(), (0, 0))
        if keys[pygame.K_w]:
            if (current_background.check_can_move_up(capybarda)):
                capybarda.up(counter)
        elif keys[pygame.K_s]:
            if (current_background.check_can_move_down(capybarda)):
                capybarda.down(counter)
        elif keys[pygame.K_d]:
            if (current_background.check_can_move_right(capybarda)):
                capybarda.right(counter)
        if keys[pygame.K_a]:
            if (current_background.check_can_move_left(capybarda)):
                capybarda.left(counter)
        if (current_background.check_if_in_next_box(capybarda) and Background.background_index < 2):
            Background.background_index += 1
            capybarda.x_coord = -100
            capybarda.y_coord = HEIGHT // 2
        if (current_background.check_if_in_prev_box(capybarda)):
            if Background.background_index > 0:
                Background.background_index -= 1
            if Background.background_index == 0:
                game_start = False
            capybarda.x_coord = 1200
            capybarda.y_coord = HEIGHT // 2
        if keys[pygame.K_UP]:
            if counter > 5 + previous_counter:
                notes_left.append(Projectile(note_image, capybarda.x_coord, capybarda.y_coord, 20))
                previous_counter = counter
        elif keys[pygame.K_DOWN]:
            if counter > 5 + previous_counter:
                notes_right.append(Projectile(note_image, capybarda.x_coord, capybarda.y_coord, 20))
                previous_counter = counter
        elif keys[pygame.K_LEFT]:
            if counter > 5 + previous_counter:
                notes_up.append(Projectile(note_image, capybarda.x_coord, capybarda.y_coord, 20))
                previous_counter = counter
        elif keys[pygame.K_RIGHT]:
            if counter > 5 + previous_counter:
                notes_down.append(Projectile(note_image, capybarda.x_coord, capybarda.y_coord, 20))
                previous_counter = counter

        notes_left = check_and_clear_notes(notes_left)
        notes_right = check_and_clear_notes(notes_right)
        notes_up = check_and_clear_notes(notes_up)
        notes_down = check_and_clear_notes(notes_down)
        

        CANVAS.blit(capybarda.last_sprite, (capybarda.x_coord, capybarda.y_coord))

    # play sounds
    if game_start:
        if Background.background_index == 0:
            forest_sound.play()
            castle_sound.stop()
            hell_sound.stop()
        elif Background.background_index == 1:
            castle_sound.play()
            forest_sound.stop()
            hell_sound.stop()
        elif Background.background_index == 2:
            hell_sound.play()
            forest_sound.stop()
            castle_sound.stop()

    if counter >= 600:
        counter = 0
        previous_counter = 0
    else:
        counter += 1

    pygame.display.flip()
    clock.tick(FPS)
