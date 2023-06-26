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

clock = pygame.time.Clock()
FPS = 120

BG = (50, 50, 50)

space  = pymunk.Space()
space.gravity = (0, 5000)
static_body = space.static_body

draw_options = pymunk.pygame_util.DrawOptions(screen)

def create_ball(radius, pos):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = 5
    space.add(body, shape)

    return shape

new_ball = create_ball(25, (300, 300)) # x and y
new1_ball = create_ball(25, (600, 300)) # x and y

run = True

while run:
    screen.fill(BG)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_ball.body.apply_impulse_at_local_point((-2200,0), (0,110))

        if event.type == pygame.QUIT:
            run = False

    clock.tick(FPS)
    space.step(1 / FPS)
    space.debug_draw(draw_options)
    pygame.display.update()

pygame.quit()