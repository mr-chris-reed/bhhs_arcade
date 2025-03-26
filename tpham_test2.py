# imports for pygame
import pygame, sys
from pygame.locals import *

# canvas variables
width = 1280 # adjust for width of canvas
height =1024 # adjust for height of canvas
#colors
BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
# frame rate
fps = 60
#background image
#background_image = pygame.image.load('gameover.png')
# colors
background_color = (0,0,0)
vert_move=0
# initializing pygame, setting up the surface (canvas)
pygame.init()
canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption("<YOUR DISPLAY CAPTION GOES HERE (STRING)>") # add a caption for your canvas
#gets the key
centerx = (1280 //2)-75
centery = (1024 - 32) // 2
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
      # self.backgroundGraphic = Asset_Reader("assets/gameover.png", 1, 1).get_asset_list()
        self.credits = "Cole, Colton, Connor, Rowan, Tyler, Nick, eli"
        self.input_box = pygame.Rect(centerx,280,100,100) #intial letter cycling box
        self.name_box =  pygame.Rect(500,480,235,125) #initals box 
        self.currentLetter = 0
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
        self.text = "" 
        self.font2 = pygame.font.SysFont("Arial",50)
        self.font = pygame.font.SysFont("Arial", 100)  
        self.currentLetterString = "" 
        self.visible = True
        self.inputVisible=False
        self.name = ""
        
        self.vert_move = 0
    def goHome(self):
        pass

    def inputName(self, canvas):
    # Draw the input box
        pygame.draw.rect(canvas, WHITE, self.input_box, 2)  # makes box around the initial cycling
        text_surface = self.font.render(self.currentLetterString, True, WHITE)  # cycling letter
    
    # Calculate the x and y positions to center the letter inside the input box
        letter_width = text_surface.get_width()
        letter_height = text_surface.get_height()
        letter_x = self.input_box.x + (self.input_box.width - letter_width) // 2  # Center the letter horizontally
        letter_y = self.input_box.y + (self.input_box.height - letter_height) // 2  # Center the letter vertically
        canvas.blit(text_surface, (letter_x, letter_y))  # Draw the letter inside the box

    # Draw the name box
        pygame.draw.rect(canvas, WHITE, self.name_box, 1)  # Draw the name box outline
        name_surface = self.font.render(self.name, True, WHITE)  # text for the name
    
    # Calculate the x and y positions to center the name inside the name box
        name_width = name_surface.get_width()
        name_height = name_surface.get_height()
        name_x = self.name_box.x + (self.name_box.width - name_width) // 2  # Center the name horizontally
        name_y = self.name_box.y + (self.name_box.height - name_height) // 2  # Center the name vertically
        canvas.blit(name_surface, (name_x, name_y))  # Draw the name inside the box
    
        pygame.display.update()

        
    def handleInput(self,canvas):
        keys=pygame.key.get_pressed()
        
        #cycles through the alphabet when the arrows keys are moved and prints, will be changed once joystick is added
        for event in pygame.event.get():
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                        if len(self.name) > 0:  # Only delete if there's at least one character in the name
                            self.name = self.name[:-1]
                        
                if abs(vert_move) > 0.5:
                    if vert_move > 0.5:  # If button is up, move to the previous letter
                        self.currentLetter = (self.currentLetter - 1) % len(self.alphabet)
                        self.currentLetterString = self.alphabet[self.currentLetter]
                        print(vert_move)
                    if vert_move < 0.5:  # If button is up, move to the previous letter
                        self.currentLetter = (self.currentLetter - 1) % len(self.alphabet)
                        self.currentLetterString = self.alphabet[self.currentLetter]
                        print(vert_move)
                print("Current input:" ,{self.name})
        if len(self.name)==3 :
            if keys[pygame.K_a]:
                    self.inputVisible = False  # Hide the input

                    

    def drawCredits(self,canvas):
        #will handle to drawing of credits, static for now, potentially add scrolling (if possible)
        text_surface2 = self.font2.render(self.credits, True, WHITE)  #draws the credits
        canvas.blit(text_surface2, (250,250))  ##shows up
        
    def drawEndScreen(self):
    # Fills screen black
        canvas.fill(BLACK)

    # draw cred, if enter is pressed while creds are displayed it then displays the input name stuf
        if self.visible:
            end_Screen.drawCredits(canvas)
            for event in pygame.event.get():
                   
                if event.type == pygame.KEYDOWN:
                    # handles whether the credits are displayed or not
                    if event.key == pygame.K_RETURN and self.visible:
                        self.visible = False  # hid credits
                        self.inputVisible = True  # shows input box   
                        self.currentLetterString = "A"
                
                
          #draws input box and stuff if it is true
        if self.inputVisible:
            end_Screen.inputName(canvas)
            end_Screen.handleInput(canvas)
    pygame.display.update() 



end_Screen = End_Screen( x=0,y=0,scale_factor=1,runtime=0,leaderboard=None,gameOverMessage="Game Over",backgroundGraphic=None,credits="cred")  # Assuming you don't need a background for now credits='')
running = True

keys = pygame.key.get_pressed()
while running:
    end_Screen.drawEndScreen()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
