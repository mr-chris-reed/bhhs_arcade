import pygame, sys, time
from Asset_Reader import Asset_Reader
from Start_Screen import Start_Screen
from Background import Background

pygame.init()

screen = pygame.display.set_mode((1280, 1024))
forest_path_background = Start_Screen("assets/forest_path_background.png", 1, 0, 0, 1.0, 0, 0, 0)
start_screen = Start_Screen("assets/CapyBarda_Start_Screen.png", 1, 0, 0, 2.1, 1, 0, 0)

clock = pygame.time.Clock()
visible = True
flash_timer = 0
flash_interval = 500
flash_enabled = True

joysticks = []

flash_text = {
    "Flashing Text": {"visible": True, "flash": True, "flash_timer": 0},
    "Static Text": {"visible": True, "flash": False}
    }

for joystick in joysticks:
        if joystick.get_button(11) and start_screen.background == Asset_Reader("assets/CapyBarda_Start_Screen.png", 1, 1).get_asset_list():
            start_screen == Asset_Reader("bhhs_arcade/assets/Forest path.png", 1, 1).get_asset_list()
            pygame.time.wait(100)
        elif joystick.get_button(11) and start_screen == "bhhs_arcade/assets/Forest path.png":
            start_screen.background == "bhhs_arcade/assets/CapyBarda_Start_Screen.png"
            pygame.time.wait(100)

while True:
    screen.fill((0, 0, 0))
    
    screen.blit(start_screen.background[0], (0,0))

    current_time = pygame.time.get_ticks()
    if current_time - flash_timer > flash_interval:
        visible = not visible
        flash_timer = current_time
    
    if flash_enabled:
        if current_time - flash_text["Flashing Text"]["flash_timer"] > flash_interval:
            flash_text["Flashing Text"]["visible"] = not flash_text["Flashing Text"]["visible"]
            flash_text["Flashing Text"]["flash_timer"] = current_time
        
    start_screen.draw_text("Press A to Start!", None, (255, 255, 255), 100, 500, 950, visible)
    
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
                    screen.blit(start_screen.background[0], (0,0))

    pygame.display.flip() 
    clock.tick(60)
    

