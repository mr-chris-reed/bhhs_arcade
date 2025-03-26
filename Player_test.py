# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.
import pygame
from pygame.locals import *
from Asset_Reader import Asset_Reader
from Player import Player

# canvas variables
width = 1480 # adjust for width of canvas
height = 1000 # adjust for height of canvas

# frame rate
fps = 60
counter = 0

# colors
background_color = (255,0,255)

# initializing pygame, setting up the surface (canvas)
pygame.init()
canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption("Yo, is this this the guy!?!?!?!?!?!?!?!?!?! ;3") # add a caption for your canvas

# import assets
egg = Player(
            50,50,
            "assets/Eggsby_4.png", "assets/Eggsby.png", "assets/Eggsby_3.png", "assets/Eggsby_2.png", "assets/Eggsby-dance.png", "assets/Eggsby-attack.png", 
            2,2,2,2,4,6,1,1,1,1,2,5,5) 


# clock to set FPS
clock = pygame.time.Clock()

# variable to control state of entire game
running = True

# main game loop
while running:
    # paint the canvas with background color
    canvas.fill(background_color)

    counter += 1
    # poll for events
    for event in pygame.event.get():
        # if 'X' is clicked on the canvas
        if event.type == QUIT:
            running = False

    # get all keys that are currently pressed    
    keys = pygame.key.get_pressed()

    
    # check to see if any of the keys are w, a, s, or d
    # and perform an action
    if keys[pygame.K_w]:
        egg.up(counter)
    elif keys[pygame.K_s]:
        egg.down(counter)
    elif keys[pygame.K_a]:
        egg.left(counter)
    elif keys[pygame.K_d]:
        egg.right(counter)
    else:
        egg.last_sprite = egg.spritePicker(counter, egg.last_sprite_list)

    canvas.blit(egg.last_sprite, (egg.x_coord, egg.y_coord))
    
    pygame.display.update()
    clock.tick(fps)

# close pygame down
pygame.quit()
sys.exit()