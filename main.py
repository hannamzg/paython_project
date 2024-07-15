import pygame
import random
import setings
import Player
import Obstacle
import Bullet

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((setings.SCREEN_WIDTH, setings.SCREEN_HEIGHT))
pygame.display.set_caption("Avoid the Obstacles")

# Load player photo
player_photo = pygame.image.load('photos/women_model_4k_hd-hd_wallpapers.jpg')  # Ensure this image exists
player_photo = pygame.transform.scale(player_photo, (70, 70))

# Font for player name
font = pygame.font.Font(None, 36)
player_name = "Hanna Mzeget"

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player.Player()
all_sprites.add(player)

for _ in range(10):
    obstacle = Obstacle.Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Game loop
running = True
while running:
    clock.tick(setings.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses for shooting
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bullet = player.shoot()
        all_sprites.add(bullet)
        bullets.add(bullet)

    all_sprites.update()

    # Check for collisions between bullets and obstacles
    for bullet in bullets:
        hits = pygame.sprite.spritecollide(bullet, obstacles, True)
        if hits:
            obstacle = Obstacle.Obstacle()
            all_sprites.add(obstacle)
            obstacles.add(obstacle)
            bullet.kill()

    # Check for collisions between player and obstacles
    if pygame.sprite.spritecollideany(player, obstacles):
        running = False

    # Draw everything
    screen.fill(setings.BLACK)

    # Draw header
    screen.fill(setings.WHITE, (0, 0, setings.SCREEN_WIDTH, setings.HEADER_HEIGHT))
    screen.blit(player_photo, (10, 25))
    text = font.render(player_name, True, setings.BLACK)
    screen.blit(text, (90, 35))

    # Draw sprites
    for entity in all_sprites:
        if isinstance(entity, Player.Player):
            entity.draw(screen)
        else:
            screen.blit(entity.image, entity.rect.topleft)

    pygame.display.flip()

pygame.quit()
