import pygame, sys
from settings import WIDTH, HEIGHT, ground_space
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird | 2024 - 2025")

class Main:
    def __init__(self, screen):
        self.screen = screen
        self.bg_img = pypygame.image.load("assets/terrain/bg.png")
        self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))
        self.ground_img = pygame.image.load("assets/terrain/ground.png")
        self.ground_scroll = 0
        self.scroll_speed = -6
        self.FPS = pygame.time.Clock()
        self.stop_ground_scroll = False
    