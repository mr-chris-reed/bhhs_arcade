from Asset_Reader import Asset_Reader

class Projectile:

    def __init__(self, projectile_image, x, y, speed):
        self.projectile_image = projectile_image
        self.projectile_rect = self.projectile_image.get_rect()
        self.x = x
        self.y = y
        self.speed = speed

    def move_in_straight_line(self, direction):
        if direction == 'L':
            self.x -= self.speed
        elif direction == 'R':
            self.x += self.speed
        elif direction == 'U':
            self.y -= self.speed
        elif direction == 'D':
            self.y += self.speed
