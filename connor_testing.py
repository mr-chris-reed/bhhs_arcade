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


# Flag to prevent continuous background switching
next_triggered = False
prev_triggered = False

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

    # Check if the circle is inside the boundary before updating position
    if (backgrounds[background_index].get_boundary_x() + circle_radius <= new_x <= backgrounds[background_index].get_boundary_x() + backgrounds[background_index].get_boundary_width() - circle_radius and
            backgrounds[background_index].get_boundary_y() + circle_radius <= new_y <= backgrounds[background_index].get_boundary_y() + backgrounds[background_index].get_boundary_height() - circle_radius):
        circle_x, circle_y = new_x, new_y

    # Check if the circle is inside the next zone
    if (backgrounds[background_index].get_next_x() <= circle_x <= backgrounds[background_index].get_next_x() + backgrounds[background_index].get_next_width() and
            backgrounds[background_index].get_next_y() <= circle_y <= backgrounds[background_index].get_next_y() + backgrounds[background_index].get_next_height()):
        if not next_triggered:  # Only change background if not already triggered
            if background_index < len(backgrounds) - 1:
                background_index += 1
            next_triggered = True
    else:
        next_triggered = False  # Reset flag when leaving the next box


# Check if the circle is inside the prev zone
    if (backgrounds[background_index].get_prev_x() <= circle_x <= backgrounds[background_index].get_prev_x() + backgrounds[background_index].get_prev_width() and
            backgrounds[background_index].get_prev_y() <= circle_y <= backgrounds[background_index].get_prev_y() + backgrounds[background_index].get_prev_height()):
        if not prev_triggered:  # Only change background if not already triggered
            if background_index > 0:
                background_index -= 1
            prev_triggered = True
    else:
        prev_triggered = False  # Reset flag when leaving the prev box


    # Draw boundary, trigger box, and circle
    pygame.draw.rect(screen, BLACK, (backgrounds[background_index].get_boundary_x(), backgrounds[background_index].get_boundary_y(), backgrounds[background_index].get_boundary_width(), backgrounds[background_index].get_boundary_height()), 2)  # Draw boundary
    pygame.draw.rect(screen, BLACK, (backgrounds[background_index].get_next_x(), backgrounds[background_index].get_next_y(), backgrounds[background_index].get_next_width(), backgrounds[background_index].get_next_height()), 2)  # Draw trigger box
    pygame.draw.circle(screen, BLUE, (circle_x, circle_y), circle_radius)
    pygame.display.update()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    

