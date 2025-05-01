import pygame
from Asset_Reader import Asset_Reader
#from Player import Player (maybe?)

screen = pygame.display.set_mode((1280, 1024))

class HUD:

    def __init__(self, width, height, player, health, time, hud_color): #timer might be moved.
        self.width = width
        self.height = height
        self.player = player
        self.time = time
        self.health = health
        self.hud_color = hud_color
    
    def draw_HUD(self, time):
        # use the draw_text function.
        self.draw_text("HP: " + str(self.health), "fonts/PirataOne-Regular.ttf", (255,255,255), 45, 1150, 10)
        self.draw_text("Time " + str(time), "fonts/PirataOne-Regular.ttf", (255,255,255), 45, 50, 10)

    def draw_heart(self, center, size, number):
        cx, cy = center
        s = size
        i = 0
        while (i < number):
            points = [
                (cx - (50*i), cy + s),             # Bottom tip of the heart
                (cx - (50*i)- s, cy),             # Left bottom curve
                (cx - (50*i)- s, cy - s // 2),    # Upper left curve
                (cx - (50*i)- s // 2, cy - s),    # Top left bump
                (cx - (50*i), cy - s // 2),        # Center dip at top
                (cx - (50*i) + s // 2, cy - s),    # Top right bump
                (cx - (50*i) + s, cy - s // 2),    # Upper right curve
                (cx - (50*i) + s, cy),             # Right bottom curve
            ]
            heart = pygame.draw.polygon(screen, (255,0,0), points)
            heart_surface = pygame.Surface((self.width, self.height))
            heart_surface.set_alpha(50)
            self.surface.blit(heart_surface, heart)
            i+=1

    #Copied from start_screen with some tweaks.
    def draw_text(self, text, font_name, color, size, x, y):
        font = pygame.font.Font(font_name if font_name else None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        text_rect.topleft = (x,y)
        self.surface.blit(text_surface, text_rect)

    #Copied from start_screen with some tweaks.
    def generate_return_surface(self, time):
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.hud_color)
        self.surface.set_alpha(0)
        self.draw_HUD(self.time)
        self.draw_heart((1150, 50), 20, self.health)
        return self.surface
