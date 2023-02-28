from typing import Tuple
from constants import *

class Camera:
    def __init__(self, coords: Tuple[int, int] = PLAYER_START_COORDS) -> None:
        self.x = coords[0]
        self.y = coords[1]
        self.speed = 6 // 2
        self.DEFAULT_SPEED = 6