import pygame, sys, time
from Asset_Reader import Asset_Reader
from Background import Background

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
        self.scale_factor = scale_factor
        self.background = Asset_Reader("assets/start_screen.webp", 1, 1).get_asset_list()
        self.leaderboard = leaderboard #Maybe not for the Alpha test if time does not allow.
        self.height = height
        self.width = width

    def draw_start_screen(self):
        screen.fill = self.background

    def flashing_text(self):
        
        visible = True
        flash_timer = 0
        flash_interval = 500
        flash_enabled = True

        flash_text = {
        "Flashing Text": {"visible": True, "flash": True, "flash_timer": 0},
        "Static Text": {"visible": True, "flash": False}
        }

        current_time = pygame.time.get_ticks()
        if current_time - flash_timer > flash_interval:
            visible = not visible
            flash_timer = current_time
        
        if flash_enabled:
            if current_time - flash_text["Flashing Text"]["flash_timer"] > flash_interval:
                flash_text["Flashing Text"]["visible"] = not flash_text["Flashing Text"]["visible"]
                flash_text["Flashing Text"]["flash_timer"] = current_time


    def draw_text(self, text, font_name, color, size, x, y, visible):
        if visible:
            pygame.font.init()
            font = pygame.font.Font(font_name if font_name else None, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect(center=(x, y))
            screen.blit(text_surface, text_rect)

    def generate_return_surface(self):
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.blit(self.background[0], (0,0))
        return self.surface
    
    

    #Probably also needs to go in main bc we need to import joytick
    #def startGame(self):
