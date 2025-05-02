from Asset_Reader import Asset_Reader

class Projectile:

    def __init__(self, projectile_image, x, y, speed):
        self.projectile_image = projectile_image
        self.x = x
        self.y = y
        self.speed = speed
        self.projectile_rect = projectile_image.get_rect()

    def move_in_straight_line(self, direction):
        if direction == 'L':
            self.x -= self.speed
            self.projectile_rect.move(self.x, self.y)
        elif direction == 'R':
            self.x += self.speed
            self.projectile_rect.move(self.x, self.y)
        elif direction == 'U':
            self.y -= self.speed
            self.projectile_rect.move(self.x, self.y)
        elif direction == 'D':
            self.y += self.speed
            self.projectile_rect.move(self.x, self.y)
