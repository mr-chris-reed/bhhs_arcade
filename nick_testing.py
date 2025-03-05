import pygame
import sys
from Start_Screen import Start_Screen


pygame.init()

screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('Start_Screen Test')
start_screen = Start_Screen("bhhs_arcade/assets/gameover.png", 1, 0, 0, 2.1, 1, 0, 0)

clock = pygame.time.Clock()

# Game loop
while True:
    screen.fill((0, 0, 0))  # Fill the screen with black
    
    # Display the current background
    screen.blit(start_screen.background[0], (0,0))
    font_title = pygame.font.SysFont('Arial', 64)
    title_text = font_title.render("CappyBarda", True, (255, 255, 255))
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    

