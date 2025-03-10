import pygame
from Asset_Reader import Asset_Reader
screen = pygame.display.set_mode((1280, 1024))

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
        self.background = Asset_Reader("assets/CapyBarda_Start_Screen.png", 1, 1).get_asset_list()
        self.leaderboard = [] #Empty list of strings

    def drawStartScreen(self):
        screen.fill = self.background

            #We might need to make another function for blinking text.
    
    def draw_text(self, text, font_name, color, size, x, y, visible):
        if visible:
            pygame.font.init()
            font = pygame.font.Font(font_name if font_name else None, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect(center=(x, y))
            screen.blit(text_surface, text_rect)

    #Probably also needs to go in main bc we need to import joytick
    #def startGame(self):

    #def display_menu(self):

#class Leaderboard: