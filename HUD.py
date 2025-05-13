import pygame
from Asset_Reader import Asset_Reader
#from Player import Player (maybe?)

screen = pygame.display.set_mode((1280, 1024))

class HUD:

    def __init__(self, width, height, player, time, hud_color): #timer might be moved.
        self.width = width
        self.height = height
        self.player = player
        self.time = time
        self.hud_color = hud_color
        self.score = None

    def draw_heart(self, center, size, distance, health):
        cx, cy = center
        s = size
        i = 0
        while (i < health):
            points = [
                (cx - (distance*i), cy + s),             # Bottom tip of the heart
                (cx - (distance*i)- s, cy),             # Left bottom curve
                (cx - (distance*i)- s, cy - s // 2),    # Upper left curve
                (cx - (distance*i)- s // 2, cy - s),    # Top left bump
                (cx - (distance*i), cy - s // 2),        # Center dip at top
                (cx - (distance*i) + s // 2, cy - s),    # Top right bump
                (cx - (distance*i) + s, cy - s // 2),    # Upper right curve
                (cx - (distance*i) + s, cy),             # Right bottom curve
            ]
            heart = pygame.draw.polygon(screen, (255,0,0), points)
            heart_surface = pygame.Surface((self.width, self.height))
            heart_surface.set_alpha(0)
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
    def generate_return_surface(self, time, health, frame_count):
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.hud_color)
        self.surface.set_alpha(100)
        self.update_time(self.time, frame_count)
        self.draw_heart((1200, 40), 25, 60, health)
        return self.surface

    def update_time(self, time, frame_count):
        font = pygame.font.Font("fonts/PirataOne-Regular.ttf", 25)
        scorelist = []
        frame_rate = 60
        total_seconds = frame_count / (frame_rate) # gets the time unrounded
        roundedtime=round(total_seconds,2)# rounds time to 2 decimal places
        self.score= f"{roundedtime:.2f}" # sets hud.time to the rounded time
        self.draw_text("Time " + str(self.score),"fonts/PirataOne-Regular.ttf", (255,255,255), 45, 50, 10)
        #time.tick(frame_rate)