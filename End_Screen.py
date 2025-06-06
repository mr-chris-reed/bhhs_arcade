import pygame
from Asset_Reader import Asset_Reader
from Leaderboard import Leaderboard

class End_Screen:
    ###
    # NOTES: You might consider blitting the runtime, leaderboard, gameOverMessage
    # onto the backgroundGraphic before returning the end screen. We could make a
    # leaderboard class, which is responsible for holding an array of top scores.
    # The leaderboard could hold its data in a list of lists or dictionary.  We
    # would want it to hold position, player's initials, and time to complete.
    # We would also want a message to tell players how to get back to the start.
    ###

    Leaderboard = Leaderboard()
    updated_leaderboard = ''
    
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
        self.credits = ["Computer Science Department:", "Colton Chappell", "Connor James", "Rowan Pedersen", "Tyler Pham","Cole Shook", "Eli Ulman","Nick Winkler","Mr. Reed","","Art Department:",  "James Dzikowski", "Isobel Hein", "Eliza Melcher", "Archer Scaffidi", "Mrs. Greiss", "",  "Music Department:", "Colin Seidel", "Dylan Teel",  "Mr. Rabenold", "", "Woodshop:", "Mr. Schmidt","Mr. Sheeler","","Graphic Design:","Mr. Lundy" ,"", "Special Thanks to the Brandywine Heights Education Foundation"]
        self.input_box = pygame.Rect((1280 //2)-75,280,100,100) #intial letter cycling box
        self.name_box =  pygame.Rect(450,480,335,125) #initals box 
        self.instruction_box = pygame.Rect(240, 50, 800, 100)
        self.currentLetter = 0
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
        self.text = "" 
        self.font2 = pygame.font.Font("fonts/PirataOne-Regular.ttf", 50)
        self.font = pygame.font.Font("fonts/PirataOne-Regular.ttf", 100)
        self.currentLetterString = "A"
        self.visible = True
        self.inputVisible=False
        self.name = ""        
        self.vert_move = 0
        self.vert_move2 = 0
        self.button_move = 0
        self.back_button_move = 0
        self.hasBeenPressedOnce = False
        self.pressedVisiblity=False
        
    def goHome(self):
        pass

    def inputName(self, canvas):
        pygame.draw.rect(canvas, (255,255,255), self.instruction_box, 1)
        instruction_surface = self.font2.render("use the joystick to write your name", True, (255,255,255))
        instruction_width = instruction_surface.get_width()
        instruction_height = instruction_surface.get_height()
        instruction_x = self.instruction_box.x + (self.instruction_box.width - instruction_width) // 2  # Center the name horizontally
        instruction_y = self.instruction_box.y + (self.instruction_box.height - instruction_height) // 2  # Center the name vertically
        canvas.blit(instruction_surface, (instruction_x, instruction_y))  # Draw the name inside the box
    
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
    
        

        
    def handleInput(self,canvas, joysticks, hud):
        # keys=pygame.key.get_pressed()
        #cycles through the alphabet when the arrows keys are moved and prints, will be changed once joystick is added
        if len(self.name) < 3:
                if self.vert_move != round(joysticks[0].get_axis(0)):
                    self.vert_move = round(joysticks[0].get_axis(0)) 
                    if self.vert_move > 0.5:  # If button is up, move to the previous letter
                        self.currentLetter = (self.currentLetter + 1) % len(self.alphabet)
                        self.currentLetterString = self.alphabet[self.currentLetter]
                        
                        
                    if self.vert_move < -0.5:  # If button is up, move to the previous letter
                        self.currentLetter = (self.currentLetter - 1) % len(self.alphabet)
                        self.currentLetterString = self.alphabet[self.currentLetter]
                        
                if self.button_move != round(joysticks[0].get_button(10)):
                    self.button_move = round(joysticks[0].get_button(10))
                    if self.button_move > 0.5 and self.hasBeenPressedOnce ==False:
                        self.hasBeenPressedOnce = True
                    elif self.button_move > 0.5 and self.hasBeenPressedOnce ==True:
                        self.name += self.currentLetterString
                if self.back_button_move != round(joysticks[0].get_button(11)):
                    self.back_button_move = round(joysticks[0].get_button(11))
                    if self.back_button_move > 0.5 and self.hasBeenPressedOnce == False:
                        self.hasBeenPressedOnce = True
                    elif self.back_button_move > 0.5 and self.hasBeenPressedOnce == True:
                        self.name = self.name[:-1]
        elif len(self.name)==3:
            if self.back_button_move != round(joysticks[0].get_button(11)):
                    self.back_button_move = round(joysticks[0].get_button(11))
                    if self.back_button_move > 0.5 and self.hasBeenPressedOnce == False:
                        self.hasBeenPressedOnce = True
                    elif self.back_button_move > 0.5 and self.hasBeenPressedOnce == True:
                        self.name = self.name[:-1]
            if self.button_move != round(joysticks[0].get_button(10)):
                self.button_move = round(joysticks[0].get_button(10))
                if self.button_move > 0.5 and self.pressedVisiblity==False:
                    self.pressedVisiblity = True            
                    self.inputVisible = False
                    name = self.name
                    Leaderboard.add_to_leaderboard(self.Leaderboard, name, int(hud.score.replace(".", "")))
                    ###
                    self.name = ''
                    ###
                    
               

                    



    def drawCredits(self, canvas):
        HEIGHT = 1000
        WIDTH = 1280
        #makes it so that the ceredits start at the botto mof the screen 
        if not hasattr(self, 'vert_move2_initialized') or not self.vert_move2_initialized:
            self.vert_move2 = HEIGHT  # Start at bottom of screen
            self.vert_move2_initialized = True

        y_pos = self.vert_move2
        #canvas.get_width()  # Get canvas width to center horizontally
      #  y_pos = self.vert_move2  # Track vertical scroll position

        # height for cred
        credit_height = len(self.credits) * 60  

        for i, credit in enumerate(self.credits):
            text_surface = self.font2.render(credit, True, (255, 255, 255))
            text_width = text_surface.get_width()
            #centers text in the middle of the screen
            x_pos = (WIDTH - text_width) // 2
            #draws text
            canvas.blit(text_surface, (x_pos, y_pos + (i * 60)))  
        # scroll upwards
        self.vert_move2 -= 9  
        # continously scrolling
        if y_pos + credit_height < 0:
            self.vert_move2 = HEIGHT

        
        
    def drawEndScreen(self, canvas, joysticks, hud):
    # Fills screen black
        
        canvas.fill((0,0,0))
        
    # draw cred, if enter is pressed while creds are displayed it then displays the input name stuf
        if self.visible:
            self.drawCredits(canvas)
    
        if (joysticks[0].get_button(10) == 1 or joysticks[0].get_button(11) == 1 or joysticks[0].get_button(8) == 1 or joysticks[0].get_button(9) == 1 ) and self.visible:
            self.visible = False  # hide credits
            pygame.time.delay(200)
            self.inputVisible = True  # shows input box   
            

          #draws input box and name box if inputvisilbe is set to true
        if self.inputVisible:
            self.inputName(canvas)
            self.handleInput(canvas,joysticks, hud)
        
