import pygame
import random
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

snake = [(width // 2, height // 2), (width // 2 - 10, height // 2), (width // 2 - 20, height // 2)]
snake_direction = "right"

food = (random.randint(0, (width - 10) // 10) * 10, random.randint(0, (height - 10) // 10) * 10)
score = 0

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"
            elif event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"

    if snake_direction == "up":
        snake.insert(0, (snake[0][0], snake[0][1] - 10))
    elif snake_direction == "down":
        snake.insert(0, (snake[0][0], snake[0][1] + 10))
    elif snake_direction == "left":
        snake.insert(0, (snake[0][0] - 10, snake[0][1]))
    elif snake_direction == "right":
        snake.insert(0, (snake[0][0] + 10, snake[0][1]))

    if (snake[0][0] < 0 or snake[0][0] >= width or
        snake[0][1] < 0 or snake[0][1] >= height or
        snake[0] in snake[1:]):
        pygame.quit()
        sys.exit()

    if snake[0] == food:
        score += 1
        food = (random.randint(0, (width - 10) // 10) * 10, random.randint(0, (height - 10) // 10) * 10)
    else:
        snake.pop()

    screen.fill((0, 0, 0))
    for pos in snake:
        pygame.draw.rect(screen, (0, 255, 0), (pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], 10, 10))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(15)  # Frame rate control, 15 frames per second