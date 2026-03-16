import pygame

# Initialise pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((640,640))
pygame.display.set_caption("My First Game")
random_pic = pygame.image.load(r"C:\Users\cjand\OneDrive\Desktop\Python ML Work\Learning Material\PIC.png").convert()

random_pic = pygame.transform.scale(random_pic, (400, 522)) 
# Game Loop
running = True

x = 0
clock = pygame.time.Clock()

while running:
    # creates a white background for screen
    screen.fill((255, 255, 255)) # RGB for white
    # blit draws an image on screen aka pictures
    screen.blit(random_pic, (x, 30))
    
    x += 1
    #determines how many fps game will run at
    clock.tick(60) # 60 fps 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

# Quit pygame
pygame.quit()

