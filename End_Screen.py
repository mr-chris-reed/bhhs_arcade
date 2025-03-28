import pygame
from Asset_Reader import Asset_Reader

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
        ):
        self.x = x
        self.y = y
        self.scale_factor = scale_factor
        self.runtime = runtime
        self.leaderboard = leaderboard
        self.gameOverMessage = gameOverMessage
      # self.backgroundGraphic = Asset_Reader("assets/gameover.png", 1, 1).get_asset_list()
        self.credits = "Cole Shook, Colton Chappell, Connor James, Rowan Pederson, Tyler Pham, Nicholas Winkler, and Eli Ulman"
        self.input_box = pygame.Rect((1280 //2)-75,280,100,100) #intial letter cycling box
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
        pygame.draw.rect(canvas, (255,255,255), self.input_box, 2)  # makes box around the initial cycling
        text_surface = self.font.render(self.currentLetterString, True, (255,255,255))  # cycling letter
    
    # Calculate the x and y positions to center the letter inside the input box
        letter_width = text_surface.get_width()
        letter_height = text_surface.get_height()
        letter_x = self.input_box.x + (self.input_box.width - letter_width) // 2  # Center the letter horizontally
        letter_y = self.input_box.y + (self.input_box.height - letter_height) // 2  # Center the letter vertically
        canvas.blit(text_surface, (letter_x, letter_y))  # Draw the letter inside the box

    # Draw the name box
        pygame.draw.rect(canvas, (255,255,255), self.name_box, 1)  # Draw the name box outline
        name_surface = self.font.render(self.name, True, (255,255,255))  # text for the name
    
    # Calculate the x and y positions to center the name inside the name box
        name_width = name_surface.get_width()
        name_height = name_surface.get_height()
        name_x = self.name_box.x + (self.name_box.width - name_width) // 2  # Center the name horizontally
        name_y = self.name_box.y + (self.name_box.height - name_height) // 2  # Center the name vertically
        canvas.blit(name_surface, (name_x, name_y))  # Draw the name inside the box
    
        pygame.display.update()

        
    def handleInput(self,canvas, joysticks):
        keys=pygame.key.get_pressed()
        #cycles through the alphabet when the arrows keys are moved and prints, will be changed once joystick is added
        if len(self.name) < 3:
                if self.vert_move != round(joysticks[0].get_axis(0)):
                    self.vert_move = round(joysticks[0].get_axis(0)) 
                    if self.vert_move > 0.5:  # If button is up, move to the previous letter
                        self.currentLetter = (self.currentLetter + 1) % len(self.alphabet)
                        self.currentLetterString = self.alphabet[self.currentLetter]
                        print(self.vert_move)
                    if self.vert_move < -0.5:  # If button is up, move to the previous letter
                        self.currentLetter = (self.currentLetter - 1) % len(self.alphabet)
                        self.currentLetterString = self.alphabet[self.currentLetter]
                        print(self.vert_move)
                    if joysticks[0].get_button(11):
                        self.name += self.currentLetterString
                        print("Current input:" ,self.name)
                    if keys[pygame.K_a]:
                        self.name += self.currentLetterString
        if len(self.name)==3 :
            if keys[pygame.K_a]:
                    self.inputVisible = False  # Hide the input

                    

    def drawCredits(self,canvas):
        #will handle to drawing of credits, static for now, potentially add scrolling (if possible)
        text_surface2 = self.font2.render(self.credits, True, (255,255,255))  #draws the credits
        canvas.blit(text_surface2, (250,250))  ##shows up
        
    def drawEndScreen(self, canvas, joysticks):
    # Fills screen black
        canvas.fill((0,0,0))

    # draw cred, if enter is pressed while creds are displayed it then displays the input name stuf
        if self.visible:
            self.drawCredits(canvas)
            for event in pygame.event.get():
                   
                if event.type == pygame.KEYDOWN:
                    # handles whether the credits are displayed or not
                    if event.key == pygame.K_RETURN and self.visible:
                        self.visible = False  # hid credits
                        self.inputVisible = True  # shows input box   
                        self.currentLetterString = "A"
                
                
          #draws input box and stuff if it is true
        if self.inputVisible:
            self.inputName(canvas)
            self.handleInput(canvas,joysticks)