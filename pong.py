import pygame
import sys


# ? GENERAL SETUP
pygame.init()
clock = pygame.time.Clock()

# ? SETTING UP THE MAIN WINDOW
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('PONG')

# ? GAME RECTANGLES
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

bg_color = (64, 64, 64)
whitish = (224, 224, 224)

ball_speed_x = 10
ball_speed_y = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # ? VISUALS
    screen.fill(bg_color)
    pygame.draw.rect(screen, whitish, player)
    pygame.draw.rect(screen, whitish, opponent)
    pygame.draw.ellipse(screen, (51, 153, 255), ball)
    pygame.draw.aaline(screen, whitish, (screen_width / 2, 0),
                       (screen_width / 2, screen_height))
    # ? UPDATING THE WINDOW
    clock.tick(60)
