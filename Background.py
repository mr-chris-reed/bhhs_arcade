from Asset_Reader import Asset_Reader

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
    def change_prev_flag(background_list, player_x, player_y):
        if (background_list[Background.background_index].prev_x <= player_x <= background_list[Background.background_index].prev_x + background_list[Background.background_index].prev_width and
            background_list[Background.background_index].prev_y <= player_y <= background_list[Background.background_index].prev_y + background_list[Background.background_index].prev_height):
            if not background_list[Background.background_index].prev_flag:  # Only change background if not already triggered
                if Background.background_index > 0:
                    Background.background_index -= 1
                background_list[Background.background_index].prev_flag = True
        else:
            background_list[Background.background_index].prev_flag = False  # Reset flag when leaving the prev box

    # Returns true if player is inside the boundaries, returns false if not
    def check_if_in_bounds(background_list, player_x, player_y, player_width, player_height):
        if (background_list[Background.background_index].boundary_x <= player_x and background_list[Background.background_index].boundary_y <= player_y and player_x + player_width <= background_list[Background.background_index].boundary_x + background_list[Background.background_index].boundary_width and player_y + player_height <= background_list[Background.background_index].boundary_y + background_list[Background.background_index].boundary_height):
            return True
        else:
            return False

