
import pygame
from Asset_Reader import Asset_Reader
 

class Player:


    def __init__(self, 
                x_coord, y_coord, 
                ss_up, ss_down, ss_left, ss_right, ss_interact, ss_attack,
                num_up, num_down, num_left, num_right, num_interact, num_attack,
                scale,up_scale,down_scale, left_scale, right_scale,
                x_speed, y_speed):
        ###
        # NOTES: For movement, you could use the instance variables x_speed and y_speed.
        # You could fill in the methods you wrote below to move the character like
        # self.x_coord += self.x_speed, self.x_coord -= self.x_coord, etc.
        # What do we want the attack to be?  Projectile or melee? Would there be extra
        # animations for this?  Are we going to have animations for interact?
        ###
        self.health = 5
        self.gold = 0
        self.damage = 5
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_speed = 5
        self.y_speed = 5
        self.ss_up = ss_up
        self.ss_down = ss_down
        self.ss_left = ss_left
        self.ss_right = ss_right
        self.ss_interact = ss_interact
        self.up_list = Asset_Reader(ss_up, num_up, up_scale).get_asset_list()
        self.down_list = Asset_Reader(ss_down, num_down, down_scale).get_asset_list()
        self.left_list = Asset_Reader(ss_left, num_left, left_scale).get_asset_list()
        self.right_list = Asset_Reader(ss_right, num_right, right_scale).get_asset_list()
        self.interact_list = Asset_Reader(ss_interact, num_interact, scale).get_asset_list()
        self.attack_list = Asset_Reader(ss_attack, num_attack, scale).get_asset_list()
        self.sprite_index = 0
        self.last_sprite = egg.right_list

    ###
    # NOTES - 3/17/25 - remove duplicate up function below.  I think when one of
    # the action functions are called from the main file (currently, your testing file),
    # The spritePicker function should be called from within each of the action functions.
    # Something like:
    # def up(self, counter):
    #    self.y_coord -= self.y_speed
    #    return spritePicker(counter, self.up_list) - I think the spritePicker function should return a surface
    #    The surface it returns will be the surface at the correct sprite_index.  You'll probabaly have to
    #    rework the spritePicker function a bit.
    ###

    
   
        #actions
    def up(self):
        self.y_coord -= self.y_speed
        return spritePicker(counter, self.uplist)
        self.last_sprite = egg.up_list
        
    def down(self):
        self.y_coord += self.y_speed

        self.last_sprite = egg.down_list

    def left(self):
        self.x_coord -= self.x_speed

        self.last_sprite = egg.left_list

    def right(self):
        self.x_coord += self.x_speed

        self.last_sprite = egg.right_list

    #def interact(self, item_group):
        #for item in item_group:
            #if pygame.sprite.collide_rect(self, item) and key
                # item.collect(self)  

                
    def spritePicker(self, counter, sprite_list): # <== maybe we can have the counter be originated in the main file and it gets passed into this function as an argument
        if counter % 60 == 0: # adjust the number to the right of the "%" symbol to increase/decrease animation speed
            if self.sprite_index == len(sprite_list) - 1:
                self.sprite_index = 0
            else:
                self.sprite_index += 1
        return sprite_list[sprite_index]


