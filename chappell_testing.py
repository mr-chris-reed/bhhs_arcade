import pygame, sys, time
from Asset_Reader import Asset_Reader
from Start_Screen import Start_Screen
from pygame.locals import *

pygame.init()
#initialise the joystick module
pygame.joystick.init()

pygame.display.set_caption('Start_Screen Test')
start_screen = Start_Screen("assets/CapyBarda_Start_Screen.png", 1, 0, 0, 2.1, 1, 0, 0, 1280, 1024)
screen = pygame.display.set_mode((start_screen.height, start_screen.width))

clock = pygame.time.Clock()
running = True
visible = True
flash_timer = 0
flash_interval = 500

joysticks = []

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
    start_screen.draw_text("Leaderboard:", None, (255, 255, 255), 30, 1215, 10, True)
    #can you work on trying to remove the text when game_start == True ?

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


    #show number of connected joysticks
    start_screen.draw_text("Controllers: " + str(pygame.joystick.get_count()), None, pygame.Color("azure"), 25, 900, 20, True)
    for joystick in joysticks:
        start_screen.draw_text("Battery Level: " + str(joystick.get_power_level()), None, pygame.Color("azure"), 25, 900, 40, True)
        start_screen.draw_text("Controller Type: " + str(joystick.get_name()), None, pygame.Color("azure"), 25, 900, 60, True)
        #draw_text("Number of axes: " + str(joystick.get_numaxes()), font, pygame.Color("azure"), 10, 85)

    #button
    for joystick in joysticks:
        if joystick.get_button(11):
            #This will transisiton to the first background for the Alpha
            start_screen.draw_text("Game has definitely, 100 percent started!", None, (255, 255, 255), 80, 620, 500, True)

    pygame.display.update()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    
