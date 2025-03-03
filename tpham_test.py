# imports for pygame
import pygame, sys
from pygame.locals import *

# canvas variables
width = 1920 # adjust for width of canvas
height =1080 # adjust for height of canvas

# frame rate
fps = 60
#background image
background_image = pygame.image.load('gameover.png')
# colors
background_color = (255,255,255)

# initializing pygame, setting up the surface (canvas)
pygame.init()
canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption("<YOUR DISPLAY CAPTION GOES HERE (STRING)>") # add a caption for your canvas

class endscreen:
    def __init__(self,backgroundGraphic):
        #self.runtime = runtime
       # self.leaderboard = leaderboard
        #self.homeButton = homeButton
        self.gameOverMessage = "gane"
        self.backgroundGraphic = backgroundGraphic
        #self.credits = credits

    def goHome(self):
        pass

    def inputName(self):
        pass

    def drawEndScreen(self):
        #fills screen black
        canvas.fill((0,0,0))
        
        #displays graphic
        canvas.blit(self.backgroundGraphic, (0,0))

        #update screen
        pygame.canvas.flip()

end_screen = endscreen(backgroundGraphic=background_image)
# import assets
sprite_sheet = pygame.image.load("Eggsby_2.png").convert_alpha() # add the path/name of your sprite sheet file

# get details about individual sprites
total_sprites = 2 # code the number of sprite images your sprite sheet has
sprite_sheet_width = sprite_sheet.get_rect().width
sprite_sheet_height = sprite_sheet.get_rect().height


# adjust sprite size
sprite_scale_factor = 2.0
sprite_sheet_width = sprite_sheet_width * sprite_scale_factor
sprite_sheet_height = sprite_sheet_height * sprite_scale_factor
sprite_sheet = pygame.transform.scale(sprite_sheet, (sprite_sheet_width, sprite_sheet_height))
sprite_sheet_width = sprite_sheet.get_rect().width
sprite_sheet_height = sprite_sheet.get_rect().height
sprite_width = sprite_sheet_width // total_sprites
sprite_height = sprite_sheet_height

# define initial x and y position of sprite
sprite_x_pos = 0
sprite_y_pos = 0
sprite_x_delta = 10
sprite_y_delta = 10

# load sprite sheet into list
sprite_list = []
for i in range(total_sprites):
    rect = pygame.Rect(i * sprite_width, 0, sprite_width, sprite_height)
    image = sprite_sheet.subsurface(rect)
    sprite_list.append(image)

# sprite picker function for animation
sprite_index = 0
counter = 0
def spritePicker():
    global sprite_index
    if counter % 20 == 0: # adjust the number to the right of the "%" symbol to increase/decrease animation speed
        if sprite_index == total_sprites - 1:
            sprite_index = 0
        else:
            sprite_index += 1

# clock to set FPS
clock = pygame.time.Clock()
wall = pygame.Rect(300, 200, 200, 50) 
# variable to control state of entire game
running = True
#game over
game=False
# main game loop
while running:
    # paint the canvas with background color
    canvas.fill(background_color)

    # poll for events
    for event in pygame.event.get():
        # if 'X' is clicked on the canvas
        if event.type == QUIT:
            running = False
    pygame.draw.rect(canvas, (0, 0, 0), wall)
    # get all keys that are currently pressed    
    keys = pygame.key.get_pressed()

    # check to see if any of the keys are w, a, s, or d
    # and perform an action
    if keys[pygame.K_w]:
        sprite_y_pos -= sprite_y_delta
    if keys[pygame.K_s]:
        sprite_y_pos += sprite_y_delta
    if keys[pygame.K_a]:
        sprite_x_pos -= sprite_x_delta
    if keys[pygame.K_d]:
        sprite_x_pos += sprite_x_delta
    if sprite_x_pos > 1920:
        sprite_x_pos=0
    if sprite_x_pos < 0:
        sprite_x_pos=1920
    if sprite_y_pos > 1080:
        sprite_y_pos=0
    if sprite_y_pos < 0:
        sprite_y_pos=1080
    if keys[pygame.K_h]:
        pygame.quit()
        sys.exit()
    canvas.blit(sprite_list[sprite_index], (sprite_x_pos, sprite_y_pos))
    spritePicker()
    pygame.display.update()
    counter += 1
    clock.tick(fps)
    # Check for collision with the wall and stop movement if there's a collision
    sprite_rect = pygame.Rect(sprite_x_pos, sprite_y_pos, sprite_width, sprite_height)
    if sprite_rect.colliderect(wall):
        print("1")
        end_screen.drawEndScreen()
        if keys[pygame.K_a]:
            sprite_x_pos += sprite_x_delta  # Prevent moving left into the wall
        if keys[pygame.K_d]:
             sprite_x_pos -= sprite_x_delta  # Prevent moving right into the wall
        if keys[pygame.K_w]:
            sprite_y_pos += sprite_y_delta  # Prevent moving up into the wall
        if keys[pygame.K_s]:
            sprite_y_pos -= sprite_y_delta   # Prevent moving down into the wall
       #canvas.blit(bg_image, (0, 0))
        #pygame.display.update()
     
# close pygame down
pygame.quit()
sys.exit()