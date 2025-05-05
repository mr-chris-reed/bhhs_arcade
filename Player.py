import pygame, math
from pygame.locals import *
from Asset_Reader import Asset_Reader
from Projectile import Projectile
 

class Player:


    def __init__(self, 
                x_coord, y_coord, 
                ss_up, ss_down, ss_left, ss_right, ss_interact, ss_attack_left, ss_attack_right,
                idle_up,idle_down,idle_left,idle_right,
                num_up, num_down, num_left, num_right, num_interact, num_attack, num_up_idle, num_down_idle, num_left_idle, num_right_idle,
                scale,up_scale,down_scale, left_scale, right_scale,
                x_speed, y_speed):

        self.health = 5
        self.gold = 0
        self.damage = 1
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.ss_up = ss_up
        self.ss_down = ss_down
        self.ss_left = ss_left
        self.ss_right = ss_right
        self.ss_interact = ss_interact
        self.idle_up = idle_up
        self.idle_down = idle_down
        self.idle_left = idle_left
        self.idle_right = idle_right
        self.up_list = Asset_Reader(ss_up, num_up, up_scale).get_asset_list()
        self.size = self.up_list[0].get_rect()
        self.width = self.size.width
        self.height = self.size.height
        self.down_list = Asset_Reader(ss_down, num_down, down_scale).get_asset_list()
        self.left_list = Asset_Reader(ss_left, num_left, left_scale).get_asset_list()
        self.right_list = Asset_Reader(ss_right, num_right, right_scale).get_asset_list()
        self.interact_list = Asset_Reader(ss_interact, num_interact, scale).get_asset_list()
        self.attack_list_left = Asset_Reader(ss_attack_left, num_attack, scale).get_asset_list()
        self.attack_list_right = Asset_Reader(ss_attack_right, num_attack, scale).get_asset_list()
        self.idle_up_list = Asset_Reader(idle_up, num_up_idle, up_scale).get_asset_list()
        self.idle_down_list = Asset_Reader(idle_down, num_down_idle, down_scale).get_asset_list()
        self.idle_left_list = Asset_Reader(idle_left, num_left_idle, left_scale).get_asset_list()
        self.idle_right_list = Asset_Reader(idle_right, num_right_idle, right_scale).get_asset_list()
        self.sprite_index = 0
        self.last_sprite_list = self.right_list
        self.last_sprite = self.right_list[0]
        self.last_idle_sprite_list = self.idle_right_list
        self.last_idle_sprite = self.idle_right_list[0]
        self.last_button = "d"
        self.collision_rect = Rect(self.x_coord, self.y_coord, self.width - 100, self.height)
        self.alive = True

    def spritePicker(self, counter, sprite_list): # <== maybe we can have the counter be originated in the main file and it gets passed into this function as an argument
        if counter % 10 == 0: # adjust the number to the right of the "%" symbol to increase/decrease animation speed
            if self.sprite_index >= len(sprite_list) - 1:
                self.sprite_index = 0
            else:
                self.sprite_index += 1
        return sprite_list[self.sprite_index]

    def up(self, counter):
        if (self.last_button != "w"):
            self.sprite_index = 0
        self.y_coord -= self.y_speed
        self.last_sprite_list = self.up_list
        self.last_sprite =self.spritePicker(counter, self.up_list)
        self.last_idle_sprite_list = self.idle_up_list
        self.last_button ="w"
        self.last_idle_sprite = self.spritePicker(counter, self.idle_up_list)
        self.collision_rect.center = (self.x_coord + 100,self.y_coord + 90)

    def down(self, counter):
        if (self.last_button != "s"):
            self.sprite_index = 0
        self.y_coord += self.y_speed
        self.last_sprite_list =self.down_list
        self.last_sprite = self.spritePicker(counter, self.down_list)
        self.last_idle_sprite_list = self.idle_down_list
        self.last_button = "s"
        self.last_idle_sprite = self.spritePicker(counter, self.idle_down_list)
        self.collision_rect.center = (self.x_coord + 100,self.y_coord + 90)

    def left(self, counter):
        if (self.last_button != "a"):
            self.sprite_index = 0
        self.x_coord -= self.x_speed
        self.last_sprite_list = self.left_list
        self.last_sprite = self.spritePicker(counter, self.left_list)
        self.last_idle_sprite_list = self.idle_left_list
        self.last_button = "a"
        self.last_idle_sprite = self.spritePicker(counter, self.idle_left_list)
        self.collision_rect.center = (self.x_coord + 85,self.y_coord + 90)

    def right(self, counter):
        if (self.last_button != "d"):
            self.sprite_index = 0
        self.x_coord += self.x_speed
        self.last_sprite_list = self.right_list
        self.last_sprite = self.spritePicker(counter, self.right_list)
        self.last_idle_sprite_list = self.idle_right_list
        self.last_button = "d"
        self.last_idle_sprite = self.spritePicker(counter, self.idle_right_list)
        self.collision_rect.center = (self.x_coord + 100,self.y_coord + 90)

    def attack_right(self, counter):
        self.last_sprite = self.spritePicker(counter, self.attack_list_right)
    def attack_left(self, counter):
        self.last_sprite = self.spritePicker(counter, self.attack_list_left)
    def attack_up(self, counter):
        self.last_sprite = self.spritePicker(counter, self.attack_list_right)
    def attack_down(self, counter):
        self.last_sprite = self.spritePicker(counter, self.attack_list_left)

    def move_towards_player(self, player, counter):

        dx = player.x_coord - self.x_coord
        dy = player.y_coord - self.y_coord
        distance = math.hypot(dx, dy)
        if distance == 0:
            return  # WHY IS THIS RETURN HERE, WHAT DOES IT DO? 
        dx /= distance
        dy /= distance
        if dy < 0 and self.collision_rect.colliderect(player.collision_rect) != True:
            self.up(counter)
        if dy > 0 and self.collision_rect.colliderect(player.collision_rect) != True:
            self.down(counter)
        if dx < 0 and self.collision_rect.colliderect(player.collision_rect) != True:
            self.left(counter)
        if dx > 0 and self.collision_rect.colliderect(player.collision_rect) != True:
            self.right(counter)
        if self.collision_rect.colliderect(player.collision_rect) == True:
            self.badger_attack(player, counter)
            return True

    def enemy_hit(self, projectile, counter):
        if self.collision_rect.colliderect(projectile.projectile_rect):
            self.health -= 1
            return True
        if self.health == 0:
            self.alive = False
        return False
    
    def player_hit(self, counter):
        if counter % 30 == 0:
            self.health -= 1
        
    def badger_attack(self, player, counter):
        if self.collision_rect.colliderect(player.collision_rect) == True and self.last_button == "d":
            self.attack_right(counter)
        if self.collision_rect.colliderect(player.collision_rect) == True and self.last_button == "a":
            self.attack_left(counter)
        if self.collision_rect.colliderect(player.collision_rect) == True and self.last_button == "w":
            self.attack_up(counter)
        if self.collision_rect.colliderect(player.collision_rect) == True and self.last_button == "s":
            self.attack_down(counter)
