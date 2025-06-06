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
counter2 = 0
previous_counter = 0
previous_counter2 = 0
notes_left = []
notes_right = []
notes_up = []
notes_down= []
bolts_left = []
bolts_right = []
bolts_up = []
bolts_down = []
end= False
frame_count = 0
current_boss = None

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

# arrow image
arrow_image = Asset_Reader("assets/arrow.png", 1, 3).get_asset_list()[0]

# wizard's lightning bolts
bolt_vertical_image = Asset_Reader("assets/bolt_vertical.png", 1, 2).get_asset_list()[0]
bolt_horizontal_image = Asset_Reader("assets/bolt_horizontal.png", 1, 2).get_asset_list()[0]

# clearing notes that are off screen
def check_and_clear_projectiles(list):
    temp = []
    for projectile in list:
        if projectile.x > 0 and projectile.x < WIDTH and projectile.y > 0 and projectile.y < HEIGHT:
            temp.append(projectile)
    return temp

# canvas        if (current_background.check_if_in_prev_box(capybarda)):
CANVAS = pygame.display.set_mode((0, 0), FULLSCREEN)

# object creation
start_screen = Start_Screen("assets/Start_Screen_NEW_5_6_25.png", leaderboard, 1.15, 25, 0, HEIGHT, WIDTH)
forest_path = Background("assets/Forest_NEW.png", 1, 1, 0, 0, 50, WIDTH - 50, 50, HEIGHT - 50)
castle = Background("assets/Castle_NEW.png", 1, 1, 0, 0, 50, WIDTH - 50, 50, HEIGHT - 50)
hell = Background("assets/Hell_NEW.png", 1, 1, 0, 0, 50, WIDTH - 50, 50, HEIGHT - 50)

capybarda = Player(
    'capybarda',
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
    10, 10, 7)

    # initial position of capybarda
capybarda.x_coord = 100
capybarda.y_coord = HEIGHT // 2

badger_boss = Player(
    'badger_boss',
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
    5, 5, 5
    )

# initial position of badger_boss
badger_boss.x_coord = WIDTH - 200
badger_boss.y_coord = HEIGHT // 2

tangerine_mimic = Player(
    'tangerine_mimic',
    500, 200, 
    "assets/no_trim_no_repage.png",
    "assets/no_trim_no_repage.png",
    "assets/no_trim_no_repage.png",
    "assets/no_trim_no_repage.png",
    "assets/no_trim_no_repage.png",
    "assets/no_trim_no_repage.png",
    "assets/no_trim_no_repage.png",
    "assets/no_trim_no_repage.png",
    "assets/no_trim_no_repage.png",
    "assets/no_trim_no_repage.png",
    "assets/no_trim_no_repage.png",
    11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
    1.5, 1.5, 1.5, 1.5, 1.5,
    5, 5, 12
)

# initial position of tangerine_mimic
tangerine_mimic.x_coord = WIDTH - 200
tangerine_mimic.y_coord = HEIGHT // 2

wizard = Player(
    'wizard',
    500, 200, 
    "assets/wizard_frontwalk.png",
    "assets/wizard_frontwalk.png",
    "assets/wizard_frontwalk.png",
    "assets/wizard_frontwalk.png",
    "assets/wizard_frontwalk.png",
    "assets/wizard_frontwalk.png",
    "assets/wizard_frontwalk.png",
    "assets/wizard_frontwalk.png",
    "assets/wizard_frontwalk.png",
    "assets/wizard_frontwalk.png",
    "assets/wizard_frontwalk.png", 
    8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
    1.5, 1.5, 1.5, 1.5, 1.5,
    5, 5, 20
    )

