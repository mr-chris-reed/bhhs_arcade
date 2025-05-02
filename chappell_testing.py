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
screen = pygame.display.set_mode((1280, 1024))
capybarda = Player(
    200, 200, 
    "assets/CapybardaRun_back.png", 
    "assets/CapybardaRun_front.png", 
    "assets/CapybardaRun_Side2.png", 
    "assets/CapybardaRun_side.png", 
    "assets/CapybardaIdle_front.png", 
    "assets/CapybardaIdle_side.png",
    "assets/CapybardaIdle_back.png",
    "assets/CapybardaIdle_back.png", 
    "assets/CapybardaIdle_front.png", 
    "assets/CapybardaIdle_side2.png", 
    "assets/CapybardaIdle_side.png",
    6, 4, 4, 6, 4, 4, 4, 4, 4, 4,
    0.6, 0.6, 0.6, 0.6, 0.6,
    10, 10
)
hud = HUD(1280, 100, player, player.health, clock)

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

screen.fill((255, 255, 255))  # Fill the screen with white
    
# Display the current background
#screen.blit(background1.generate_return_surface(), (125, 0))
h = hud.generate_return_surface(clock)
screen.blit(h, (0, 0))

# clearing notes that are off screen
def check_and_clear_notes(list):
    temp = []
    for note in list:
        if note.x > 0 and note.x < WIDTH and note.y > 0 and note.y < HEIGHT:
            temp.append(note)
    return temp

# canvas        if (current_background.check_if_in_prev_box(capybarda)):
CANVAS = pygame.display.set_mode((0, 0))

player_hud = HUD(1280, 200,None,None, clock, (0, 0, 255))
time = 0
# main game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False

        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
    if (FPS % 30 == 0):
        time += 1   
    CANVAS.blit(player_hud.generate_return_surface(time), (0, 0))
    
    pygame.display.flip()
    clock.tick(FPS)