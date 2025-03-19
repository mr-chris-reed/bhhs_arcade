# imports for pygame
import pygame, sys
from pygame.locals import *
from Asset_Reader import Asset_Reader
# canvas variables
width = 1290 # adjust for width of canvas
height = 1024 # adjust for height of canvas
#colors
BLUE = (0,0,255)
RED = (255,0,0)
# frame rate
fps = 60
count = 0
previous_count = 0
#background image
#background_image = pygame.image.load('gameover.png')
# colors
background_color = (0,0,0)

# initializing pygame, setting up the surface (canvas)
pygame.init()
pygame.joystick.init()
joysticks = []

canvas = pygame.display.set_mode((width, height))
# background = pygame.Surface((width, height))

pygame.display.set_caption("<YOUR DISPLAY CAPTION GOES HERE (STRING)>") # add a caption for your canvas

class End_Screen:
    ###
    # NOTES: You might consider blitting the runtime, leaderboard, gameOverMessage
    # onto the backgroundGraphic before returning the end screen. We could make a
    # leaderboard class, which is responsible for holding an array of top scores.
    # The leaderboard could hold its data in a list of lists or dictionary.  We
    # would want it to hold position, player's initials, and time to complete.
    # We would also want a message to tell players how to get back to the start.
    ###
    def __init__(
            self,
            x,
            y,
            scale_factor,
            runtime,
            leaderboard,
            gameOverMessage,
            backgroundGraphic,
            credits,
        ):
        self.x = x
        self.y = y
        self.scale_factor = scale_factor
        self.runtime = runtime
        self.leaderboard = leaderboard
        self.gameOverMessage = gameOverMessage
        self.backgroundGraphic = Asset_Reader("assets/gameover.png", 1, 1).get_asset_list()
        self.credits = credits
        self.input_box = pygame.Rect(250,150,40,50)
        self.name_box =  pygame.Rect(100,150,140,50)
        self.currentLetter = 0 
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
        self.currentLetterString = "" 
        self.name = ""
        self.font = pygame.font.SysFont("Arial", 32)
        self.vert_move = 0
        ###
        self.background = pygame.Surface((1280, 1024))

    def goHome(self):
        pass

    def inputName(self,canvas):
        #the text box, eventually will display the letter taken from the handle imput
        pygame.draw.rect(canvas,BLUE,self.input_box,2 )
        text_surface = self.font.render(self.currentLetterString, True, (255, 255, 255))  # Render the current text
        canvas.blit(text_surface, (self.input_box.x + 10, self.input_box.y + 10))  # Draw the text inside the box
        pygame.draw.rect(canvas,RED,self.name_box,2 ) # Draw the red name box
        name_surface = self.font.render(self.name, True, (255, 255, 255))  # Render the current text
        canvas.blit(name_surface, (self.name_box.x + 10, self.name_box.y + 10))  # Draw the text inside the box
        pygame.display.update()
        

    def handleInput(self):
        #cycles through the alphabet when the arrows keys are moved and prints, will be changed once joystick is added
            if len(self.name) < 3:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:  # If Right Arrow key is pressed, move to the next letter
                        self.currentLetter = (self.currentLetter + 1) % len(self.alphabet)
                        self.currentLetterString = self.alphabet[self.currentLetter]
                    elif event.key == pygame.K_LEFT:  # If Left Arrow key is pressed, move to the previous letter
                        self.currentLetter = (self.currentLetter - 1) % len(self.alphabet)
                        self.currentLetterString = self.alphabet[self.currentLetter]
                    elif event.key == pygame.K_RETURN: # when enter is pressed, add it to the name instance variable
                        self.name += self.currentLetterString

                if self.vert_move != round(joysticks[0].get_axis(1)):
                    self.vert_move = round(joysticks[0].get_axis(1)) 
                    if self.vert_move > 0.5:  # If button is up, move to the previous letter
                        self.currentLetter = (self.currentLetter - 1) % len(self.alphabet)
                        self.currentLetterString = self.alphabet[self.currentLetter]
                        print(self.vert_move)
                    if self.vert_move < -0.5:  # If button is up, move to the previous letter
                        self.currentLetter = (self.currentLetter - 1) % len(self.alphabet)
                        self.currentLetterString = self.alphabet[self.currentLetter]
                        print(self.vert_move)

    def drawEndScreen(self):
        #fills screen black
        self.background.fill((0,0,0))

        #displays graphic
        self.background.blit(self.backgroundGraphic[0], (0,0))

        #updates screen?
        #pygame.display.flip()
        return self.background

end_Screen = End_Screen(
        x=0,
        y=0,
        scale_factor=1,
        runtime=0,
        leaderboard=None,
        gameOverMessage="Game Over",
        backgroundGraphic=None,  # Assuming you don't need a background for now
        credits="Some credits")

running = True

visible = True

while running:
    canvas.fill((255,255,255))
    count += 1
    canvas.blit(end_Screen.drawEndScreen(), (0, 0))
    
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        if event.type == QUIT:
           running = False

        if event.type == JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
            print("joystick?")

        end_Screen.handleInput()
        end_Screen.inputName(canvas)
    
    pygame.display.flip()
