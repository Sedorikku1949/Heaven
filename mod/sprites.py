import pygame
from math import *
from typing import List, Tuple
from enum import Enum

from mod.assets import Assets
from mod.camera import *
from constants import *

class Movement(Enum):
    UP = 0
    UP_RIGHT = 1
    UP_LEFT = 2
    LEFT = 3
    RIGHT = 4
    BOTTOM_RIGHT = 5
    BOTTOM_LEFT = 6
    BOTTOM = 7

class SpriteType(Enum):
    PLAYER = 0
    SPIRIT = 1

class Sprite:
    def __init__(self, life: int, name: str, type: SpriteType, asset: str = "") -> None:
        self.life = life
        self.name = name
        self.type = type
        self.asset = asset

        self.movement = Movement.BOTTOM


class Player(Sprite):
    def __init__(self, x = 0, y = 0) -> None:
        super().__init__(10, "Player", SpriteType.PLAYER)

        self.idling = True
        self.ticks = 0

        self.x = x
        self.y = y

        self.animation_frame = 0
        self.MAX_ANIMATION_FRAME = 4
        self.last_movement_tick = 0

    def get_movement_animation(self) -> str:
        if self.idling:
            if self.movement == Movement.LEFT:
                return "player_left_idle"
            elif self.movement == Movement.RIGHT:
                return "player_right_idle"
            elif self.movement in [Movement.UP, Movement.UP_LEFT, Movement.UP_RIGHT]:
                return "player_up_idle"
            else:
                return "player_down_idle"
        else:
            if self.movement == Movement.LEFT:
                return f"player_left_{self.animation_frame}"
            elif self.movement == Movement.RIGHT:
                return f"player_right_{self.animation_frame}"
            elif self.movement in [Movement.UP, Movement.UP_LEFT, Movement.UP_RIGHT]:
                return f"player_up_{self.animation_frame}"
            else:
                return f"player_down_{self.animation_frame}"

    def draw(self, screen: pygame.Surface, assets: Assets, camera: Camera):
        player_surface = assets.get(self.get_movement_animation())
        if not (player_surface is None):
            screen.blit(
                        player_surface,
                        (
                            (screen.get_width() // 2) - (CASE_SIZE // 2),
                            (screen.get_height() // 2) - (CASE_SIZE // 2) 
                        )
                    )

    def move(self, movement: Movement, vector: Tuple[int, int], camera: Camera):
        self.last_movement_tick = self.ticks

        if movement != self.movement:
            self.movement = movement
        
        if self.idling:
            self.idling = False
        
        self.x += vector[0]
        camera.x += vector[0]
        
        self.y += vector[1]
        camera.y += vector[1]

    
    def update(self, frequence: pygame.time.Clock):
        self.ticks += 1

        if self.ticks % 6 == 0:
            self.animation_frame = (self.animation_frame + 1) % self.MAX_ANIMATION_FRAME

        if (self.ticks - self.last_movement_tick >= 2) and (not self.idling):
            self.idling = True