from Asset_Reader import Asset_Reader
from Player import Player

class Background:

    background_index = 0

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

        ###
        # NOTES - 3/17/25 - You need to work on moving code that you currently have in the connor_teting
        # file to this class.  In the testing class, which will ultimately be our main driving file,
        # you could have 3 constructor calls to the Background class creating 3 backgrounds. Then in
        # the main game loop (your connner_testing file / main) you can write the logic for changing
        # screens.  This will occur when the player reaches the right-hand side of the screen (like going
        # through a door).
        ###
    def __init__(self, background, num_images, x, y, scale_factor, origin_x, origin_y, width, height):
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
        self.next_flag = next_flag
        self.prev_flag = prev_flag

    # If player is inside the next boundary, the background only changes once(flag becomes true when inside, becomes false when outside)
    def change_next_flag(background_list, player_x, player_y):
        if (background_list[Background.background_index].next_x <= player_x <= background_list[Background.background_index].next_x + background_list[Background.background_index].next_width and
            background_list[Background.background_index].next_y <= player_y <= background_list[Background.background_index].next_y + background_list[Background.background_index].next_height):
            if not background_list[Background.background_index].next_flag:  # Only change background if not already triggered
                if Background.background_index < len(background_list) - 1:
                    Background.background_index += 1
                background_list[Background.background_index].next_flag = True
        else:
            background_list[Background.background_index].next_flag = False  # Reset flag when leaving the next box

    # If player is inside the prev boundary, the background only changes once(flag becomes true when inside, becomes false when outside)
    def change_prev_flag(background_list, character):
        x = charcter.x_attrib
        if (background_list[Background.background_index].prev_x <= player_x <= background_list[Background.background_index].prev_x + background_list[Background.background_index].prev_width and
            background_list[Background.background_index].prev_y <= player_y <= background_list[Background.background_index].prev_y + background_list[Background.background_index].prev_height):
            if not background_list[Background.background_index].prev_flag:  # Only change background if not already triggered
                if Background.background_index > 0:
                    Background.background_index -= 1
                background_list[Background.background_index].prev_flag = True
        else:
            background_list[Background.background_index].prev_flag = False  # Reset flag when leaving the prev box

    # Returns true if player is inside the boundaries, returns false if not
    def checkIfInBounds(background_list, character):
        x = character.x_coord
        y = character.y_coord
        if (background_list[Background.background_index].boundary_x + x <= new_x <= background_list[Background.background_index].boundary_x + background_list[Background.background_index].boundary_width - circle_radius and
            background_list[Background.background_index].boundary_y + y <= new_y <= background_list[Background.background_index].boundary_y + background_list[Background.background_index].boundary_height - circle_radius):
            return True
        else:
            return False

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
    
