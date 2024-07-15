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

# Font for player name and level
font = pygame.font.Font(None, 36)
player_name = "Hanna Mzeget"
level_font = pygame.font.Font(None, 48)
game_over_font = pygame.font.Font(None, 72)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player.Player()
all_sprites.add(player)

# Function to create obstacles based on level
def create_obstacles(level):
    for _ in range(5 + level):  # Increase number of obstacles with level
        obstacle = Obstacle.Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

# Function to display the "Game Over" screen
def show_game_over_screen():
    screen.fill(setings.BLACK)
    game_over_text = game_over_font.render("Game Over", True, setings.RED)
    screen.blit(game_over_text, (setings.SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                                 setings.SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

# Initialize game state
running = True
game_level = 1
create_obstacles(game_level)
obstacles_cleared = 0

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
            bullet.kill()
            obstacles_cleared += 1
            print(obstacles_cleared)
            if obstacles_cleared == 6:  # Increase level after clearing 6 obstacles
                game_level += 1
                obstacles_cleared = 0
                create_obstacles(game_level)

    # Check for collisions between player and obstacles
    if pygame.sprite.spritecollideany(player, obstacles):
        running = False
        show_game_over_screen()

    # Draw everything
    screen.fill(setings.BLACK)

    # Draw header
    screen.fill(setings.WHITE, (0, 0, setings.SCREEN_WIDTH, setings.HEADER_HEIGHT))
    screen.blit(player_photo, (10, 25))
    text = font.render(player_name, True, setings.BLACK)
    screen.blit(text, (90, 35))

    # Display the current level
    level_text = level_font.render(f"Level: {game_level}", True, setings.BLACK)
    screen.blit(level_text, (setings.SCREEN_WIDTH - 150, 35))

    # Draw sprites
    for entity in all_sprites:
        if isinstance(entity, Player.Player):
            entity.draw(screen)
        else:
            screen.blit(entity.image, entity.rect.topleft)

    pygame.display.flip()

pygame.quit()
