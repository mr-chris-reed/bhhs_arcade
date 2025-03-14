from Asset_Reader import Asset_Reader

class Background:
    def __init__(self, background, num_images, x, y, scale_factor, boundary_x, boundary_y, boundary_width, boundary_height, next_x, next_y, next_width, next_height, prev_x, prev_y, prev_width, prev_height, next_flag, prev_flag):
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
        self.boundary_x = boundary_x
        self.boundary_y = boundary_y
        self.boundary_width = boundary_width
        self.boundary_height = boundary_height
        self.next_x = next_x
        self.next_y = next_y
        self.next_width = next_width
        self.next_height = next_height
        self.prev_x = prev_x
        self.prev_y = prev_y
        self.prev_width = prev_width
        self.prev_height = prev_height
        self.next_flag = False
        self.prev_flag = False

    def get_current_background(self): # Returns the current background
        return self.background_list[self.current_index]
    
    def get_boundary_x(self): # Returns the x coordinate of the boundary
        return self.boundary_x
    
    def get_boundary_y(self): # Returns the y coordinate of the boundary
        return self.boundary_y
    
    def get_boundary_width(self): # Returns the width of the boundary
        return self.boundary_width
    
    def get_boundary_height(self): # Returns the height of the boundary
        return self.boundary_height
    
    def get_next_x(self):
        return self.next_x
    
    def get_next_y(self):
        return self.next_y
    
    def get_next_width(self):
        return self.next_width
    
    def get_next_height(self):
        return self.next_height
    
    def get_prev_x(self):
        return self.prev_x
    
    def get_prev_y(self):
        return self.prev_y
    
    def get_prev_width(self):
        return self.prev_width
    
    def get_prev_height(self):
        return self.prev_height
    
    def get_next_flag(self):
        return self.next_flag
    
    def get_prev_flag(self):
        return self.prev_flag
    
    def set_next_flag(self, tof):
        self.next_flag = tof

    def set_prev_flag(self, tof):
        self.prev_flag = tof
    