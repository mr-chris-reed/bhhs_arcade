import pygame, sys, time
from Asset_Reader import Asset_Reader
from Start_Screen import Start_Screen

pygame.init()
#initialise the joystick module
pygame.joystick.init()

screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('Start_Screen Test')
start_screen = Start_Screen("bhhs_arcade/assets/CapyBarda_Start_Screen.png", 1, 0, 0, 2.1, 1, 0, 0)

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
    start_screen.draw_text("Leaderboard:", None, (255, 255, 255), 35, 80, 300, True)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
    #button
    for joystick in joysticks:
        if joystick.get_button(11) and start_screen.background == Asset_Reader("assets/CapyBarda_Start_Screen.png", 1, 1).get_asset_list():
            start_screen == Asset_Reader("assets/background1.png", 1, 1).get_asset_list()
            print(True)
            pygame.time.wait(100)
        elif joystick.get_button(11) and start_screen == "bhhs_arcade/assets/background1.png":
            start_screen.background == "bhhs_arcade/assets/CapyBarda_Start_Screen.png"
            pygame.time.wait(100)

    pygame.display.update()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    
