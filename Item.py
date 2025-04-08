# Item class that will be used to provide items that the player can interact with
# i.e. items that boost stats and other instruments
#Made in cohesion to Player class - Cole

import pygame
from Asset_Reader import Asset_Reader

class Item:

    def __init__(self, item_image, item_name, x, y, price):
        self.item_image = Asset_Reader(item_image, 1, 1.0).get_asset_list()[0]
        self.item_name = item_name
        self.interact = False
        self.x = x
        self.y = y
        self.price = price
        self.interact_surface = pygame.Surface((70, 70), pygame.SRCALPHA)
        self.interact_rect = pygame.Rect(x, y, 70, 70)
        self.picked_up = False

    def draw_item(self, CANVAS):
        if (self.picked_up == False):
            CANVAS.blit(self.item_image, (self.x, self.y))

    def interact_check(self, player):
        player_rect = pygame.Rect(player.x_coord, player.y_coord, player.width, player.height)
        if self.interact_rect.colliderect(player_rect):
            self.picked_up = True
            return True
        else:
            return False