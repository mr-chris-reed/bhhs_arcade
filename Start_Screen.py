import pygame
from Asset_Reader import Asset_Reader

class Start_Screen:

    def __init__(self, startmessage, background, title, leaderboard, font, scale_factor, x, y):
        ###
        # NOTES for constructor: You might consider blitting the startmessage, title, and leaderboard
        # on to the background before returning the background.
        # You might consider getting a Google font and pass in the .ttf file for the font parameter.
        # For the font, you will need to create a "Font" object, like this
        # t = Font(font, font_size, title)
        # You might consider creating a Leaderboard class that holds the data in a sorted list.
        # If you add 1 to the index of the list, you can get the ranking 1, 2, 3, etc.
        ###
        self.x = x
        self.y = y
        self.scale_factor = scale_factor
        #self.font = pygame.font.SysFont('times new roman', 40)
        #self.startmessage = font.render("Press the A Button to Start!", True, (255, 255, 255))
        self.background = Asset_Reader("bhhs_arcade/assets/gameover.png", 1, 1).get_asset_list()
        #self.title = font.render("CapyBarda", True, (255, 255, 255))
        self.leaderboard = [] #Empty list of strings

    def drawStartScreen(self):
        screen.fill = self.background

    def drawStartMessage(self):
        pass

    #Probably also needs to go in main bc we need to import joytick
    #def startGame(self):