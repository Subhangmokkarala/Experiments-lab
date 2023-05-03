import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")

# Load game assets
player_img = pygame.image.load('player.png')
player_rect = player_img.get_rect()
player_rect.centerx = screen_width / 2
player_rect.bottom = screen_height - 10

enemy_img = pygame.image.load('enemy.png')
enemy_rect = enemy_img.get_rect()

bullet_img = pygame.image.load('bullet.png')
bullet_rect = bullet_img.get_rect()

# Set up game variables
player_speed = 5
enemy_speed = 3
bullet_speed = 8
bullet_state = "ready"
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.left -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_rect.right += player_speed
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_rect.centerx = player_rect.centerx
                bullet_rect.top = player_rect.top
                bullet_state = "fire"
    
    # Move enemies
    enemy_rect.top += enemy_speed
    if enemy_rect.top > screen_height:
        enemy_rect.left = random.randint(0, screen_width - enemy_rect.width)
        enemy_rect.top = -enemy_rect.height
        score += 1
    
    # Move bullet
    if bullet_state == "fire":
        bullet_rect.top -= bullet_speed
        if bullet_rect.top < 0:
            bullet_state = "ready"
    
    # Check for collisions
    if bullet_rect.colliderect(enemy_rect):
        enemy_rect.left = random.randint(0, screen_width - enemy_rect.width)
        enemy_rect.top = -enemy_rect.height
        bullet_state = "ready"
        score += 10
    
    # Draw the screen
    screen.fill((0, 0, 0))
    screen.blit(player_img, player_rect)
    screen.blit(enemy_img, enemy_rect)
    if bullet_state == "fire":
        screen.blit(bullet_img, bullet_rect)
    
    # Draw the score
    score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

# Clean up
pygame.quit()