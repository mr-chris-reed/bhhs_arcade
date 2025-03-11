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
    alphabet = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    clock = pygame.time.Clock()
    input_name = 'e'

    # Game loop
    while True:
        screen.fill((0, 0, 0))  # Fill the screen with black
        keys = pygame.key.get_pressed()
        # Display the current background
        screen.blit(background1.backgroundGraphic[0],(0,0))
        pygame.draw.rect(screen, [255,0,0], (500,800,900,200))
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + input_name, True, (255, 255, 255))
        screen.blit(score_text, (50, 50))
        alphabet_counter = 0
        new_letter_text = font.render(alphabet[0])
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == keys[pygame.K_w]:
                pass
                

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit the frame rate to 60 FPS

if __name__ == '__main__':
    main()
