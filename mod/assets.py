import pygame
from math import *
from typing import List, Tuple

class Assets:
    """Store all assets that can be drawed in the game"""
    def __init__(self) -> None:
        """Drink your coffee while pygame is loading each assets, nothing to do but to wait"""
        self.assets = {}

    def get(self, key: str) -> pygame.Surface: # | None
        """Get an asset from a key"""
        if key in self.assets.keys():
            return self.assets[key]

    def draw_centered(self, target: pygame.Surface, surface: pygame.Surface, coords: Tuple[int, int]):
        """
        Allow game draw handler to draw an asset centered by the coordinates given (with multiple assets size)
        """
        surface_size = surface.get_size()
        target.blit(
            surface,
            (
                coords[0] - (surface_size[0] // 4),
                coords[1] - (surface_size[1] // 4)
            ) # (x, y)
        )

class GameAssets(Assets):
    def __init__(self) -> None:
        super().__init__()
        self.assets = {
            "rock1": pygame.image.load("design/game/objects/08.png", "rock1"), # "assets/rock1"
            "rock2": pygame.image.load("design/game/objects/00.png", "rock2"), # "assets/rock2"
            "test_grass": pygame.image.load("design/game/test/5.png", "test_grass"),
            "test_sprite": pygame.image.load("design/game/monsters/spirit/idle/0.png"),
            
            # Player animation with movements

            "player_down_idle": pygame.image.load("design/game/player/down_idle/idle_down.png", "player_down_idle"), # "assets/player.png"
            "player_down_0": pygame.image.load("design/game/player/down/down_0.png", "player_down_0"),
            "player_down_1": pygame.image.load("design/game/player/down/down_1.png", "player_down_1"),
            "player_down_2": pygame.image.load("design/game/player/down/down_2.png", "player_down_2"),
            "player_down_3": pygame.image.load("design/game/player/down/down_3.png", "player_down_3"),
            
            "player_left_idle": pygame.image.load("design/game/player/left_idle/idle_left.png", "player_down_idle"),
            "player_left_0": pygame.image.load("design/game/player/left/left_0.png", "player_left_0"),
            "player_left_1": pygame.image.load("design/game/player/left/left_1.png", "player_left_1"),
            "player_left_2": pygame.image.load("design/game/player/left/left_2.png", "player_left_2"),
            "player_left_3": pygame.image.load("design/game/player/left/left_3.png", "player_left_3"),
            
            "player_right_idle": pygame.image.load("design/game/player/right_idle/idle_right.png", "player_right_idle"),
            "player_right_0": pygame.image.load("design/game/player/right/right_0.png", "player_right_0"),
            "player_right_1": pygame.image.load("design/game/player/right/right_1.png", "player_right_1"),
            "player_right_2": pygame.image.load("design/game/player/right/right_2.png", "player_right_2"),
            "player_right_3": pygame.image.load("design/game/player/right/right_3.png", "player_right_3"),
            
            "player_up_idle": pygame.image.load("design/game/player/up_idle/idle_up.png", "player_up_idle"),
            "player_up_0": pygame.image.load("design/game/player/up/up_0.png", "player_up_0"),
            "player_up_1": pygame.image.load("design/game/player/up/up_1.png", "player_up_1"),
            "player_up_2": pygame.image.load("design/game/player/up/up_2.png", "player_up_2"),
            "player_up_3": pygame.image.load("design/game/player/up/up_3.png", "player_up_3"),
        }