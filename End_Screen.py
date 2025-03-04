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
        self.backgroundGraphic = Asset_Reader("gameover.png", 1, 1).get_asset_list()
        self.credits = credits
        

    def goHome(self):
        pass

    def inputName(self):
        name = input("input your name")



    def drawEndScreen(self):
        #fills screen black
        screen.fill((0,0,0))
        
        #displays graphic
        screen.blit(self.backgroundGraphic, (0,0))
    
        #updates screen?
        pygame.display.flip()
        

   # screen drawing goes in main aparently

