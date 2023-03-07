# Bugs rencontrés

Au cours de la programmation et conception de notre projet final de NSI, nous avons rencontrés divers bugs et problèmes plus ou moins contraignants

## Voici une liste non exhaustive:

- Camera vs Joueur: Le joueur et la camera n'étaient pas copains, leurs coordonnées divergeaient
- Les fenêtres provoquaient un bug en étant modifiées: Quand on changeait la taille de la fenêtre (hauteur ou largeur), la carte se déplacait mais pas le joueur; Il a fallu appliquer un coeff delta (Δn) où on déplace la carte de (Δn // 2)
- A cause d'un problème de conditions, si on appuie sur une touche de direction (en l'occurence Z et S) et que la touche "SPACE" était ENSUITE enfoncée, le jeux se coupait. En réalité le jeux pensait que il était dans le menu de pause du jeux !
- Il est impossible de passer d'une fenêtre non fenetrée à une fenêtre en plein écran (et inversement). Cela a été résolu en quittant le display, redéfinissant le display puis en l'initialisant
- Chute de performances: En dessinant une image, nous perdions 30-40 images par secondes (10 mises à jours/s), cependant, grâce à la méthode convert_alpha sur les Surface, nous sommes capables de gagner BEAUCOUP de performances