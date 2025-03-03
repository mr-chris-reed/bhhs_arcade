
# Player file

# Tasks for cshook - ss_up, ss_down, ss_left, ss_right, ss_interact, ss_attack, up, down, left, right

    #update with Rowan's code 

        #self.ss_up = ss_up
        #self.ss_down = ss_down
        #self.ss_left = ss_left
        #self.ss_right = ss_right
        #self.ss_interact = ss_interact
        #self.ss_attack = ss_attack
            
    

import pygame
import Asset_Reader
 
class player:

     def __init__(self,x_coord, y_coord, ss_up, ss_down, ss_left, ss_right, ss_interact, ss_attack):
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
        #self.up_list =
        #self.down_list = 
        #self.left_list = 
        #self.right_list
        #self.interact_list
        #self.attack_list


        #actions
        def up():
            pass
        
        def down():
            pass

        def left():
            pass

        def right():
            pass