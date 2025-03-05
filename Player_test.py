# Main file where pygame game loop will exist.
# We can use this file to declare and modify 
# global variables and create objects and test
# our code.

import pygame
from pygame.locals import *
from Asset_Reader import Asset_Reader
from End_Screen import End_Screen
from Start_Screen import Start_Screen
from Player import Player

# canvas variables
width = 1480 # adjust for width of canvas
height = 1000 # adjust for height of canvas

# frame rate
fps = 60

# colors
background_color = (255,0,255)

# initializing pygame, setting up the surface (canvas)
pygame.init()
canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption("maD egg lol") # add a caption for your canvas

# import assets
egg = Player(50,50, eggsby_4.png, eggsby.png, eggsby_3.png, eggsby_2.png, eggsby_dance.png, eggsby_attack.png, 2,2,2,2,4,6,5,5) 

# clock to set FPS
clock = pygame.time.Clock()

# variable to control state of entire game
running = True

# main game loop
while running:
    # paint the canvas with background color
    canvas.fill(background_color)

    # poll for events
    for event in pygame.event.get():
        # if 'X' is clicked on the canvas
        if event.type == QUIT:
            running = False

    # get all keys that are currently pressed    
    keys = pygame.key.get_pressed()

    """
    # check to see if any of the keys are w, a, s, or d
    # and perform an action
    if keys[pygame.K_w]:

        egg.y_coord -= 10
        i=-1
        for i in range(up_list.length):

        egg.up_list
    
    if keys[pygame.K_s]:
        egg.y_coord += 10
    if keys[pygame.K_a]:
        egg.x_coord -= 10
    if keys[pygame.K_d]:
        egg.x_coord += 10
     if keys[pygame.K_d]:
        egg.x_coord += 10
    """

# close pygame down
pygame.quit()
sys.exit()