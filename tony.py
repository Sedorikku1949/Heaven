import pygame, sys
from pytmx.util_pygame import load_pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
tmx_data = load_pygame('./map_test/carte.tmx')

running = True

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

screen.fill('black')
pygame.display.update