import pygame
from Asset_Reader import Asset_Reader
#from Player import Player (maybe?)

screen = pygame.display.set_mode((1280, 1024))

class HUD:

    def __init__(self, width, height, player, health, time): #timer might be moved.
        pass
        self.width = width
        self.height = height
        self.player = player
        self.time = time
        self.health = health
    
    def draw_HUD(self, time):
        #Draws a rectangle at the top of the screen and will use the draw_text function.
        '''self.box = pygame.Surface((1280,100))
        self.box.fill((255,0,0))
        self.box.set_alpha(10)
        self.surface.blit(self.box, (0,0))'''
        self.draw_text("HUD", "fonts/PirataOne-Regular.ttf", (255, 255, 255), 20, 1000, 20)
        self.draw_text("HP: " + str(self.health), "fonts/PirataOne-Regular.ttf", (255,255,255), 45, 800, 25)
        self.draw_text("Time " + str(time), "fonts/PirataOne-Regular.ttf", (255,255,255), 45, 50, 25)

    #Copied from start_screen with some tweaks.
    def draw_text(self, text, font_name, color, size, x, y):
        font = pygame.font.Font(font_name if font_name else None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.surface.blit(text_surface, text_rect)

    #Copied from start_screen with some tweaks.
    def generate_return_surface(self, time):
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255,0,0))
        self.surface.set_alpha(100)
        self.draw_HUD(self.time)
        self.update_time(self.time)
        return self.surface

    #Doesn't work yet.
    def update_time(self, time):
        font = pygame.font.Font("fonts/PirataOne-Regular.ttf", 25)
        scorelist = []
        frame_count = 0
        frame_rate = 60
        total_seconds = frame_count // frame_rate  # total seconds passed
        score= f"Time: {total_seconds}"
        text = font.render(score, True, (0, 0, 0)) # render _ display
        screen.blit(text, [250, 20])
        frame_count += 1
        time.tick(frame_rate)