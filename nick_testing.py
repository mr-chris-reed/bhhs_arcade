import pygame, sys, time
from Asset_Reader import Asset_Reader
from Start_Screen import Start_Screen

pygame.init()

window = (1024, 1280)
screen = pygame.display.set_mode((1024,1280))
#start_screen = screen.generate_return_surface()
background = pygame.Surface(1024, 1280)

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

    screen.blit(background, (0,0))

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
    

