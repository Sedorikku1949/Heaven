from typing import Tuple
from constants import *

class Camera:
    def __init__(self, coords: Tuple[int, int] = PLAYER_START_COORDS, speed = DEFAULT_PLAYER_SPEED) -> None:
        self.x = coords[0]
        self.y = coords[1]
        self.speed = speed
        self.DEFAULT_SPEED = speed