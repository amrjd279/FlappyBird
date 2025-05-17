import pygame
from settings import WIDTH, HEIGHT

pygame.font.init()

class GameIndicator:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Bauhaus 93", 60)
        self.inst_font = pygame.font.SysFont("Bauhaus 93", 30)
        self.color = pygame.Color("White")
        self.inst_color = pygame.Color("Black")