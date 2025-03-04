import pygame
import sys
from Start_Screen import Start_Screen


pygame.init()

screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('Start_Screen Test')
start_screen = Start_Screen("Press A to Start", "assets/gameover.png", "CapyBarda", [], "Futura", 1, 0, 0)

clock = pygame.time.Clock()

# Game loop
while True:
    screen.fill((0, 0, 0))  # Fill the screen with black
    
    # Display the current background
    screen.blit(start_screen.background[0], (-300,0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    
