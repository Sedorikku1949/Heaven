from constants import *

def fps_coeff(fps: int) -> float:
    """
    Renvoit un coefficient du nombre de mises à jours par secondes
    le résultat sera toujours compris dans l'interval ]0; 1]
    [!] Le résultat est automatiquement géré selon la constante `TICKS_PER_SECONDS`
    """
    coeff = fps / TICKS_PER_SECONDS
    if coeff >= 1: return 1
    else: return coeff