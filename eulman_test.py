# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.

import pygame
import sys
from Background import Background
from End_Screen import End_Screen

def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 1024))
    pygame.display.set_caption('End Screen Test')
    background1 = End_Screen(0,0,1,0,0,0,0,0)

    clock = pygame.time.Clock()

    # Game loop
    while True:
        screen.fill((0, 0, 0))  # Fill the screen with black
        
        # Display the current background
        screen.blit(background1.backgroundGraphic,(0,0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle keypress for moving between backgrounds
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_RIGHT:  # Move to the next background
                    #bg.moveToNext()
                #elif event.key == pygame.K_LEFT:  # Move to the previous background
                    #bg.moveToPrev()

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit the frame rate to 60 FPS

if __name__ == '__main__':
    main()
