import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Star")

# Load player image
try:
    player_img = pygame.image.load("player.png").convert_alpha()
except pygame.error:
    print("Cannot load image 'player.png'. Please make sure it exists.")
    pygame.quit()
    sys.exit()

player_rect = player_img.get_rect()
player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Load star image
try:
    ikan_img = pygame.image.load("ikan.png").convert_alpha()
except pygame.error:
    print("Cannot load image 'ikan.png'. Please make sure it exists.")
    pygame.quit()
    sys.exit()

ikan_rect = ikan_img.get_rect()
ikan_rect.topleft = (random.randint(0, SCREEN_WIDTH - ikan_rect.width),
                     random.randint(0, SCREEN_HEIGHT - ikan_rect.height))

# Load bomb image
try:
    bomb_img = pygame.image.load("bomb.png").convert_alpha()
except pygame.error:
    print("Cannot load image 'bomb.png'. Please make sure it exists.")
    pygame.quit()
    sys.exit()

bomb_rect = bomb_img.get_rect()
bomb_rect.topleft = (random.randint(0, SCREEN_WIDTH - bomb_rect.width),
                     random.randint(0, SCREEN_HEIGHT - bomb_rect.height))

# Load background image
try:
    background_img = pygame.image.load("background.jpeg").convert()
except pygame.error:
    print("Cannot load image 'background.jpeg'. Please make sure it exists.")
    pygame.quit()
    sys.exit()

# Load background music
try:
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1)
except pygame.error:
    print("Cannot load audio 'background.mp3'. Please make sure it exists.")
    pygame.quit()
    sys.exit()

speed = 5
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def game_over():
    # Display Game Over text
    game_over_font = pygame.font.SysFont(None, 72)
    game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                                 SCREEN_HEIGHT // 3))

    final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 0))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2,
                                   SCREEN_HEIGHT // 2))

    pygame.display.flip()

# Game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if keys[pygame.K_UP]:
        player_rect.y -= speed
    if keys[pygame.K_DOWN]:
        player_rect.y += speed

    # Keep player on screen
    player_rect.clamp_ip(screen.get_rect())

    # Check collision with star
    if player_rect.colliderect(ikan_rect):
        score += 1
        # Move star to a new random position
        ikan_rect.topleft = (random.randint(0, SCREEN_WIDTH - ikan_rect.width),
                             random.randint(0, SCREEN_HEIGHT - ikan_rect.height))

    # Check collision with bomb
    if player_rect.colliderect(bomb_rect):
        game_over()
        pygame.time.delay(2000)  # Wait for 2 seconds before quitting
        running = False

    # Draw everything
    screen.blit(background_img, (0, 0))  # Draw the background image
    screen.blit(player_img, player_rect)
    screen.blit(ikan_img, ikan_rect)
    screen.blit(bomb_img, bomb_rect)

    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()
