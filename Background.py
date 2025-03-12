from Asset_Reader import Asset_Reader

class Background:
    def __init__(self, background, num_images, x, y, scale_factor):
        ###
        # NOTES: You might consider creating instance variables that define the
        # movable space - the area where characters can move around - boundaries for background.
        # One way to do this is to create instance variables of x_low, x_high, y_low, y_high. These instance variables
        # can be used by the player and enimies to control the character not moving off of the screen.
        # We need to discuss how we want to control background flow. Will it be part of this class,
        # like you have below with the methods moveToNext and moveToPrev, or will this be controlled
        # in the main loop?  Along with this challenge, we also need to think about how the character
        # transitions to the next background.  Does it happen automatically when minions/boss is
        # destroyed or is there a door?
        ###
        self.background_list = Asset_Reader(background, num_images, scale_factor).get_asset_list()  # Load the backgrounds
        self.x = x
        self.y = y
        #self.origin_x = origin_x
        #self.origin_y = origin_y
        #self.width = width
        #self.height = height

    def get_current_background(self): # Returns the current background
        return self.background_list[self.current_index]