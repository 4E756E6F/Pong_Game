import pygame
import sys


class Ball:
    def __init__(self, screen, color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.draw_ball()

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color,
                           (self.posX, self.posY), self.radius)


class Player:
    def __init__(self, screen, color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.draw_player()

    def draw_player(self):
        pygame.draw.rect(self.screen, self.color, (self.posX,
                                                   self.posY, self.width, self.height))


# ? MODULE INITIALIZER
pygame.init()

# ? CONSTANTS
WIDTH = 1280
HEIGHT = 960
BACKGROUND_COLOR = (32, 32, 32)
WHITE = (224, 224, 224)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PONG')


def paint_background():
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), width=2)


paint_background()

# ? OBJECTS
ball = Ball(screen, WHITE, WIDTH//2, HEIGHT//2, 15)
player_left = Player(screen, WHITE, 15, HEIGHT//2-60, 20, 120)
player_right = Player(screen, WHITE, WIDTH-20-15, HEIGHT//2-60, 20, 120)

# ? MAIN LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
