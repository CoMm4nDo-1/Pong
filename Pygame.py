from cmath import rect

import pygame
import sys


# Initialise pygame
pygame.init()
SW, SH = 800, 800

# Set up the screen
screen = pygame.display.set_mode((SW,SH))
pygame.display.set_caption("Pong!")


clock = pygame.time.Clock()

# Defines class of paddle
class Paddle:
    def __init__(self):
        # Starting position x and y
        self.x = 0
        self.y = 0
        # Direction of movement in y direction (up and down)
        self.ydir = 0
        # Size of the paddle
        self.width = 20
        self.height = 85
        # Color of the paddle
        self.color = ("#FFFFFF")
    def draw(self):
        # draws the paddle on the screen    
        rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rectangle)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 15
        elif keys[pygame.K_s]:
            self.y += 15
        elif keys[pygame.K_DOWN]:
            self.y += 15
        elif keys[pygame.K_UP]:
            self.y -= 15

# Defines ball class
class Ball:
    def __init__(self):
        # Ball starting position
        self.x = 400
        self.y = 400
    def draw(self):
        circle = pygame.draw.circle(screen, ("#FFFFFF"), (self.x, self.y), 10)
 
paddle = Paddle()
ball = Ball()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fills screen with black to erase previous frames
    screen.fill("black")
    paddle.draw()
    paddle.move()
    ball.draw()

    #determines how many fps game will run at
    clock.tick(60) # 60 fps
    #updates the screen
    pygame.display.update()






