# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.

import pygame
import sys

class Background:
    def __init__(self, backgrounds, x, y, width, height):
        self.backgrounds = backgrounds  # List of backgrounds
        self.currentIndex = 0  # Index of the current background
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def moveToNext(self):
        if self.currentIndex < len(self.backgrounds) - 1:  # Check if there is a next background
            self.currentIndex += 1

    def moveToPrev(self):
        if self.currentIndex > 0:  # Check if there is a previous background
            self.currentIndex -= 1

    def getCurrentBackground(self):
        return self.backgrounds[self.currentIndex]  # Get the current background

def main():
    pygame.init()

    # Load background images
    background1 = pygame.image.load('background1.png')
    background2 = pygame.image.load('background2.png')
    background3 = pygame.image.load('background3.png')

    backgrounds = [background1, background2, background3]

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Background Test')

    # Create a Background object with the list of backgrounds
    bg = Background(backgrounds, 0, 0, 800, 600)

    clock = pygame.time.Clock()

    # Game loop
    while True:
        screen.fill((0, 0, 0))  # Fill the screen with black
        
        # Display the current background
        screen.blit(bg.getCurrentBackground(), (bg.x, bg.y))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle keypress for moving between backgrounds
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:  # Move to the next background
                    bg.moveToNext()
                elif event.key == pygame.K_LEFT:  # Move to the previous background
                    bg.moveToPrev()

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit the frame rate to 60 FPS

if __name__ == '__main__':
    main()
