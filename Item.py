# Item class that will be used to provide items that the player can interact with
# i.e. items that boost stats and other instruments
#Made in cohesion to Player class - Cole

import pygame
from Asset_Reader import Asset_Reader

class Item:

    def __init__(self, item_image, item_name, interact):
        self.item_image = item_image
        self.item_name = item_name
        self.interact = interact