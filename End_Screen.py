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
            credits,
        ):
        self.x = x
        self.y = y
        self.scale_factor = scale_factor
        self.runtime = runtime
        self.leaderboard = leaderboard
        self.gameOverMessage = gameOverMessage
      # self.backgroundGraphic = Asset_Reader("assets/gameover.png", 1, 1).get_asset_list()
        self.credits = ""
        self.input_box = pygame.Rect(200,150,140,32)
        self.currentLetter = 0 
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
        self.text = "" 
        self.font = pygame.font.SysFont("Arial", 32)  
    def goHome(self):
        pass

    def inputName(self,canvas):
        #the text box, eventually will display the letter taken from the handle imput
        pygame.draw.rect(canvas,BLUE,self.input_box,2 )
        text_surface = self.font.render(self.text, True, (0, 0, 0))  # Render the current text
        canvas.blit(text_surface, (self.input_box.x + 10, self.input_box.y + 10))  # Draw the text inside the box
        pygame.display.update()
        

    def handleInput(self,canvas):
        #cycles through the alphabet when the arrows keys are moved and prints, will be changed once joystick is added
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:  # If Right Arrow key is pressed, move to the next letter
                    self.currentLetter = (self.currentLetter + 1) % len(self.alphabet)
                elif event.key == pygame.K_LEFT:  # If Left Arrow key is pressed, move to the previous letter
                    self.currentLetter = (self.currentLetter - 1) % len(self.alphabet)
                
                self.text = self.alphabet[self.currentLetter]

                print(f"Current input: {self.text}")

    def drawCredits(self,canvas):
        #will handle to drawing of credits, static for now, potentially add scrolling (if possible)
        text_surface2 = self.font.render(self.credits, True, (0, 0, 0))  # Render the current text
        canvas.blit(text_surface2, (self.input_box.x + 10, self.input_box.y + 10))  # Draw the text inside the box
    
    ###
    # NOTES - 3/17/25: I think the event loop and the pygame.display.update() belong in the main file,
    # which is currently your chappell_testing and tpham_test files.  I think you are on the
    # right track for the drawEndScreen function, but make it build a composite surface with
    # everything you want on the end screen and return it to the calling code.
    ###
    def drawEndScreen(self):
        #fills screen black
        canvas.fill((100,0,0))
        #draws credits, if a button is pressed displays input name selection
        if self.visible == True:
            end_Screen.drawCredits(canvas)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.visible=False
                    self.inputVisible = True
                    self.text="A"
        if self.inputVisible == True:
            end_Screen.inputName(canvas)
            end_Screen.handleInput(canvas)
        pygame.display.update()

