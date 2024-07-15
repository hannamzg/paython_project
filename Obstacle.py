import pygame
import setings
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(setings.RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, setings.SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(100, 100)
        self.speed_y = random.randint(5, 10)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > setings.SCREEN_HEIGHT:
            self.rect.x = random.randint(0, setings.SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(100, 100)
            self.speed_y = random.randint(5, 10)
