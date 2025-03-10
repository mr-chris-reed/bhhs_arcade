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
egg = Player(
            50,50,
            "assets/Eggsby_4.png", "assets/Eggsby.png", "assets/Eggsby_3.png", "assets/Eggsby_2.png", "assets/Eggsby-dance.png", "assets/Eggsby-attack.png", 
            2,2,2,2,4,6,1,5,5) 

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

    
    # check to see if any of the keys are w, a, s, or d
    # and perform an action
    if keys[pygame.K_w]:
        egg.sprite_index = 0
        for i in range egg.up_list.length:
            canvas.blit(egg.up_list[egg.sprite_picker()], (x_coord, y_coord))
        egg.up()
    if keys[pygame.K_s]:
        egg.sprite_index = 0
        for i in range egg.down_list.length:
            canvas.blit(egg.down_list[egg.sprite_picker()], (x_coord, y_coord))
        egg.down()
    if keys[pygame.K_a]:
        egg.sprite_index = 0
        for i in range egg.left_list.length:
            canvas.blit(egg.left_list[egg.sprite_picker()], (x_coord, y_coord))
        egg.left()
    if keys[pygame.K_d]:
        egg.sprite_index = 0
        for i in range egg.right_list.length:
            canvas.blit(egg.right_list[egg.sprite_picker()], (x_coord, y_coord))
        egg.right()

# close pygame down
pygame.quit()
sys.exit()