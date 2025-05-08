# Main file where pygame game loop will exist.

import pygame, time
from pygame.locals import *
from Asset_Reader import Asset_Reader
from End_Screen import End_Screen
from Start_Screen import Start_Screen
from Background import Background
from Player import Player
from Projectile import Projectile
from Leaderboard import Leaderboard
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
leaderboard_instance = Leaderboard()
leaderboard = leaderboard_instance.read_leaderboard()
current_background = None
previous_background_index = 0
running = True
joysticks = []
counter = 0
previous_counter = 0
notes_left = []
notes_right = []
notes_up = []
notes_down= []
end= False
frame_count = 0

# screen transitions
show_start_screen = True
show_game_screens = False
show_end_screen = False

# load sounds
forest_sound = pygame.mixer.Sound("sounds/Forest_Scene_Concept.mp3")
forest_sound.set_volume(0.05)
castle_sound = pygame.mixer.Sound("sounds/Castle_Scene_Concept.mp3")
castle_sound.set_volume(0.05)
hell_sound = pygame.mixer.Sound("sounds/Boss_Intro_Concept.mp3")
hell_sound.set_volume(0.05)

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
start_screen = Start_Screen("assets/Start_Screen_NEW_5_6_25.png", leaderboard, 1, 100, 50, HEIGHT, WIDTH)
forest_path = Background("assets/Forest_NEW.png", 1, 1, 0, 0, 50, WIDTH - 50, 50, HEIGHT - 50)
castle = Background("assets/Castle_NEW.png", 1, 1, 0, 0, 50, WIDTH - 50, 50, HEIGHT - 50)
hell = Background("assets/Hell_NEW.png", 1, 1, 0, 0, 50, WIDTH - 50, 50, HEIGHT - 50)
capybarda = None
badger_boss = None
tangerine_mimic = None

def constructCapyBarda(capybarda):
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

    # initial position of capybarda
    capybarda.x_coord = 100
    capybarda.y_coord = HEIGHT // 2

    return capybarda

def constructBadgerBoss(badger_boss):
    badger_boss = Player(
        500, 200, 
        "assets/badger_walking_LEFT.png",
        "assets/badger_walking_RIGHT.png",
        "assets/badger_walking_LEFT.png",
        "assets/badger_walking_RIGHT.png",
        "assets/badger_slashing_RIGHT.png",
        "assets/badger_slashing_LEFT.png",
        "assets/badger_slashing_RIGHT.png",
        "assets/badger_slashing_LEFT.png",
        "assets/badger_slashing_RIGHT.png",
        "assets/badger_slashing_LEFT.png",
        "assets/badger_walking_RIGHT.png", 
        23, 23, 23, 23, 9, 9, 9, 9, 9, 23,
        3, 3, 3, 3, 3,
        5, 5
    )

    # initial position of badger_boss
    badger_boss.x_coord = 500
    badger_boss.y_coord = HEIGHT // 2

    return badger_boss

def constructTangerineMimic(tangerine_mimic):
    tangerine_mimic = Player(
        500, 200, 
        "assets/vineup.png",
        "assets/vinedown.png",
        "assets/vineleft.png",
        "assets/vineright.png",
        "assets/vineface.png",
        "assets/vineface.png",
        "assets/vineface.png",
        "assets/vineup.png",
        "assets/vinedown.png",
        "assets/vineleft.png",
        "assets/vineright.png",
        7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
        3, 3, 3, 3, 3,
        5, 5
    )

    # initial position of badger_boss
    tangerine_mimic.x_coord = 500
    tangerine_mimic.y_coord = HEIGHT // 2

    return tangerine_mimic

