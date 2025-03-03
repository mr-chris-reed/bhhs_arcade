

import pygame


class End_Screen:
    def __init__(self, runtime, leaderboard, homeButton, gameOverMessage, backgroundGraphic, credits):
        self.runtime = runtime
        self.leaderboard = leaderboard
        self.homeButton = homeButton
        self.gameOverMessage = gameOverMessage
        self.backgroundGraphic = backgroundGraphic
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
        
