from Asset_Reader import Asset_Reader
import pygame

class Background:

    background_index = 0

    def __init__(self, sprite_sheet, num_images, scale_factor, x, y, low_x, high_x, low_y, high_y):
        self.background_image = Asset_Reader(sprite_sheet, num_images, scale_factor).get_asset_list()
        self.x = x
        self.y = y
        self.low_x = low_x
        self.high_x = high_x
        self.low_y = low_y
        self.high_y = high_y
        self.size = self.background_image[0].get_rect()
        self.width = self.size.width
        self.height = self.size.height
        self.in_box = pygame.Surface((200, 200), pygame.SRCALPHA)
        self.in_box_rect = pygame.Rect(self.low_x, self.low_y, 200, 1000)
        self.out_box = pygame.Surface((200, 200), pygame.SRCALPHA)
        self.out_box_rect = pygame.Rect(self.high_x, self.low_y, 200, 1000)

    def generate_return_surface(self):
        surface = pygame.Surface((self.width, self.height))
        surface.blit(self.background_image[0], (self.x, self.y))
        pygame.draw.line(surface, (0, 0, 0), (self.low_x, self.low_y), (self.high_x, self.low_y), width=3)
        pygame.draw.line(surface, (0, 0, 0), (self.low_x, self.low_y), (self.low_x, self.high_y), width=3)
        pygame.draw.line(surface, (0, 0, 0), (self.high_x, self.low_y), (self.high_x, self.high_y), width=3)
        pygame.draw.line(surface, (0, 0, 0), (self.low_x, self.high_y), (self.high_x, self.high_y), width=3)
        pygame.draw.rect(self.in_box, (255, 255, 255, 64), (0, 0, 200, 200))
        surface.blit(self.in_box, (self.low_x, self.low_y))
        pygame.draw.rect(self.out_box, (255, 255, 255, 64), (0, 0, 200, 200))
        surface.blit(self.out_box, (self.high_x - 200, self.high_y - 200))
        return surface

    def check_can_move_left(self, player):
        if (player.x_coord - player.x_speed > self.low_x):
            return True
        else:
            return False

    def check_can_move_right(self, player):
        if (player.x_coord + player.x_speed + player.width < self.high_x):
            return True
        else:
            return False

    def check_can_move_up(self, player):
        if (player.y_coord - player.y_speed > self.low_y):
            return True
        else:
            return False

    def check_can_move_down(self, player):
        if (player.y_coord + player.y_speed + player.height < self.high_y):
            return True
        else:
            return False

    def check_if_in_next_box(self, player):
        player_rect = pygame.Rect(player.x_coord, player.y_coord, player.width, player.height)
        if self.out_box_rect.contains(player_rect):
            return True
        else:
            return False

    def check_if_in_prev_box(self, player):
        player_rect = pygame.Rect(player.x_coord, player.y_coord, player.width, player.height)
        if self.in_box_rect.contains(player_rect):
            return True
        else:
            return False
