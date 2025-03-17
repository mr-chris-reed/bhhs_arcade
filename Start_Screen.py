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
        self.leaderboard = [] #Empty list of strings. Maybe not for the Alpha test if time does not allow.

    def drawStartScreen(self):
        screen.fill = self.background

    
    def draw_text(self, text, font_name, color, size, x, y, visible):
        if visible:
            pygame.font.init()
            font = pygame.font.Font(font_name if font_name else None, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect(center=(x, y))
            screen.blit(text_surface, text_rect)

    #Probably also needs to go in main bc we need to import joytick
    #def startGame(self):

### NOTES - 3/17/25 - should not have 2 classes in 1 file.  If you
# want to use the surface builder idea, place the code with a function
# inside this class
###
class surface_builder:

    def __init__(self, width, height, image, font_file, text1, text1_size, text2, text2_size):
        self.width = width
        self.height = height
        self.image = Asset_Reader(image, 1, 1).get_asset_list()
        self.font_file = font_file
        self.text1 = text1
        self.text1_size = text1_size
        self.text2 = text2
        self.text2_size = text2_size
        self.surface = None
    
    def generate_return_surface(self):
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.blit(self.image[0], (0,0))
        font1 = pygame.font.Font(self.font_file, self.text1_size)
        font2 = pygame.font.Font(self.font_file, self.text2_size)
        text1_surface = font1.render(self.text1, True, (255, 255, 255))
        text2_surface = font2.render(self.text2, True, (255, 255, 255))
        self.surface.blit(text1_surface, (self.width // 2, 100))
        self.surface.blit(text2_surface, (self.width // 2, 300))
        return self.surface

#class Leaderboard: