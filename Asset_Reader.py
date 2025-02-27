# A utility class that can be used to import assets
# The class has three public methods:
#
# process_asset_list() - breaks up assets into a list,
# if there is only one asset, you can access is by 
# getting the object at index 0.
#
# scale_asset_list() - will scale each asset in the list
# to the width and height specified as arguments.
#
# get_asset_list() - returns the processed asset list.

import pygame

class Asset_Reader:

    def __init__(self, asset ,num_images):
        self.asset = pygame.image.load(asset).convert_alpha()
        self.width = self.asset.get_rect().width
        self.height = self.asset.get_rect().height
        self.num_images = num_images
        self.asset_list = []

    def process_asset_list(self):
        sprite_width = self.width // self.num_images
        sprite_height = self.height
        for i in range(self.num_images):
            rect = pygame.Rect(i * sprite_width, 0, sprite_width, sprite_height)
            image = self.asset.subsurface(rect)
            self.asset_list.append(image)

    def scale_asset_list(self, width, height):
        for i in range(len(self.asset_list)):
            self.asset_list[i] = pygame.transform.scale(self.asset_list[i], (width, height))

    def get_asset_list(self):
        return self.asset_list