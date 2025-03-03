import pygame
from Asset_Reader import Asset_Reader

class Start_Screen:

    def __init__(self, startmessage, background, title, leaderboard, font, scale_factor, x, y):
        self.x = x
        self.y = y
        self.scale_factor = scale_factor
        self.font = pygame.font.SysFont('times new roman', 40)
        self.startmessage = font.render("Press the A Button to Start!", True, (255, 255, 255))
        self.background = (0,0,0) #dosent work yet no file but thats the concept
        #Asset_Reader("Start_Screen.png", 1, 1)
        self.title = font.render("CapyBarda", True, (255, 255, 255))
        self.leaderboard = [] #Empty list of strings

    # prob has to go in main loop 
    # def drawStartScreen(self):
        #screen.fill = self.background

    def drawStartButton(self):
        pass

    #Probably also needs to go in main bc we need to import joytick
    #def startGame(self):