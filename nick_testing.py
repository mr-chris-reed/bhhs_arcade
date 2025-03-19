import pygame, sys, time
from Asset_Reader import Asset_Reader
from Background import Background
from Start_Screen import Start_Screen

pygame.init()
start_screen = Start_Screen("assets/CapyBarda_Start_Screen.png", 1, 0, 0, 2.1, 1, 0, 0, 1280, 1024)
background1 = Background("assets/forest_path_background.png", 1, 0, 0, 1)
screen = pygame.display.set_mode((start_screen.height, start_screen.width))

clock = pygame.time.Clock()
visible = True
flash_timer = 0
flash_interval = 500
flash_enabled = True

game_start = False

joysticks = []

flash_text = {
    "Flashing Text": {"visible": True, "flash": True, "flash_timer": 0},
    "Static Text": {"visible": True, "flash": False}
    }

while True:
    screen.fill((0, 0, 0))

    screen.blit(start_screen.background[0], (125, 0))

    current_time = pygame.time.get_ticks()
    if current_time - flash_timer > flash_interval:
        visible = not visible
        flash_timer = current_time
    
    if flash_enabled:
        if current_time - flash_text["Flashing Text"]["flash_timer"] > flash_interval:
            flash_text["Flashing Text"]["visible"] = not flash_text["Flashing Text"]["visible"]
            flash_text["Flashing Text"]["flash_timer"] = current_time

    start_screen.draw_text("Press A to Start!", None, (255, 255, 255), 100, 640, 950, visible)
    start_screen.draw_text("Leaderboard:", None, (255, 255, 255), 30, 1150, 10, True)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
        
        if event.type == pygame.JOYBUTTONDOWN:
            for joystick in joysticks:
                if joystick.get_button(11):
                    game_start = True
        
        if game_start == True:
            #start_screen = Start_Screen("bhhs_arcade/assets/forest_path_background.png", 1, 0, 0, 2.1, 1, 0, 0, 1280, 1024)
            screen.blit(background1.get_current_background(), (125, 0))
            print(game_start)

    pygame.display.flip() 
    clock.tick(60)
    

