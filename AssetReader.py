# A utility class that can be used to import assets
# The class has one public method that returns a list
# of the assets
import pygame

class AssetReader:

    def __init__(self, asset ,numImages):
        self.asset = pygame.image.load(asset).convert_alpha()
        self.width = self.asset.get_rect().width
        self.height = self.asset.get_rect().height
        self.numImages = numImages
        self.asset_list = []

    def getAssetList(self):
        sprite_width = self.width // self.numImages
