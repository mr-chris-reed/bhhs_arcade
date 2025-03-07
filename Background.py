from Asset_Reader import Asset_Reader

class Background:
    def __init__(self, background, num_images, x, y, scale_factor, origin_x, origin_y, width, height):
        self.background_list = Asset_Reader(background, num_images, scale_factor).get_asset_list()  # Load the backgrounds
        self.x = x
        self.y = y
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width
        self.height = height

    def get_current_background(self): # Returns the current background
        return self.background_list[self.current_index]