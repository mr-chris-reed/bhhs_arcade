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

hell_background = Background("assets/hell_background.png", 1, 0, 0, 1.0, 100, 100, 1080, 820, 300, 300, 100, 100)
forest_path_background = Background("assets/forest_path_background.png", 1, 0, 0, 1.0, 100, 100, 1080, 820, 300, 300, 100, 100)
background2 = Background("assets/background2.png", 1, 0, 0, 1.0, 100, 100, 1080, 820, 300, 300, 100 ,100)

backgrounds = [forest_path_background, hell_background, background2]
background_index = 0

clock = pygame.time.Clock()

# Circle properties
square_x, square_y = 200, 200
square_width = 20
square_height = 20
square_speed = 20

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Display the current background
    screen.blit(backgrounds[background_index].background_list[0], (background2.x, background2.y))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement logic (should be outside event loop for continuous movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        square_x -= square_speed
        if (not Background.check_if_in_bounds(backgrounds, square_x, square_y, square_width, square_height)):
            square_x = backgrounds[Background.background_index].boundary_x
    if keys[pygame.K_d]:
        square_x += square_speed
        if (not Background.check_if_in_bounds(backgrounds, square_x, square_y, square_width, square_height)):
            square_x = backgrounds[Background.background_index].boundary_x + backgrounds[Background.background_index].boundary_width - square_width
    if keys[pygame.K_w]:
        square_y -= square_speed
        if (not Background.check_if_in_bounds(backgrounds, square_x, square_y, square_width, square_height)):
            square_y = backgrounds[Background.background_index].boundary_y
    if keys[pygame.K_s]:
        square_y += square_speed
        if (not Background.check_if_in_bounds(backgrounds, square_x, square_y, square_width, square_height)):
            square_y = backgrounds[Background.background_index].boundary_y + backgrounds[Background.background_index].boundary_height - square_height

    # Check if the circle is inside the boundary before updating position
    print(Background.check_if_in_bounds(backgrounds, square_x, square_y, square_width, square_height))
        
    

    Background.change_next_flag(backgrounds, square_x, square_y)
    Background.change_prev_flag(backgrounds, square_x, square_y)

    # Draw boundary, trigger box, and circle
    #Remove these to make boundaries invisible
    pygame.draw.rect(screen, (0, 0, 0), (backgrounds[Background.background_index].boundary_x, backgrounds[Background.background_index].boundary_y, backgrounds[Background.background_index].boundary_width, backgrounds[Background.background_index].boundary_height), 2)  # Draw boundary
    pygame.draw.rect(screen, (0, 0, 0), (backgrounds[Background.background_index].next_x, backgrounds[Background.background_index].next_y, backgrounds[Background.background_index].next_width, backgrounds[Background.background_index].next_height), 2)  # Draw trigger box
    pygame.draw.rect(screen, (0, 0, 0), (backgrounds[Background.background_index].prev_x, backgrounds[Background.background_index].prev_y, backgrounds[Background.background_index].prev_width, backgrounds[Background.background_index].prev_height), 2)  # Draw trigger box
    
    # Draw player
    pygame.draw.rect(screen, (0, 0, 255), (square_x, square_y, square_width, square_height), 2)

    pygame.display.update()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    

