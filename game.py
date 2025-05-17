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

    def show_score(self, int_score):
        bird_score = str(int_score)
        score = self.font.render(bird_score, True, self.color)
        self.screen.blit(score, (WIDTH // 2, 50))