# initial position of wizard
wizard.x_coord = WIDTH - 200
wizard.y_coord = HEIGHT // 2

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
        notes_left = []
        notes_right = []
        notes_up = []
        notes_down= []
        bolts_left = []
        bolts_right = []
        bolts_up = []
        bolts_down = []
        capybarda.health = 7
        badger_boss.health = 7

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
        start_screen = Start_Screen("assets/Start_Screen_NEW_5_6_25.png", leaderboard, 1.15, 25, 0, HEIGHT, WIDTH)
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
        if badger_boss.alive == True and Background.background_index == 0:
            current_boss = badger_boss
            if (badger_boss.move_towards_player(capybarda, counter)):
                    capybarda.player_hit(counter)
        
        if wizard.alive == True and Background.background_index == 2:
            current_boss = wizard
            if (wizard.move_towards_player(capybarda, counter)):
                    capybarda.player_hit(counter)

        if (current_background.check_if_in_next_box(capybarda) and Background.background_index == 0 and badger_boss.alive == False ):
            Background.background_index += 1
            
            capybarda.x_coord = 100
            capybarda.y_coord = HEIGHT // 2
        
        if (current_background.check_if_in_next_box(capybarda) and Background.background_index == 1 and tangerine_mimic.alive == False ):
            Background.background_index += 1

            capybarda.x_coord = 100
            capybarda.y_coord = HEIGHT // 2
        

        if (current_background.check_if_in_next_box(capybarda) and Background.background_index == 2 and wizard.alive == False):
            show_end_screen = True
            show_game_screens = False
        '''
        if (current_background.check_if_in_prev_box(capybarda)):
            if Background.background_index >= 0:
                Background.background_index -= 1
                
            if Background.background_index == -1:
                show_game_screens = False
                show_start_screen = True
        ''' 
        #capybarda.x_coord = 100
        #capybarda.y_coord = HEIGHT // 2

        # flashing arrow for next screen
        if counter % 30 > 0 and counter % 30 < 15 and not(show_end_screen):
            if Background.background_index == 0 and badger_boss.alive == False:
                CANVAS.blit(arrow_image, (1000, 415))
            elif Background.background_index == 1 and tangerine_mimic.alive == False:
                CANVAS.blit(arrow_image, (1000, 415))
            elif Background.background_index == 2 and wizard.alive == False:
                CANVAS.blit(arrow_image, (1000, 415))
        
        CANVAS.blit(capybarda.last_sprite, (capybarda.x_coord, capybarda.y_coord))
        #pygame.draw.rect(CANVAS, (255,0,0), capybarda.collision_rect, 2)

        if Background.background_index == 0 and badger_boss.alive == True:
            CANVAS.blit(badger_boss.last_sprite, (badger_boss.x_coord, badger_boss.y_coord))
            #pygame.draw.rect(CANVAS, (255,0,0), badger_boss.collision_rect, 2)

        if Background.background_index == 2:
            
            if wizard.alive == True:
                CANVAS.blit(wizard.last_sprite, (wizard.x_coord, wizard.y_coord))
                #pygame.draw.rect(CANVAS, (255,0,0), wizard.collision_rect, 2)

        if (joysticks[0].get_button(9)):
            if counter > 10 + previous_counter:
                notes_left.append(Projectile(note_image, capybarda.x_coord + capybarda.width // 2,
                                            capybarda.y_coord + capybarda.height // 3, 20))
                previous_counter = counter
        if (joysticks[0].get_button(8)):
            if counter > 10 + previous_counter:
                notes_right.append(Projectile(note_image, capybarda.x_coord + capybarda.width // 2,
                                              capybarda.y_coord + capybarda.height // 3, 20))
                previous_counter = counter
        if (joysticks[0].get_button(11)):
            if counter > 10 + previous_counter:
                notes_up.append(Projectile(note_image, capybarda.x_coord + capybarda.width // 2,
                                           capybarda.y_coord + capybarda.height // 3, 20))
                previous_counter = counter
        if (joysticks[0].get_button(10)):
            if counter > 10 + previous_counter:
                notes_down.append(Projectile(note_image, capybarda.x_coord + capybarda.width //2,
                                             capybarda.y_coord + capybarda.height // 3, 20))
                previous_counter = counter

        notes_left = check_and_clear_projectiles(notes_left)
        notes_right = check_and_clear_projectiles(notes_right)
        notes_up = check_and_clear_projectiles(notes_up)
        notes_down = check_and_clear_projectiles(notes_down)

        if badger_boss.alive == True:
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

        if wizard.alive == True and Background.background_index == 2:
            for note in notes_left:
                if (wizard.enemy_hit(note, counter)):
                    notes_left.remove(note)
            for note in notes_right:
                if (wizard.enemy_hit(note, counter)):
                    notes_right.remove(note)
            for note in notes_up:
                if (wizard.enemy_hit(note, counter)):
                    notes_up.remove(note)
            for note in notes_down:
                if (wizard.enemy_hit(note, counter)):
                    notes_down.remove(note)

            # check if wizard is inline with capybardy
            # if true, fire projectiles
            # if hit, decrement capy's life
            # remove lightning bolts if hit capy
            # clear lightning bolts when off screen
            # fire bolts indiscriminately

            if counter2 > 15 + previous_counter2:
                bolts_up.append(Projectile(bolt_vertical_image, wizard.x_coord + wizard.width // 2,
                                           wizard.y_coord + wizard.height // 3, 20))
                bolts_down.append(Projectile(bolt_vertical_image, wizard.x_coord + wizard.width // 2,
                                           wizard.y_coord + wizard.height // 3, 20))
                bolts_left.append(Projectile(bolt_vertical_image, wizard.x_coord + wizard.width // 2,
                                           wizard.y_coord + wizard.height // 3, 20))
                bolts_right.append(Projectile(bolt_horizontal_image, wizard.x_coord + wizard.width // 2,
                                           wizard.y_coord + wizard.height // 3, 20))
                previous_counter2 = counter2

            for bolt in bolts_left:
                bolt.move_in_straight_line('L')
                CANVAS.blit(bolt.projectile_image, (bolt.x, bolt.y))
            for bolt in bolts_right:
                bolt.move_in_straight_line('R')
                CANVAS.blit(bolt.projectile_image, (bolt.x, bolt.y))
            for bolt in bolts_up:
                bolt.move_in_straight_line('U')
                CANVAS.blit(bolt.projectile_image, (bolt.x, bolt.y))
            for bolt in bolts_down:
                bolt.move_in_straight_line('D')
                CANVAS.blit(bolt.projectile_image, (bolt.x, bolt.y))

            if capybarda.alive == True:
                for bolt in bolts_left:
                    if (capybarda.enemy_hit(bolt, counter2)):
                        bolts_left.remove(bolt)
                for bolt in bolts_right:
                    if (capybarda.enemy_hit(bolt, counter2)):
                        bolts_right.remove(bolt)
                for bolt in bolts_up:
                    if (capybarda.enemy_hit(bolt, counter2)):
                        bolts_up.remove(bolt)
                for bolt in bolts_down:
                    if (capybarda.enemy_hit(bolt, counter2)):
                        bolts_down.remove(bolt)

            bolts_left = check_and_clear_projectiles(bolts_left)
            bolts_right = check_and_clear_projectiles(bolts_right)
            bolts_up = check_and_clear_projectiles(bolts_up)
            bolts_down = check_and_clear_projectiles(bolts_down)
            
        ### tangerine mimic ###
        if Background.background_index == 1 and tangerine_mimic.alive == True:
            current_boss = tangerine_mimic
            if (tangerine_mimic.move_towards_player(capybarda, counter)):
                capybarda.player_hit(counter)
            CANVAS.blit(tangerine_mimic.last_sprite, (tangerine_mimic.x_coord, tangerine_mimic.y_coord))
            #pygame.draw.rect(CANVAS, (255,0,0), tangerine_mimic.collision_rect, 2)

        if tangerine_mimic.alive == True and Background.background_index == 1:
            for note in notes_left:
                if (tangerine_mimic.enemy_hit(note, counter)):
                    notes_left.remove(note)
            for note in notes_right:
                if (tangerine_mimic.enemy_hit(note, counter)):
                    notes_right.remove(note)
            for note in notes_up:
                if (tangerine_mimic.enemy_hit(note, counter)):
                    notes_up.remove(note)
            for note in notes_down:
                if (tangerine_mimic.enemy_hit(note, counter)):
                    notes_down.remove(note)
        
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
       
        frame_count += 1
        h = hud.generate_return_surface(0, capybarda.health, frame_count, current_boss)
        CANVAS.blit(h, (0, 0))


    elif show_end_screen:

        end_screen.drawEndScreen(CANVAS, joysticks, hud)

        if end_screen.pressedVisiblity == True and end_screen.inputVisible == False:
    
            capybarda.alive = True
            capybarda.health = 7

            badger_boss.alive = True
            badger_boss.health = 5
            badger_boss.x_coord = 500
            badger_boss.y_coord = HEIGHT // 2

            tangerine_mimic.alive = True
            tangerine_mimic.health = 20
            tangerine_mimic.x_coord = 500
            tangerine_mimic.y_coord = HEIGHT // 2

            wizard.alive = True
            wizard.health = 16
            wizard.x_coord = 500
            wizard.y_coord = HEIGHT // 2

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

    if counter2 >= 600:
        counter2 = 0
        previous_counter2 = 0
    else:
        counter2 += 1
    
    # check if capybarda is still alive
    # and restart if necessary
    if capybarda.health <= 0:
        capybarda.alive = False
        if capybarda.alive == False:
            show_start_screen = True
            show_game_screens = False
            show_end_screen = False
            capybarda.alive = True
            capybarda.health = 7
            badger_boss.alive = True
            badger_boss.health = 5
            tangerine_mimic.alive = True
            tangerine_mimic.health = 20
            wizard.alive = True
            wizard.health = 16
            forest_sound.stop()
            castle_sound.stop()
            hell_sound.stop()
            badger_boss.x_coord = WIDTH - 200
            badger_boss.y_coord = HEIGHT // 2
            tangerine_mimic.x_coord = WIDTH - 200
            tangerine_mimic.y_coord = HEIGHT // 2
            wizard.x_coord = WIDTH - 200
            wizard.y_coord = HEIGHT // 2

   
    
    pygame.display.flip()
    clock.tick(FPS)

    # print("capy health = ", capybarda.health, " badger health = ", badger_boss.health, " tangerine health = ", tangerine_mimic.health, " wizard health = ", wizard.health)
