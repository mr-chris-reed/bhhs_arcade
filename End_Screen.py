import pygame
from Asset_Reader import Asset_Reader

class End_Screen:
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
        pass



    def drawEndScreen(self):
        #fills screen black
        screen.fill((0,0,0))
        
        #displays graphic
        screen.blit(self.backgroundGraphic, (0,0))
    
        #updates screen?
        pygame.display.flip()
        

   # screen drawing goes in main aparently

