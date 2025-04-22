import pygame
from Asset_Reader import Asset_Reader
#from Player import Player (?)

screen = pygame.display.set_mode((1280, 1024))

class HUD:

    def __init__(self, width, height, player, health): #might not implement gold and timer might be moved.
        pass
        self.width = width
        self.height = height
        self.player = player
        self.timer = timer
        self.gold = gold
        self.health = health
        self.font = pygame.font.Font("fonts/PirataOne-Regular.ttf", 50)
        
    def generate_return_surface(self):
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(255,255,255)
        self.draw_text("Press Any Button To Start!", "fonts/PirataOne-Regular.ttf", (255,255,255), 45, 640, 800, counter, 30) # bigger numbers for i = slower flash
        self.draw_leaderboard("fonts/PirataOne-Regular.ttf", (255, 255, 255), 40, 100, 25, counter)
        return self.surface
    
    def update_timer():
        pass
    
    def draw_HUD(self):
        #Most likely going to draw a rectangle at the top of the screen and will use the draw_text function.

        pygame.Rect(0, 0, self.width, self.height - 924)
        self.draw_text("HUD", "fonts/PirataOne-Regular.ttf", (255, 255, 255), 20, 20)

        
    
    #Copied from start_screen
    def draw_text(self, text, font_name, color, size, x, y):
        font = pygame.font.Font(font_name if font_name else None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.surface.blit(text_surface, text_rect)

    def generate_return_surface(self):
        self.surface = pygame.Surface((self.width, self.height))
        #self.surface.blit(self.background[0], (self.x,self.y))
        pygame.Rect(0, 0, self.width, self.height - 924)
        self.draw_text("HP: ", "fonts/PirataOne-Regular.ttf", (255,255,255), 30, 20, 20)
        return self.surface