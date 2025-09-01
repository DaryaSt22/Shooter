import sys

import pygame
from pygame.examples.go_over_there import screen

# from random import randint

# clock = pygame.time.Clock()

pygame.init()

screen_width, screen_height = 800, 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My Pygame")
fill_color = (32, 52, 71)

rect_width, rect_height = 100, 200
rect_x = screen_width / 2 - rect_width / 2
rect_y = screen_height / 2 - rect_height / 2
rect_color = pygame.Color('lightyellow')

step = 10

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rect_y = rect_y - step
            if event.key == pygame.K_DOWN:
                rect_y = rect_y + step
            if event.key == pygame.K_LEFT:
                rect_x = rect_x - step
            if event.key == pygame.K_RIGHT:
                rect_x = rect_x + step

    # screen.fill(pygame.Color('blue'))
    # screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
    screen.fill(fill_color)
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()
    # clock.tick(5)
