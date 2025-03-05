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
        self.backgroundGraphic = Asset_Reader("assets/gameover.png", 1, 1).get_asset_list()
        self.credits = credits
        self.input_box = pygame.Rect(200,150,140,32)
        self.text = ''
        
    def goHome(self):
        pass

    def inputName(self):
        name = input("input your name")
        alphabet = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
        pygame.draw.rect(canvas,BLUE,self.input_box,2 )
        pygame.display.update()
        
    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                self.text = (key_name)
            print(key_name)
    def drawEndScreen(self):
        #fills screen black
        screen.fill((0,0,0))
        
        #displays graphic
        screen.blit(self.backgroundGraphic, (0,0))
    
        #updates screen?
        pygame.display.flip()
        

   # screen drawing goes in main aparently

