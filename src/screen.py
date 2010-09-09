import pygame

class MainScreen(object):

    def __init__(self, width, height):
        self.size = self.width, self.height = width, height
        self.screen = pygame.display.set_mode(self.size)
