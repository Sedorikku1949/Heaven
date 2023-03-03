from enum import Enum

# Définis la taille de chaque entitée/tuile
CASE_SIZE = 64
CHECKBOX_SIZE = 42

TICKS_PER_SECONDS = 50
PLAYER_DIAGONAL_COEFF = 1.5
# 1.5 car on utilise l'opération suivante:
# v(n) = n // PLAYER_DIAGONAL_COEFF
# où n ∈ ]-∞; +∞[ et PLAYER_DIAGONAL_COEFF un nombre réel non nul



# Ces variables servent à dessiner, respectivement, une grille et un fond pour les tuiles
# Elles sont utilisées à des fins de débogages lors de nos sessions de développements
# Il n'est pas recommandé de les activer, des chutes du nombre de mises à jours par secondes est à prévoir !
DRAW_DEBUG_GRID = False
DRAW_DEBUG_BACKGROUND = False

# Ces variables servent à definir des couleurs, points de vies, unitées et données utiles au jeux en lui même
# Veuillez ne pas modifier ces variables pour une expérience plus immersive ^^
DEFAULT_PLAYER_LIFE = 20
DEFAULT_PLAYER_DEFENSE = 50
PLAYER_SHIELD_COLOR = (83, 165, 216)
PLAYER_LIFE_COLOR = (227, 49, 49)
PLAYER_START_COORDS = (-442, -1228)

class MenuCategories(Enum):
    NO_ONE = 0
    OPTIONS = 1
    COMMANDS = 2
    SUCCESS = 3