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
        # Size of the paddle
        self.width = 20
        self.height = 85
        # Color of the paddle
        self.color = ("#FFFFFF")

    def draw(self):
        # draws the paddle on the screen    
        rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        # Sets boundaries for paddle 
        boundaries = rectangle.clamp(screen.get_rect(size=(SW, SH)))
        pygame.draw.rect(screen, self.color, boundaries)

    def move(self):
        keys = pygame.key.get_pressed()
        # Moves the paddle up and down with W and S or UP and DOWN keys
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= 15
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += 15
        # Reset y position to stay on screen
        if self.y < 0:
            self.y = 0
        if self.y > SH - self.height:
            self.y = SH - self.height
        
# Defines ball class
class Ball:
    def __init__(self):
        # Ball starting position
        self.x = 400
        self.y = 400
    def draw(self):
        pygame.draw.circle(screen, ("#FFFFFF"), (self.x, self.y), 10)
    # Ball movement    
    def update(self):
        self.x += 5
        self.y += 5

 
paddle = Paddle()
ball = Ball()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fills screen with black to erase previous frames
    screen.fill("black")
    paddle.move()
    paddle.draw()
    ball.update()
    ball.draw()

    #determines how many fps game will run at
    clock.tick(45) # 45 fps
    #updates the screen
    pygame.display.update()









