import pygame
# import pytmx
# import pyscroll
from math import *
from constants import *

from mod.ui import *
from mod.sprites import *
from mod.assets import *
from mod.map import *
from mod.camera import *

#
#
#       GAME
#
#
 

class Game:
    def __init__(self) -> None:
        self.map = Map()
        self.sprites_map = SpriteMap()
        self.camera = Camera()
        self.assets = GameAssets()
        self.ui_assets = UiAssets()


        # TEST


        self.map.add_layer(0)
        self.map.insert_tile(0, (0, 0), Tile("test_grass"))
        self.map.insert_tile(0, (-CASE_SIZE*1.5, 0), Tile("rock1"))
        self.map.insert_tile(0, (CASE_SIZE, 2 * CASE_SIZE), Tile("rock2"))


        # Blep
        self.player = Player()
        self.ui = UI()

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((0, 0, 0))

        self.map.draw(screen, self.assets, self.camera)
        self.sprites_map.draw(screen, self.assets, self.camera)
        self.player.draw(screen, self.assets, self.camera)
        self.ui.draw(UiDrawArguments(self.player, self.ui_assets, screen))

    def update(self, frequence: pygame.time.Clock) -> None:
        self.movements(frequence)

        self.player.update(frequence)
        self.ui.update(frequence, self.player, self.sprites_map)
    
    def movements(self, frequence: pygame.time.Clock) -> None:
        keys = pygame.key.get_pressed()

        # On vérifie chaque touche (z, q, s, d) pour connaitre le mouvement précis

        if keys[pygame.K_z] and not(keys[pygame.K_q] or keys[pygame.K_d]):
            # move only up
            self.player.move(Movement.UP, (0, self.camera.speed), self.camera)
        elif keys[pygame.K_z] and keys[pygame.K_q] and (not keys[pygame.K_d]):
            # move up left
            self.player.move(Movement.UP_LEFT, (self.camera.speed, self.camera.speed), self.camera)
        elif keys[pygame.K_z] and (not keys[pygame.K_q]) and keys[pygame.K_d]:
            # move up right
            self.player.move(Movement.UP_RIGHT, (-self.camera.speed, self.camera.speed), self.camera)
        elif keys[pygame.K_q] and not(keys[pygame.K_z] or keys[pygame.K_s]):
            # move only left
            self.player.move(Movement.LEFT, (self.camera.speed, 0), self.camera)
        elif keys[pygame.K_d] and not(keys[pygame.K_z] or keys[pygame.K_s]):
            # move only right
            self.player.move(Movement.RIGHT, (-self.camera.speed, 0), self.camera)
        elif keys[pygame.K_s] and not(keys[pygame.K_q] or keys[pygame.K_d]):
            # move only bottom
            self.player.move(Movement.BOTTOM, (0, -self.camera.speed), self.camera)
        elif keys[pygame.K_s] and keys[pygame.K_q] and (not keys[pygame.K_d]):
            # move bottom left
            self.player.move(Movement.BOTTOM_LEFT, (self.camera.speed, -self.camera.speed), self.camera)
        elif keys[pygame.K_s] and (not keys[pygame.K_q]) and keys[pygame.K_d]:
            # move bottom right
            self.player.move(Movement.BOTTOM_RIGHT, (-self.camera.speed, -self.camera.speed), self.camera)