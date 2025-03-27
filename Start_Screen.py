import pygame
from Asset_Reader import Asset_Reader

screen = pygame.display.set_mode((1280, 1024))

class Start_Screen:

    def __init__(self, background, leaderboard, scale_factor, x, y, height, width):
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
        self.background = Asset_Reader(background, 1, scale_factor).get_asset_list()
        self.leaderboard = leaderboard
        self.height = height
        self.width = width
        self.surface = None

    def draw_text(self, text, font_name, color, size, x, y, counter, i): # i = 1 for solid text
        if i == 1:
            font = pygame.font.Font(font_name if font_name else None, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect(center=(x, y))
            self.surface.blit(text_surface, text_rect)
        
        elif counter % i > 1 and counter % i < 15:
            font = pygame.font.Font(font_name if font_name else None, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect(center=(x, y))
            self.surface.blit(text_surface, text_rect)

    def generate_return_surface(self, counter):
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.blit(self.background[0], (self.x,self.y))
        self.draw_text("Press Any Button To Start!", "fonts/PirataOne-Regular.ttf", (255,255,255), 45, 640, 800, counter, 30) # bigger numbers for i = slower flash
        self.draw_leaderboard("fonts/PirataOne-Regular.ttf", (255, 255, 255), 40, 100, 25, counter)
        return self.surface

    def draw_leaderboard(self, font_name, color, size, x, y, counter):
        self.draw_text("Leaderboard:", font_name, color, size, x, y, counter, 1)
        for player in self.leaderboard:
            x -= 70
            y += 50
            self.draw_text(player[0], font_name, color, size, x, y, counter, 1)
            self.draw_text(player[1], font_name, color, size, x + 70, y, counter, 1)
            x += 70

