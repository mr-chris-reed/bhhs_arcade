import pygame
from pygame.locals import *
from Asset_Reader import Asset_Reader
from End_Screen import End_Screen
from Start_Screen import Start_Screen
from Background import Background
from Player import Player
from Projectile import Projectile
from End_Screen import End_Screen
from HUD import HUD
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
end= False
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
forest_path = Background("assets/forest_path_background.png", 1, 1, 0, 0, 50, WIDTH - 50, 50, HEIGHT - 50)
castle = Background("assets/Castle.png", 1, 1, 0, 0, 50, WIDTH - 50, 50, HEIGHT - 50)
hell = Background("assets/_Hell_.png", 1, 1, 0, 0, 50, WIDTH - 50, 50, HEIGHT - 50)
capybarda = Player(
    200, 200,
    "assets/CapybardaRun_back.png", "assets/CapybardaRun_front.png", "assets/CapybardaRun_Side2.png", "assets/CapybardaRun_side.png", "assets/CapybardaIdle_front.png", "assets/CapybardaIdle_back.png",
    "assets/CapybardaIdle_back.png", "assets/CapybardaIdle_front.png", "assets/CapybardaIdle_side2.png", "assets/CapybardaIdle_side.png",
    6, 4, 4, 6, 4, 4, 4, 4, 4, 4,
    0.6, 0.6, 0.6, 0.6, 0.6,
    10, 10
)

badger_boss = Player(
    500, 200, 
    "assets/badger_walking_LEFT.png", "assets/badger_walking_RIGHT.png", "assets/badger_walking_LEFT.png", "assets/badger_walking_RIGHT.png", "assets/badger_slashing_LEFT.png", "assets/badger_slashing_RIGHT.png", "assets/badger_slashing_LEFT.png", "assets/badger_slashing_RIGHT.png", "assets/badger_slashing_LEFT.png", "assets/badger_walking_RIGHT.png", 
    23, 23, 23, 23, 23, 23, 23, 23, 23, 23,
    0.6, 0.6, 0.6, 0.6, 0.6,
    10, 10
)

player_hud = HUD(1280, 200,None,None,None,None)
end_screen = End_Screen(1,1,1,1,1,1,"assets/gameover.png")
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

        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)

    if not(game_start) and not(end):
        if joysticks[0].get_button(11):
            game_start = True
            end_screen.name = ""
    
    if not(game_start) and not(end): 
        current_background = start_screen
        CANVAS.blit(HUD.generate_return_surface(), (0, 0))
    
    pygame.display.flip()
    clock.tick(FPS)