# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.

import pygame
import sys
from Background import Background


pygame.init()

screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('Background Test')
background1 = Background("assets/background1.png", 1, 0, 0, 2.1)
background2 = Background("assets/background2.png", 1, 0, 0, 2.1)
backgrounds = [background1, background2]

clock = pygame.time.Clock()

# Game loop
while True:
    screen.fill((0, 0, 0))  # Fill the screen with black
    
    # Display the current background
    screen.blit(backgrounds[0].background_list[0], (background1.x, background1.y))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle keypress for moving between backgrounds
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:  # Move to the next background
                b
            elif event.key == pygame.K_LEFT:  # Move to the previous background
                background1.moveToPrev()

    pygame.display.update()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    

