import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init()

WIDTH = 1200
HEIGHT = 640
PANEL = 50 

screen = pygame.display.set_mode((WIDTH, HEIGHT + PANEL))
pygame.display.set_caption("8 POOL BY Hisham")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()