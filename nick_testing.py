import pygame, sys, time
from Asset_Reader import Asset_Reader
from Start_Screen import Start_Screen, surface_builder
from Background import Background

pygame.init()

screen = pygame.display.set_mode((1280, 1024))
start_screen = surface_builder(1280, 1040, "bhhs_arcade/assets/CapyBarda_Start_Screen.png", "arial.ttf", "Test", 40, "Press A To Start!", 40)
final_surface = start_screen.generate_return_surface()

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

while True:
    screen.fill((0, 0, 0))

    screen.blit(final_surface, (0, 0))

    current_time = pygame.time.get_ticks()
    if current_time - flash_timer > flash_interval:
        visible = not visible
        flash_timer = current_time
    
    if flash_enabled:
        if current_time - flash_text["Flashing Text"]["flash_timer"] > flash_interval:
            flash_text["Flashing Text"]["visible"] = not flash_text["Flashing Text"]["visible"]
            flash_text["Flashing Text"]["flash_timer"] = current_time
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
        
        #if event.type == pygame.JOYBUTTONDOWN:
            #for joystick in joysticks:
                #if joystick.get_button(11):

    pygame.display.flip() 
    clock.tick(60)
    

