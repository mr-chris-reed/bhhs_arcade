# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.

import pygame
import sys
from Background import Background

def main():
    pygame.init()

    # Load background images
    # background1 = pygame.image.load('background1.png')
    # background2 = pygame.image.load('background2.png')
    # background3 = pygame.image.load('background3.png')

    # backgrounds = [background1, background2, background3]

    screen = pygame.display.set_mode((1280, 1024))
    pygame.display.set_caption('Background Test')
    background1 = Background("assets/background1.png", 1, 0, 0, 2.1)

    clock = pygame.time.Clock()

    # Game loop
    while True:
        screen.fill((0, 0, 0))  # Fill the screen with black
        
        # Display the current background
        screen.blit(background1.background_list[0], (background1.x, background1.y))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle keypress for moving between backgrounds
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_RIGHT:  # Move to the next background
                    #background1.moveToNext()
                #elif event.key == pygame.K_LEFT:  # Move to the previous background
                    #bg.moveToPrev()

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit the frame rate to 60 FPS
