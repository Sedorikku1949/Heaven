import pygame
from math import *
from typing import List, Tuple

from constants import CASE_SIZE

IDS_FROM_SAVE = []

IDS_ASSETS = {
    4: "sign_top_left",
    5: "sign_top_right",
    44: "sign_bottom_left",
    45: "sign_bottom_right",
    322: "grass_1_5",
    323: "grass_1_6",
    362: "grass_10_3",
    324: "grass_10_3",
    603: "grass_15_3",
    333: "grass_16_3",
    284: "grass_34_9",
    285: "grass_34_9",
    250: "grass_34_9",
    325: "grass_34_9",
    334: "grass_34_9",
    242: "grass_34_10",
    405: "grass_33_9",
    403: "grass_33_9",
    402: "grass_33_9",
    408: "grass_33_9",
}

class Assets:
    """Store all assets that can be drawed in the game"""
    def __init__(self) -> None:
        """Drink your coffee while pygame is loading each assets, nothing to do but to wait"""
        self.assets = {}

    def get(self, key: str) -> pygame.Surface: # | None
        """Get an asset from a key"""
        if key in self.assets.keys():
            return self.assets[key]

    #def draw_centered(self, target: pygame.Surface, surface: pygame.Surface, coords: Tuple[int, int]):
    #    """
    #    Allow game draw handler to draw an asset centered by the coordinates given (with multiple assets size)
    #    """
    #    surface_size = surface.get_size()
    #    target.blit(
    #        surface,
    #        (
    #            coords[0] - (surface_size[0] // 4),
    #            coords[1] - (surface_size[1] // 4)
    #        ) # (x, y)
    #    )

