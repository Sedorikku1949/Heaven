# Bugs rencontrés

Au cours de la programmation et conception de notre projet final de NSI, nous avons rencontrés divers bugs et problèmes plus ou moins contraignants

## Voici une liste non exhaustive:

- Camera vs Joueur: Le joueur et la camera n'étaient pas copains, leurs coordonnées divergeaient
- Les fenêtres provoquaient un bug en étant modifiées: Quand on changeait la taille de la fenêtre (hauteur ou largeur), la carte se déplacait mais pas le joueur; Il a fallu appliquer un coeff delta (Δn) où on déplace la carte de (Δn // 2)