from typing import Tuple
from constants import *
from entities.mod import Movement

def fps_coeff(fps: int | float) -> float:
    """
    Renvoit un coefficient du nombre de mises à jours par secondes
    le résultat sera toujours compris dans l'interval ]0; 1]
    [!] Le résultat est automatiquement géré selon la constante `TICKS_PER_SECONDS`
    """
    coeff = float(fps) / UPDATE_TICKS
    if coeff >= 1: return 1
    else: return float(coeff)

def determine_collision_move(movement: Movement, axe: 0 | 1) -> Movement | None:
    """
    permet de savoir si l'axe demandé est dans le mouvement
    0 = x
    1 = y
    """
    if (movement in [Movement.UP, Movement.BOTTOM]):
        if axe == 0: return None
        else: return movement
    elif (movement in [Movement.RIGHT, Movement.LEFT]):
        if axe == 0: return movement
        else: return None
    elif (movement == Movement.UP_RIGHT):
        if axe == 0: return Movement.RIGHT
        else: return Movement.UP
    elif (movement == Movement.UP_LEFT):
        if axe == 0: return Movement.LEFT
        else: return Movement.UP
    elif (movement == Movement.BOTTOM_LEFT):
        if axe == 0: return Movement.LEFT
        else: return Movement.BOTTOM
    elif (movement == Movement.BOTTOM_RIGHT):
        if axe == 0: return Movement.RIGHT
        else: return Movement.BOTTOM

def determine_move(vec: Tuple[int, int]) -> Movement:
    if vec[0] > 0 and vec[1] == 0:
        return Movement.RIGHT
    elif vec[0] < 0 and vec[1] == 0:
        return Movement.LEFT
    elif vec[0] == 0 and vec[1] > 0:
        return Movement.UP
    elif vec[0] == 0 and vec[1] < 0:
        return Movement.BOTTOM
    elif vec[0] < 0 and vec[1] < 0:
        return Movement.BOTTOM_LEFT
    elif vec[0] > 0 and vec[1] < 0:
        return Movement.BOTTOM_RIGHT
    elif vec[0] < 0 and vec[1] > 0:
        return Movement.UP_LEFT
    elif vec[0] > 0 and vec[1] < 0:
        return Movement.UP_RIGHT
    else:
        return Movement.BOTTOM