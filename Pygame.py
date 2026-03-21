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
        self.width = 15
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
        # Detects if hits the wall
        self.hit = False
        # Ball movement direction
        self.xdir = 5
        self.ydir = 7
    # Resets the ball position to middle
    def reset(self):    
        self.x = 400
        self.y = 400
        self.xdir = 5
        self.ydir = 7
        self.hit = False

    def draw(self):
        pygame.draw.circle(screen, ("#FFFFFF"), (self.x, self.y), 10)
    # Ball movement    
    def update(self):
        self.x += self.xdir
        self.y += self.ydir
        # Reset ball position to stay on screen for x position
        if self.x < 0:
            self.x = 0
            self.hit = True
        if self.x > SW:
            self.x = SW
            self.hit = True
        # Reset ball position to stay on screen for y position
        if self.y < 0:
            self.y = 0
            self.hit = True
        if self.y > SH:
            self.y = SH
            self.hit = True
        
        # If the ball hits the wall it changes direction
        if self.hit == True:
            if (self.x == SW):
                self.xdir *= -1
            if (self.y <= 0 or self.y >= SH):
                self.ydir *= -1
            self.hit = False
            
            # IMPLETEMENT SCORE SYSTEM IF X == 0 or X == SW MUST COME BACK
            if self.x <= 0:
                score.score1 += 1
                self.reset()
            if self.x >= SW:
                score.score2 += 1
                # TEMPORARILY LEAVE COMMENTED UNTIL CPU IS COMPLETE
                # self.reset()

# Sets up score class
class Score:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0


paddle = Paddle()
ball = Ball()
score = Score()

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









