import pygame

class Start_Screen:

    def __init__(self, startbutton, background, title, leaderboard, font):
        self.font = font
        font = pygame.font.SysFont('times new roman', 40)
        self.startbutton = startbutton
        startbutton = font.render("Start", True, (255, 255, 255))
        self.background = background
        self.title = title
        title = font.render("CapyBarda", True, (255, 255, 255))
        self.leaderboard = leaderboard

        def drawStartScreen(self):
            pass

        def startGame(self):
            pass