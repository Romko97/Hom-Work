import pygame
from math import pow
from math import sqrt
pygame.init()
DISPLA_WIDTH = 600
DISPLA_HEIGH = 600
screen = pygame.display.set_mode((DISPLA_WIDTH, DISPLA_HEIGH))
pygame.display.set_caption("Hello world!")
X = 200
Y = 200
width = 100
height = 100
vol = 1
run = True

X1 = 300
Y1 = 300
width1 = 100
height1 = 100
X3 = X1
Y3 = Y1
width3 = (X1+width1) - (X + width1)
height3 = (Y1+height1) - (Y+height)

clock = pygame.time.Clock()
while run:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
  
    r = 0
    g = 0
    b = 255
    r1 = 255
    g1 = 0
    b1 = 0
    r3 = 0
    g3 = 0
    b3 = 0
    keyboard = pygame.key.get_pressed()
    if keyboard[pygame.K_LEFT] and X > 0:
        X -= vol
        X1 += vol
    if keyboard[pygame.K_RIGHT]and X < (DISPLA_HEIGH-width):
        X += vol
        X1 -= vol
    if keyboard[pygame.K_UP] and Y > 0:
        Y -= vol
        Y1 += vol
    if keyboard[pygame.K_DOWN] and Y < (DISPLA_HEIGH-height):
        Y += vol
        Y1 -= vol

    distance_XY_X1Y1 = sqrt(pow(X1 - X, 2) + pow(Y1-Y, 2))
    diagonalXY = sqrt(pow(width, 2) + pow(height, 2))

    if distance_XY_X1Y1 < diagonalXY:
        pygame.draw.rect(screen, (r3, g3, b3), [X3, Y3, width3, height3])
    
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (r, g, b), [X, Y, width, height])
    pygame.draw.rect(screen, (r1, g1, b1), [X1, Y1, width1, height1])
    #pygame.draw.rect(screen, (r3, g3, b3), [X3, Y3, width3, height3])
    pygame.display.update()    
    clock.tick(60)  
