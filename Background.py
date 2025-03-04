from Asset_Reader import Asset_Reader

class Background:
    def __init__(self, background, num_images, x, y, scale_factor):
        self.background_list = Asset_Reader(background, num_images, scale_factor).get_asset_list()  # Load the backgrounds
        self.current_index = 0  # Track current background
        self.x = x
        self.y = y
        index = 0

    def moveToNext(self):
        """Move to the next background in the list, looping back if needed."""
        self.index = (self.index + 1) % len(self.backgrounds)

    def moveToPrev(self):
        """Move to the previous background, looping if at the beginning."""
        if self.current_index > 0:
            self.current_index -= 1
        else:
            self.current_index = len(self.background_list) - 1  # Loop to the last background

    def get_current_background(self):
        """Returns the current background image."""
        return self.background_list[self.current_index]