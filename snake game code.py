import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Clock & font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Score
def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, [10, 10])

# Draw snake
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, BLOCK_SIZE, BLOCK_SIZE])

# Main game loop
def game_loop():
    # Initial snake position
    x = WIDTH // 2
    y = HEIGHT // 2

    # Movement direction: moving right by default
    dx = BLOCK_SIZE
    dy = 0

    snake = [[x, y]]
    snake_length = 1

    # Random food position
    food_x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Movement with arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -BLOCK_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = BLOCK_SIZE
                    dx = 0

        # Update snake position
        x += dx
        y += dy

        # Check wall collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            break  # Game over

        # Update snake body
        snake.append([x, y])
        if len(snake) > snake_length:
            del snake[0]

        # Check self collision
        if snake.count([x, y]) > 1:
            break  # Game over

        # Check food collision
        if x == food_x and y == food_y:
            snake_length += 1
            food_x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            food_y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

        # Drawing
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        draw_snake(snake)
        show_score(snake_length - 1)
        pygame.display.update()
        clock.tick(10)

    # Game over screen

    screen.fill(BLACK)
    msg = font.render("Game Over! Press any key to exit.", True, RED)
    screen.blit(msg, [WIDTH // 6, HEIGHT // 2])
    pygame.display.update()
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                wait = False
    pygame.quit()
game_loop()
