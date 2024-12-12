import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Table Tennis Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Game variables
paddle_width, paddle_height = 10, 100
ball_radius = 7
paddle_speed = 5
ball_speed_x, ball_speed_y = 4, 4

# Paddle positions
left_paddle_y = right_paddle_y = height // 2 - paddle_height // 2

# Ball position
ball_x, ball_y = width // 2, height // 2

# Score
left_score, right_score = 0, 0

# Fonts
score_font = pygame.font.Font(None, 36)

def draw_paddles():
    pygame.draw.rect(screen, white, (20, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (width - 30, right_paddle_y, paddle_width, paddle_height))

def draw_ball():
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

def draw_score():
    left_text = score_font.render(str(left_score), True, white)
    screen.blit(left_text, (width // 4, 20))
    right_text = score_font.render(str(right_score), True, white)
    screen.blit(right_text, (width * 3 // 4, 20))

def check_collision():
    global ball_speed_x, ball_speed_y, left_score, right_score
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        ball_speed_y = -ball_speed_y
    if ball_x - ball_radius <= 30 and left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
        ball_speed_x = -ball_speed_x
    elif ball_x + ball_radius >= width - 30 and right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
        ball_speed_x = -ball_speed_x
    elif ball_x - ball_radius < 0:
        right_score += 1
        reset_ball()
    elif ball_x + ball_radius > width:
        left_score += 1
        reset_ball()

def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x, ball_y = width // 2, height // 2
    ball_speed_x, ball_speed_y = random.choice([4, -4]), random.choice([4, -4])

# Main game loop
running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y - paddle_speed > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y + paddle_speed < height - paddle_height:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y - paddle_speed > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y + paddle_speed < height - paddle_height:
        right_paddle_y += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    check_collision()
    draw_paddles()
    draw_ball()
    draw_score()

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
