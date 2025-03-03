import pygame
from Asset_Reader import Asset_Reader
 
class player:

     def __init__(self,x_coord, y_coord, ss_up, ss_down, ss_left, ss_right, ss_interact, ss_attack, num_images, scale):
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
        self.up_list = Asset_Reader(ss_up, num_images, scale).get_asset_list()
        self.down_list = Asset_Reader(ss_down, num_images, scale).get_asset_list()
        self.left_list = Asset_Reader(ss_left, num_images, scale).get_asset_list()
        self.right_list = Asset_Reader(ss_right, num_images, scale).get_asset_list()
        self.interact_list = Asset_Reader(ss_interact, num_images, scale).get_asset_list()
        self.attack_list = Asset_Reader(ss_attack, num_images, scale).get_asset_list()



        # Player file

# Tasks for cshook - ss_up, ss_down, ss_left, ss_right, ss_interact, ss_attack, up, down, left, right

    #update with Rowan's code 

        #self.ss_up = ss_up
        #self.ss_down = ss_down
        #self.ss_left = ss_left
        #self.ss_right = ss_right
        #self.ss_interact = ss_interact
        #self.ss_attack = ss_attack

        #actions
        def up()

