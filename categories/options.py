import pygame
from constants import *
from typing import List, Tuple

class Options:
    def __init__(self) -> None:
        
        self.FONT_40 = pygame.font.Font("./RetroGaming.ttf", 40)
        self.FONT_30 = pygame.font.Font("./RetroGaming.ttf", 30)
        self.FONT_25 = pygame.font.Font("./RetroGaming.ttf", 25)
        self.FONT_20 = pygame.font.Font("./RetroGaming.ttf", 20)
        
        self.esc_to_close = self.FONT_20.render("[ECHAP] pour quitter ce menu", True, (240, 240, 240))
        self.dev_mode = self.FONT_20.render("Mode développeur", True, (240, 240, 240))

        self.actual_page = 0

        # mode développeur
        self.show_dev_page = False
        self.DEV_KEYS = 0

    def draw(self, screen: pygame.Surface):
        screen_width, screen_height = screen.get_size()

        # Fond
        pygame.draw.rect(
            screen,
            (0,0,0,0),
            (
                100,
                100,
                screen_width - 200,
                screen_height - 200
            ),
            border_radius=25
        )
        pygame.draw.rect(
            screen,
            (20, 20, 20),
            (
                100,
                100,
                screen_width - 200,
                self.esc_to_close.get_height() + 40
            ),
            border_top_left_radius=25,
            border_top_right_radius=25
        )

        # Instruction pour revenir en arrière
        screen.blit(self.esc_to_close, (145, 120))

        # Mode dev:
        if self.show_dev_page:
            screen.blit(
                self.dev_mode,
                (
                    screen_width - 145 - self.dev_mode.get_width(),
                    120
                )
            )


        #
        #   Dessin de la page
        # 
        # Catégories:
        # - Général (FPS, Coords, VSYNC)
        # - Dev(GRID, DEBUG_BACKGROUND, CASE_SIZE)
        #

        self.checkbox(
            screen,
            (125, screen_height // 2),
            "Blep",
            True
        )

        self.checkbox(
            screen,
            (125, screen_height * 0.75),
            "Blep 2",
            False
        )

    def checkbox(self, screen: pygame.Surface, coords: Tuple[int, int], name: str, v: bool, color = (255, 255, 255)):
        checkbox = pygame.Surface((CHECKBOX_SIZE + 4, CHECKBOX_SIZE + 4))
        checkbox.fill((0,0,0))
        pygame.draw.rect(
            checkbox,
            (255, 255, 255),
            (0, 0, CHECKBOX_SIZE, CHECKBOX_SIZE)
        )
        
        pygame.draw.rect(
            checkbox,
            (0, 0, 0),
            (4, 4, CHECKBOX_SIZE - 8, CHECKBOX_SIZE - 8)
        )
        
        if v:
            pygame.draw.rect(
                checkbox,
                color,
                (8, 8, CHECKBOX_SIZE - 16, CHECKBOX_SIZE - 16)
            )

        screen.blit(checkbox, coords)

        text = self.FONT_30.render(name, True, color)
        screen.blit(
            text,
            (
                coords[0] + CHECKBOX_SIZE + 20,
                coords[1]
            )
        )

    def reset_options_interface(self):
        pass

    def update(self, frequence: pygame.time.Clock):
        
        keys = pygame.key.get_pressed()
        if (not self.show_dev_page) and keys[pygame.K_h] and keys[pygame.K_e] and keys[pygame.K_a] and keys[pygame.K_v] and keys[pygame.K_n]:
            self.show_dev_page = True

    def key_down(self, event):
        if event.key == pygame.K_e:
            self.DEV_KEYS += 1
            if self.DEV_KEYS >= 5:
                self.show_dev_page = True


options: Options = Options()