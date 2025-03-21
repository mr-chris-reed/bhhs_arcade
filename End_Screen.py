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
        self.backgroundGraphic = Asset_Reader("assets/gameover.png", 1, 1).get_asset_list()
        self.credits = "Credits: eli the emu, tyler the phyler"
        self.input_box = pygame.Rect(200,150,140,32)
        self.name_box =  pygame.Rect(100,150,140,50)
        self.currentLetter = 0
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
        self.text = "" 
        self.font = pygame.font.SysFont("Arial", 32)  
        self.currentLetterString = "" 
        self.visible = True
        self.inputVisible=True
        self.name = ""
        self.vert_move = 0
        

    def goHome(self):
        pass

    def inputName(self,canvas):
        #the text box, eventually will display the letter taken from the handle imput
        pygame.draw.rect(canvas,(0,255,0),self.input_box,2)
        text_surface = self.font.render(self.currentLetterString, True, (0, 0, 0))  # Render the current text
        canvas.blit(text_surface, (self.input_box.x + 10, self.input_box.y + 10))  # Draw the text inside the box
        pygame.draw.rect(canvas,(255,0,0),self.name_box,2 ) # Draw the red name box
        name_surface = self.font.render(self.name, True, (0, 0, 0))  # Render the current text
        canvas.blit(name_surface, (self.name_box.x + 10, self.name_box.y + 10))  # Draw the text inside the box
        pygame.display.update()
        
    def handleInput(self, current_vert, canvas):
        #cycles through the alphabet when the arrows keys are moved and prints, will be changed once joystick is added
        if len(self.name) < 3:
                if self.vert_move != round(joysticks[0].get_axis(1)):
                    self.vert_move = round(joysticks[0].get_axis(1)) 
                    if self.vert_move > 0.5:  # If button is up, move to the previous letter
                        self.currentLetter = (self.currentLetter + 1) % len(self.alphabet)
                        self.currentLetterString = self.alphabet[self.currentLetter]
                        print(self.vert_move)
                    if self.vert_move < -0.5:  # If button is up, move to the previous letter
                        self.currentLetter = (self.currentLetter - 1) % len(self.alphabet)
                        self.currentLetterString = self.alphabet[self.currentLetter]
                        print(self.vert_move)
                if event.type == pygame.JOYBUTTONDOWN:
                    for joystick in joysticks:
                        if joystick.get_button(11):
                            self.name += self.currentLetterString

                print("Current input:" ,{self.name})

    def drawCredits(self,canvas):
        #will handle to drawing of credits, static for now, potentially add scrolling (if possible)
        text_surface2 = self.font.render(self.credits, True, (0, 0, 0))  # Render the current text
        canvas.blit(text_surface2, (self.input_box.x + 10, self.input_box.y + 10))  # Draw the text inside the box
        
    def drawEndScreen(self,canvas):
    # Fills screen black
        canvas.fill((100, 0, 0))

    # draw cred, if enter is pressed while creds are displayed it then displays the input name stuf
        #fills screen black
        canvas.fill((255,0,0))

        #displays graphic
        canvas.blit(self.backgroundGraphic[0], (0,0))

        if self.visible:
            self.drawCredits(canvas)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    # handles whether the credits are displayed or not
                    if event.key == pygame.K_RETURN and self.visible:
                        self.visible = False  # hid credits
                        self.inputVisible = True  # shows input box
                        self.text = "A" 
                    #working on this, will make the input name stuff invisible and display something else 
            
                       
          #draws input box and stuff if it is true
        if self.inputVisible:
            self.inputName(canvas)
            self.handleInput(canvas)