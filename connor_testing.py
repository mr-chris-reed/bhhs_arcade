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

hell_background = Background("assets/hell_background.png", 1, 0, 0, 1.0, 100, 100, 1080, 820, 300, 300, 100, 100, 100, 100, 100, 100, False, False)
forest_path_background = Background("assets/forest_path_background.png", 1, 0, 0, 1.0, 100, 100, 1080, 820, 700, 500, 100, 100, 100, 100, 100, 100, False, False)
castle_background = Background("assets/castle_background.png", 1, 0, 0, 1.0, 100, 100, 1080, 820, 500, 500, 100 ,100, 100, 100, 100, 100, False, False)

backgrounds = [forest_path_background, hell_background, castle_background]
clock = pygame.time.Clock()

# Circle properties
circle_x, circle_y = 200, 200
circle_radius = 20
circle_speed = 20

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Display the current background
    screen.blit(backgrounds[Background.background_index].background_list[0], (backgrounds[Background.background_index].x, backgrounds[Background.background_index].y))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement logic (should be outside event loop for continuous movement)
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
    if (backgrounds[Background.background_index].boundary_x + circle_radius <= new_x <= backgrounds[Background.background_index].boundary_x + backgrounds[Background.background_index].boundary_width - circle_radius and
            backgrounds[Background.background_index].boundary_y + circle_radius <= new_y <= backgrounds[Background.background_index].boundary_y + backgrounds[Background.background_index].boundary_height - circle_radius):
        circle_x, circle_y = new_x, new_y

    Background.change_next_flag(backgrounds, circle_x, circle_y)
    Background.change_prev_flag(backgrounds, circle_x, circle_y)

    # Draw boundary, trigger box, and circle
    pygame.draw.rect(screen, (0, 0, 0), (backgrounds[Background.background_index].boundary_x, backgrounds[Background.background_index].boundary_y, backgrounds[Background.background_index].boundary_width, backgrounds[Background.background_index].boundary_height), 2)  # Draw boundary
    pygame.draw.rect(screen, (0, 0, 0), (backgrounds[Background.background_index].next_x, backgrounds[Background.background_index].next_y, backgrounds[Background.background_index].next_width, backgrounds[Background.background_index].next_height), 2)  # Draw trigger box
    pygame.draw.rect(screen, (0, 0, 0), (backgrounds[Background.background_index].prev_x, backgrounds[Background.background_index].prev_y, backgrounds[Background.background_index].prev_width, backgrounds[Background.background_index].prev_height), 2)  # Draw trigger box
    pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), circle_radius)

    pygame.display.update()  # Update the display

pygame.quit()
sys.exit() 