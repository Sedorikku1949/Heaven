from math import *
from typing import List, Tuple
from enum import Enum

from mod.assets import Assets
from mod.camera import *
from constants import *
from mod.utils import *

class Movement(Enum):
    UP = 0
    UP_RIGHT = 1
    UP_LEFT = 2
    LEFT = 3
    RIGHT = 4
    BOTTOM_RIGHT = 5
    BOTTOM_LEFT = 6
    BOTTOM = 7

class EntityType(Enum):
    PLAYER = 0
    SPIRIT = 1
    COMPANION = 2

class Entity:
    def __init__(self, coords: Tuple[int, int], life: int,  type: EntityType, asset: str = "") -> None:
        self.x = coords[0]
        self.y = coords[1]

        self.life = life
        self.type = type
        self.asset = asset

        self.movement = Movement.BOTTOM

    def move_x(self, x: int) -> None:
        self.coords[0] += x

    def move_y(self, y: int) -> None:
        self.coords[1] += y
