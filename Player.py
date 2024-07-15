# Player.py
import pygame
import setings
import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (setings.SCREEN_WIDTH // 2, setings.SCREEN_HEIGHT - 50)
        self.speed_x = 0
        self.corner_radius = 10
        self.color = setings.WHITE

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -5
        if keys[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > setings.SCREEN_WIDTH:
            self.rect.right = setings.SCREEN_WIDTH

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=self.corner_radius)

    def shoot(self):
        bullet = Bullet.Bullet(self.rect.centerx, self.rect.top)
        return bullet
