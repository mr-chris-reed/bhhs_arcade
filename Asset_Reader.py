# A utility class that can be used to import assets
# The class does all the processing during object
# creation.  There is a getter method to get
# the asset as a list.

import pygame

class Asset_Reader:

    def __init__(self, asset, num_images, scale_factor):
        self.asset = pygame.image.load(asset).convert_alpha()
        self.sprite_sheet_width = self.asset.get_rect().width
        self.sprite_sheet_height = self.asset.get_rect().height
        self.num_images = num_images
        self.scale_factor = scale_factor
        self.sprite_width = self.sprite_sheet_width // self.num_images
        self.sprite_height = self.sprite_sheet_height
        self.asset_list = []
        for i in range(self.num_images):
            rect = pygame.Rect(i * self.sprite_width, 0, self.sprite_width, self.sprite_sheet_height)
            image = self.asset.subsurface(rect)
            self.asset_list.append(image)
        for i in range(len(self.asset_list)):
            self.asset_list[i] = pygame.transform.scale(
                self.asset_list[i],
                (self.sprite_width * self.scale_factor, self.sprite_height * self.scale_factor)
            )

    def get_asset_list(self):
        return self.asset_list