end_screen = End_Screen(1,1,1,1,1,1,"assets/gameover.png")
hud = HUD(1280, 75, capybarda, 0, (255,0,0))

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

    if show_start_screen:
        # construct player and enimies at start of game
        if capybarda == None:
            capybarda = constructCapyBarda(capybarda)
            badger_boss = constructBadgerBoss(badger_boss)
            capybarda.health = 5
            badger_boss.health = 5

        leaderboard = leaderboard_instance.read_leaderboard()
        if joysticks[0].get_button(11):
            show_start_screen = False
            show_game_screens = True
            end_screen.name = ""
            capybarda.x_coord = 100
            capybarda.y_coord = HEIGHT // 2
            frame_count = 0 
                       
    if show_start_screen: 
        leaderboard = leaderboard_instance.read_leaderboard()
        # start_screen = Start_Screen("assets/Start_Screen_NEW_5_5_25.png", leaderboard, 1, 0, 0, HEIGHT, WIDTH)
        current_background = start_screen
        CANVAS.blit(current_background.generate_return_surface(counter), (0, 0))
        Background.background_index = 0
        forest_sound.stop()
        hell_sound.stop()
        
        end_screen.pressedVisiblity = False
        end_screen.inputVisible = False
        end_screen.visible = True
        end_screen.hasBeenPressedOnce = False

    elif show_game_screens:
        roundedtime = 0
        frame_count += 1
        current_background = backgrounds[Background.background_index]
        CANVAS.blit(current_background.generate_return_surface(), (0, 0))
        if (joysticks[0].get_axis(0) > 0.5):
            if (current_background.check_can_move_up(capybarda)):
                capybarda.up(counter)
        elif (joysticks[0].get_axis(0) < -0.5):
            if (current_background.check_can_move_down(capybarda)):
                capybarda.down(counter)
        elif (joysticks[0].get_axis(1) > 0.5):
            if (current_background.check_can_move_right(capybarda)):
                capybarda.right(counter)
        elif (joysticks[0].get_axis(1) < -0.5):
            if (current_background.check_can_move_left(capybarda)):
                capybarda.left(counter)
        else:
            capybarda.last_sprite = capybarda.spritePicker(counter, capybarda.last_idle_sprite_list)

        ### enemy AI - "follow" ###
        if badger_boss != None:
            if (badger_boss.move_towards_player(capybarda, counter)):
                    capybarda.player_hit(counter)

        if (current_background.check_if_in_next_box(capybarda) and Background.background_index < 2):
            Background.background_index += 1
            
            capybarda.x_coord = 100
            capybarda.y_coord = HEIGHT // 2
        if (current_background.check_if_in_next_box(capybarda) and Background.background_index == 2):
            show_end_screen = True
            show_game_screens = False

        if (current_background.check_if_in_prev_box(capybarda)):
            if Background.background_index >= 0:
                Background.background_index -= 1
                
            if Background.background_index == -1:
                show_game_screens = False
                show_start_screen = True
            
            capybarda.x_coord = 100
            capybarda.y_coord = HEIGHT // 2
     
        CANVAS.blit(capybarda.last_sprite, (capybarda.x_coord, capybarda.y_coord))
        pygame.draw.rect(CANVAS, (255,0,0), capybarda.collision_rect, 2)

        if badger_boss != None and Background.background_index == 0 and badger_boss.alive == True:
            CANVAS.blit(badger_boss.last_sprite, (badger_boss.x_coord, badger_boss.y_coord))
            pygame.draw.rect(CANVAS, (255,0,0), badger_boss.collision_rect, 2)
        else: # badger_boss is no more
            badger_boss = None

        if (joysticks[0].get_button(9)):
            if counter > 5 + previous_counter:
                notes_left.append(Projectile(note_image, capybarda.x_coord + capybarda.width // 2,
                                            capybarda.y_coord + capybarda.height // 3, 20))
                previous_counter = counter
        if (joysticks[0].get_button(8)):
            if counter > 5 + previous_counter:
                notes_right.append(Projectile(note_image, capybarda.x_coord + capybarda.width // 2,
                                              capybarda.y_coord + capybarda.height // 3, 20))
                previous_counter = counter
        if (joysticks[0].get_button(11)):
            if counter > 5 + previous_counter:
                notes_up.append(Projectile(note_image, capybarda.x_coord + capybarda.width // 2,
                                           capybarda.y_coord + capybarda.height // 3, 20))
                previous_counter = counter
        if (joysticks[0].get_button(10)):
            if counter > 5 + previous_counter:
                notes_down.append(Projectile(note_image, capybarda.x_coord + capybarda.width //2,
                                             capybarda.y_coord + capybarda.height // 3, 20))
                previous_counter = counter

        notes_left = check_and_clear_notes(notes_left)
        notes_right = check_and_clear_notes(notes_right)
        notes_up = check_and_clear_notes(notes_up)
        notes_down = check_and_clear_notes(notes_down)

        if badger_boss != None:
            for note in notes_left:
                if (badger_boss.enemy_hit(note, counter)):
                    notes_left.remove(note)
            for note in notes_right:
                if (badger_boss.enemy_hit(note, counter)):
                    notes_right.remove(note)
            for note in notes_up:
                if (badger_boss.enemy_hit(note, counter)):
                    notes_up.remove(note)
            for note in notes_down:
                if (badger_boss.enemy_hit(note, counter)):
                    notes_down.remove(note)

        ### tangerine mimic ###
        if Background.background_index == 1:
            if tangerine_mimic == None:
                tangerine_mimic = constructTangerineMimic(tangerine_mimic)
            else:
                tangerine_mimic.move_towards_player(capybarda, counter)
                CANVAS.blit(tangerine_mimic.last_sprite, (tangerine_mimic.x_coord, tangerine_mimic.y_coord))
                pygame.draw.rect(CANVAS, (255,0,0), tangerine_mimic.collision_rect, 2)
        #######################
        
        for note in notes_left:
            note.move_in_straight_line('L')
            CANVAS.blit(note.projectile_image, (note.x, note.y))
        for note in notes_right:
            note.move_in_straight_line('R')
            CANVAS.blit(note.projectile_image, (note.x, note.y))
        for note in notes_up:
            note.move_in_straight_line('U')
            CANVAS.blit(note.projectile_image, (note.x, note.y))
        for note in notes_down:
            note.move_in_straight_line('D')
            CANVAS.blit(note.projectile_image, (note.x, note.y))

        #timer
        total_seconds = frame_count / (FPS * 2) # gets the time unrounded
        roundedtime=round(total_seconds,2)# rounds time to 2 decimal places
        hud.time= f"{roundedtime:.2f}" # sets hud.time to the rounded time
        
        h = hud.generate_return_surface(0, capybarda.health)
        CANVAS.blit(h, (0, 0))


    elif show_end_screen:
        capybarda = None
        end_screen.drawEndScreen(CANVAS, joysticks)
        if end_screen.pressedVisiblity == True and end_screen.inputVisible == False:
            show_end_screen = False
            show_game_screens = False
            show_start_screen = True
        frame_count = 0
    # play sounds
    if show_game_screens:
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
