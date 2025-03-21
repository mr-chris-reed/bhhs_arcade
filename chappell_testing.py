import pygame, sys, time
from Asset_Reader import Asset_Reader
from Background import Background
from Start_Screen import Start_Screen
from pygame.locals import *

pygame.init()
#initialise the joystick module
pygame.joystick.init()

pygame.display.set_caption('Start_Screen Test')
start_screen = Start_Screen("assets/CapyBarda_Start_Screen.png", 1, 2.1, 1, 0, 1280, 1024)
background1 = Background("assets/forest_path_background.png", 1, 0, 0, 1)
screen = pygame.display.set_mode((start_screen.height, start_screen.width))

clock = pygame.time.Clock()
visible = True
flash_timer = 0
flash_interval = 500
flash_enabled = True
game_start = False
title_screen = True

joysticks = []

flash_text = {
    "Flashing Text": {"visible": True, "flash": True, "flash_timer": 0},
    "Static Text": {"visible": True, "flash": False}
    }

# Game loop
while True:

    screen.fill((0, 0, 0))  # Fill the screen with black
    
    # Display the current background
    screen.blit(start_screen.background[0], (125, 0))
    
    current_time = pygame.time.get_ticks()
    if current_time - flash_timer > flash_interval:
        visible = not visible
        flash_timer = current_time
        
    start_screen.draw_text("Press A to Start!", None, (255, 255, 255), 100, 640, 950, visible)
    start_screen.draw_text("Leaderboard:", None, (255, 255, 255), 30, 1215, 10, title_screen)

    #A for loop that displays however many players on the leaderboard
    # for string in start_screen.leaderboard:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #button
    for joystick in joysticks:
        #This will transisiton to the first background for the Alpha
        if joystick.get_button(11):
            start_screen.draw_text("Game has definitely, 100 percent started!", None, (255, 255, 255), 80, 620, 500, True)
            #This deactivates the text that isn't blinking. I couldn't find a solution to the blinking text yet.
            title_screen = False
            game_start = True
        
    if game_start == True:
        #start_screen = Start_Screen("bhhs_arcade/assets/forest_path_background.png", 1, 0, 0, 2.1, 1, 0, 0, 1280, 1024)
        screen.blit(background1.get_current_background(), (125, 0))
        
    if game_start == False:
        screen.blit(start_screen.background[0], (125, 0))

    if flash_enabled:
        if current_time - flash_text["Flashing Text"]["flash_timer"] > flash_interval:
            flash_text["Flashing Text"]["visible"] = not flash_text["Flashing Text"]["visible"]
            flash_text["Flashing Text"]["flash_timer"] = current_time

    #show number of connected joysticks
    start_screen.draw_text("Controllers: " + str(pygame.joystick.get_count()), None, pygame.Color("azure"), 25, 900, 20, title_screen)
    for joystick in joysticks:
        start_screen.draw_text("Battery Level: " + str(joystick.get_power_level()), None, pygame.Color("azure"), 25, 900, 40, title_screen)
        start_screen.draw_text("Controller Type: " + str(joystick.get_name()), None, pygame.Color("azure"), 25, 900, 60, title_screen)

    pygame.display.flip()
    pygame.display.update()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    
