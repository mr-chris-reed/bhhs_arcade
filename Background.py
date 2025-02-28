
class Background:
    def __init__(self, backgrounds, x, y, width, height):
        self.backgrounds = backgrounds  # List of backgrounds
        self.currentIndex = 0  # Index of the current background
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def moveToNext(self):
        if self.currentIndex < len(self.backgrounds) - 1:  # Check if there is a next background
            self.currentIndex += 1

    def moveToPrev(self):
        if self.currentIndex > 0:  # Check if there is a previous background
            self.currentIndex -= 1

    def getCurrentBackground(self):
        return self.backgrounds[self.currentIndex]  # Get the current background