import pygame, sys, time
from Asset_Reader import Asset_Reader
from Background import Background
from Player import Player
from HUD import HUD
from pygame.locals import *

pygame.init()
#initialise the joystick module
pygame.joystick.init()

pygame.display.set_caption('HUD Test')
background1 = Background("assets/Forest_NEW.png", 1, 1, 0, 0, 50, 1280 - 50, 50, 1024 - 50)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 1024))
player = Player(
    200, 200,
    "assets/CapybardaRun_back.png", "assets/CapybardaRun_front.png", "assets/CapybardaRun_Side2.png", "assets/CapybardaRun_side.png", "assets/CapybardaIdle_front.png", "assets/CapybardaIdle_back.png",
    "assets/CapybardaIdle_back.png", "assets/CapybardaIdle_front.png", "assets/CapybardaIdle_side2.png", "assets/CapybardaIdle_side.png",
    6, 4, 4, 6, 4, 4, 4, 4, 4, 4,
    0.6, 0.6, 0.6, 0.6, 0.6,
    10, 10
)
hud = HUD(1280, 100, player, player.health, clock)

# joysticks = []

# Game loop
while True:

    screen.fill((255, 255, 255))  # Fill the screen with white
    
    # Display the current background
    #screen.blit(background1.generate_return_surface(), (125, 0))
    h = hud.generate_return_surface(clock)
    screen.blit(h, (0, 0))

    # Event handling
    for event in pygame.event.get():
        #if event.type == pygame.JOYDEVICEADDED:
            #joy = pygame.joystick.Joystick(event.device_index)
            #joysticks.append(joy)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #button
    #for joystick in joysticks:
        #This will transisiton to the first background for the Alpha
        #if joystick.get_button(11):
            #start_screen.draw_text("Game has definitely, 100 percent started!", None, (255, 255, 255), 80, 620, 500, True)
            #This deactivates the text that isn't blinking. I couldn't find a solution to the blinking text yet.
            #title_screen = False
            #game_start = True
        
    #show number of connected joysticks
    #start_screen.draw_text("Controllers: " + str(pygame.joystick.get_count()), None, pygame.Color("azure"), 25, 900, 20, title_screen)
    #for joystick in joysticks:
        #start_screen.draw_text("Battery Level: " + str(joystick.get_power_level()), None, pygame.Color("azure"), 25, 900, 40, title_screen)
        #start_screen.draw_text("Controller Type: " + str(joystick.get_name()), None, pygame.Color("azure"), 25, 900, 60, title_screen)

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    
