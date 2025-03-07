import pygame, sys, time
from Asset_Reader import Asset_Reader
from Start_Screen import Start_Screen

pygame.init()

screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('Start_Screen Test')
start_screen = Start_Screen("bhhs_arcade/assets/gameover.png", 1, 0, 0, 2.1, 1, 0, 0)

clock = pygame.time.Clock()
running = True
visible = True
flash_timer = 0
flash_interval = 500

# Game loop
while True:
    screen.fill((0, 0, 0))  # Fill the screen with black
    
    # Display the current background
    screen.blit(start_screen.background[0], (0,0))
    
    current_time = pygame.time.get_ticks()
    if current_time - flash_timer > flash_interval:
        visible = not visible
        flash_timer = current_time
        
    start_screen.draw_text("CapyBarda", None, (255, 255, 255), 36, 400, 300, visible)
    start_screen.draw_text("Press A to Start!", None, (255, 255, 255), 36, 500, 400, visible)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    

