import pygame
from typing import Tuple

def draw_image(screen: pygame.Surface, sfc: pygame.Surface, coords: Tuple[int, int]):
    screen.blit(sfc, coords)