class GameAssets(Assets):
    def __init__(self) -> None:
        super().__init__()
        self.assets = {
            "rock1": pygame.image.load("design/game/objects/08.png", "rock1").convert_alpha(), # "assets/rock1"
            "rock2": pygame.image.load("design/game/objects/00.png", "rock2").convert_alpha(), # "assets/rock2"
            "test_grass": pygame.image.load("design/game/test/5.png", "test_grass").convert_alpha(),
            "test_spirit": pygame.image.load("design/game/monsters/spirit/idle/0.png").convert_alpha(),
            # "grass_1_5": pygame.transform.scale(pygame.image.load("assets/map/image1x5.png"), (CASE_SIZE, CASE_SIZE)).convert_alpha(),
            # "grass_1_6": pygame.transform.scale(pygame.image.load("assets/map/image1x6.png"), (CASE_SIZE, CASE_SIZE)).convert_alpha(),
            # "grass_10_3": pygame.transform.scale(pygame.image.load("assets/map/image3x10.png"), (CASE_SIZE, CASE_SIZE)).convert_alpha(),
            # "grass_15_3": pygame.transform.scale(pygame.image.load("assets/map/image3x15.png"), (CASE_SIZE, CASE_SIZE)).convert_alpha(),
            # "grass_16_3": pygame.transform.scale(pygame.image.load("assets/map/image3x16.png"), (CASE_SIZE, CASE_SIZE)).convert_alpha(),
            # "grass_34_9": pygame.transform.scale(pygame.image.load("assets/map/image34x9.png"), (CASE_SIZE, CASE_SIZE)).convert_alpha(),
            # "grass_34_10": pygame.transform.scale(pygame.image.load("assets/map/image34x10.png"), (CASE_SIZE, CASE_SIZE)).convert_alpha(),
            # "grass_33_9": pygame.transform.scale(pygame.image.load("assets/map/image33x9.png"), (CASE_SIZE, CASE_SIZE)).convert_alpha(),
            
            # UI
            "in_hand": pygame.transform.scale(pygame.image.load("assets/in_hand.png"), (124, 124)).convert_alpha(),
            "item_wood_sword": pygame.transform.scale(pygame.image.load("assets/items/wood_sword.png"), (CASE_SIZE, CASE_SIZE)).convert_alpha(),

            # Map:
            "map_tuto": pygame.transform.scale(pygame.image.load("carte.png"), (400*4, 400*4)),


            # Player animation with movements

            "player_down_idle": pygame.image.load("design/game/player/down_idle/idle_down.png", "player_down_idle").convert_alpha(), # "assets/player.png"
            "player_down_0": pygame.image.load("design/game/player/down/down_0.png", "player_down_0").convert_alpha(),
            "player_down_1": pygame.image.load("design/game/player/down/down_1.png", "player_down_1").convert_alpha(),
            "player_down_2": pygame.image.load("design/game/player/down/down_2.png", "player_down_2").convert_alpha(),
            "player_down_3": pygame.image.load("design/game/player/down/down_3.png", "player_down_3").convert_alpha(),
            
            "player_left_idle": pygame.image.load("design/game/player/left_idle/idle_left.png", "player_down_idle").convert_alpha(),
            "player_left_0": pygame.image.load("design/game/player/left/left_0.png", "player_left_0").convert_alpha(),
            "player_left_1": pygame.image.load("design/game/player/left/left_1.png", "player_left_1").convert_alpha(),
            "player_left_2": pygame.image.load("design/game/player/left/left_2.png", "player_left_2").convert_alpha(),
            "player_left_3": pygame.image.load("design/game/player/left/left_3.png", "player_left_3").convert_alpha(),
            
            "player_right_idle": pygame.image.load("design/game/player/right_idle/idle_right.png", "player_right_idle").convert_alpha(),
            "player_right_0": pygame.image.load("design/game/player/right/right_0.png", "player_right_0").convert_alpha(),
            "player_right_1": pygame.image.load("design/game/player/right/right_1.png", "player_right_1").convert_alpha(),
            "player_right_2": pygame.image.load("design/game/player/right/right_2.png", "player_right_2").convert_alpha(),
            "player_right_3": pygame.image.load("design/game/player/right/right_3.png", "player_right_3").convert_alpha(),
            
            "player_up_idle": pygame.image.load("design/game/player/up_idle/idle_up.png", "player_up_idle").convert_alpha(),
            "player_up_0": pygame.image.load("design/game/player/up/up_0.png", "player_up_0").convert_alpha(),
            "player_up_1": pygame.image.load("design/game/player/up/up_1.png", "player_up_1").convert_alpha(),
            "player_up_2": pygame.image.load("design/game/player/up/up_2.png", "player_up_2").convert_alpha(),
            "player_up_3": pygame.image.load("design/game/player/up/up_3.png", "player_up_3").convert_alpha(),
        }
    
    def load_images(self):
        pass
        #  folder_path = "assets/map"
        #  # Créer une liste de noms de fichiers triés par ordre alphabétique
        #  files = sorted([os.fsdecode(filename) for filename in os.listdir(folder_path)])
        #
        #  # Déterminer le nombre maximal de colonnes dans les images
        #  max_x = max([int(filename.split("x")[0].replace("image", "")) for filename in files])
        #
        #  for filename in files:
        #      if filename.endswith(".png"):
        #          # Extraire les nombres du nom de fichier en ignorant la chaîne "image"
        #          x, y = map(int, filename.replace("image", "").replace(".png", "").split("x"))
        #          # Calculer l'index à partir des deux nombres extraits
        #          index = y * (max_x + 1) + x
        #          print(f"Image {filename} has dimensions {x} x {y} and index {index}")

    #    print(IDS_FROM_SAVE)
    #    image = pygame.image.load("natureset.png")
    #    tile_width, tile_height = 16, 16  # la largeur et la hauteur de chaque image dans l'image globale
    #    n = 0
    #    for i in range(0, image.get_height() - tile_height, tile_height):
    #        for j in range(0, image.get_width() - tile_width, tile_width):
    #            # Extraire un sous-rectangle de la surface pour chaque image
    #            rect = pygame.Rect(j, i, tile_width, tile_height)
    #            tile_image = image.subsurface(rect)
    #            # Ajouter l'image à l'ensemble des assets avec une clé unique
    #            if not(n in IDS_ASSETS):
    #                self.assets[n] = tile_image
    #            else:
    #                self.assets[IDS_ASSETS[n]] = tile_image
    #            print(n)
    #            n += 1
