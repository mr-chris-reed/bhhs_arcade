import pygame
from Asset_Reader import Asset_Reader

class Start_Screen:

    def __init__(self, startbutton, background, title, leaderboard, font, scale_factor):
        self.font = font
        font = pygame.font.SysFont('times new roman', 40)
        self.startbutton = startbutton
        startbutton = font.render("Start", True, (255, 255, 255))
        self.background = background
        background = (0, 0, 0) #For now
        self.title = title
        title = font.render("CapyBarda", True, (255, 255, 255))
        self.leaderboard = leaderboard
        leaderboard = [] #Empty list of strings

        def drawStartScreen(self):
            pass
            screen.fill = self.background

        def drawStartButton(self):
            pass

        def startGame(self):
            pass