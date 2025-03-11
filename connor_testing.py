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
hell_background = Background("assets/hell_background.png", 1, 0, 0, 1.0, 0, 0, 0, 0)
forest_path_background = Background("assets/forest_path_background.png", 1, 0, 0, 1.0, 0, 0, 0, 0)
background2 = Background("assets/background2.png", 1, 0, 0, 1.0, 0, 0, 0, 0)
backgrounds = [forest_path_background, hell_background, background2]
background_index = 0

clock = pygame.time.Clock()

#Circle properties
circle_x, circle_y = 200, 200
circle_radius = 20
circle_speed = 20
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#Boundary properties
# Boundary properties
BOUNDARY_X, BOUNDARY_Y = 100, 100
BOUNDARY_WIDTH, BOUNDARY_HEIGHT = 500, 500
BLACK = (0, 0, 0)


# Game loop
while True:
    screen.fill((0, 0, 0))  # Fill the screen with black
    
    # Display the current background
    screen.blit(backgrounds[background_index].background_list[0], (background2.x, background2.y))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        new_x, new_y = circle_x, circle_y
        if keys[pygame.K_a]:
            new_x -= circle_speed
        if keys[pygame.K_d]:
            new_x += circle_speed
        if keys[pygame.K_w]:
            new_y -= circle_speed
        if keys[pygame.K_s]:
            new_y += circle_speed

        # Handle keypress for moving between backgrounds
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:  # Move to the next background
                if (background_index < len(backgrounds) - 1):
                    background_index += 1
                    backgrounds[background_index]
            elif event.key == pygame.K_LEFT:  # Move to the previous background
                if (background_index > 0):
                    background_index -= 1
                    backgrounds[background_index]
            elif event.key == pygame.K_UP:
                background_index = 1
            elif event.key == pygame.K_DOWN:
                background_index = 0
            
            if (BOUNDARY_X + circle_radius <= new_x <= BOUNDARY_X + BOUNDARY_WIDTH - circle_radius and
            BOUNDARY_Y + circle_radius <= new_y <= BOUNDARY_Y + BOUNDARY_HEIGHT - circle_radius):
                circle_x, circle_y = new_x, new_y


    pygame.draw.rect(screen, BLACK, (BOUNDARY_X, BOUNDARY_Y, BOUNDARY_WIDTH, BOUNDARY_HEIGHT), 2)  # Draw boundary
    pygame.draw.circle(screen, BLUE, (circle_x, circle_y), circle_radius)
    pygame.display.update()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    

