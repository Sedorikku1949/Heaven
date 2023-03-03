import pygame
from constants import *
from typing import List, Tuple


class Commands:
    def __init__(self) -> None:
        
        self.FONT_40 = pygame.font.Font("./RetroGaming.ttf", 40)
        self.FONT_25 = pygame.font.Font("./RetroGaming.ttf", 25)
        self.FONT_20 = pygame.font.Font("./RetroGaming.ttf", 20)
        
        self.esc_to_close = self.FONT_20.render("[ECHAP] pour quitter ce menu", True, (240, 240, 240))


        self.pages = [
            {
                "name": "Général",
            }
        ]
        self.actual_page = 0