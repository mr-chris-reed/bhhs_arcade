# Item class that will be used to provide items that the player can interact with
# i.e. items that boost stats and other instruments
#Made in cohesion to Player class - Cole

import pygame
from Asset_Reader import Asset_Reader

class Item:

    def __init__(self, item_image, item_name, x, y, price):
        self.item_image = item_image
        self.item_name = item_name
        self.interact = False
        self.price = price
        self.interact_surface = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.interact_rect = pygame.Rect(x, y, 30, 30)

    def interact_check(self, Player):
        pass