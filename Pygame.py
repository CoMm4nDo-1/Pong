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
        self.x = 200
        self.y = 200
        self.width = 20
        self.height = 100
        self.color = ("#FFFFFF")
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)

paddle = Paddle()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #determines how many fps game will run at
    clock.tick(10) # 60 fps     




