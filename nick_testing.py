import pygame, sys, time
from Asset_Reader import Asset_Reader
from Start_Screen import Start_Screen

pygame.init()

screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('Start_Screen Test')
start_screen = Start_Screen("bhhs_arcade/assets/CapyBarda_Start_Screen.png", 1, 0, 0, 2.1, 1, 0, 0)

clock = pygame.time.Clock()
visible = True
flash_timer = 0
flash_interval = 500
flash_enabled = True

flash_text = {
    "Flashing Text": {"visible": True, "flash": True, "flash_timer": 0},
    "Static Text": {"visible": True, "flash": False}
    }

# Game loop
while True:
    screen.fill((0, 0, 0))  # Fill the screen with black
    
    # Display the current background
    screen.blit(start_screen.background[0], (0,0))

    current_time = pygame.time.get_ticks()
    if current_time - flash_timer > flash_interval:
        visible = not visible
        flash_timer = current_time
    
    if flash_enabled:
        if current_time - flash_text["Flashing Text"]["flash_timer"] > flash_interval:
            flash_text["Flashing Text"]["visible"] = not flash_text["Flashing Text"]["visible"]
            flash_text["Flashing Text"]["flash_timer"] = current_time
        
    start_screen.draw_text("Press A to Start!", None, (255, 255, 255), 40, 250, 100, flash_text["Flashing Text"]["visible"])
    start_screen.draw_text("CapyBarda", None, (255, 255, 255), 40, 250, 150, flash_text["Static Text"]["visible"])
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flash_enabled = False
                flash_text["Flashing Text"]["visible"] = True
    
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    

