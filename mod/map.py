import pygame
from math import *
from typing import List, Tuple

from constants import *
from mod.assets import Assets, GameAssets
from mod.sprites import Sprite
from mod.camera import *

class Tile:
    def __init__(self, asset: str) -> None:
        self.asset = asset

class Layer:
    def __init__(self, y: int) -> None:
        self.map = {}
        self.y = y

    def insert(self, coords: Tuple[int, int], tile: Tile):
        if not (coords in self.map.keys()):
            self.map[coords] = tile
    
    def replace(self, coords: Tuple[int, int], tile: Tile):
        if (coords in self.map.keys()):
            self.map[coords] = tile
    
    def add_or_replace(self, coords: Tuple[int, int], tile: Tile):
        self.map[coords] = tile

    def remove(self, coords: Tuple[int, int]):
        del self.map[coords]
    
    def try_remove(self, coords: Tuple[int, int]):
        if coords in self.map.keys():
            self.remove(coords)

class Map:
    def __init__(self) -> None:
        self.layers = {}
        self.centered_assets = [] #["rock1", "rock2"] # Place name of assets wich need to be drawed centered from the coordinates given

    def add_layer(self, y: int) -> None:
        if not (y in self.layers.keys()):
            self.layers[y] = Layer(y)

    def remove_layer(self, y: int) -> None:
        if y in self.layers.keys():
            del self.layers[y]

    def get(self, y: int) -> Layer: # | None
        if y in self.layers.keys():
            return self.layers[y]

    def get_layers(self) : # -> list[Layer]
        l = list(self.layers.values())
        l.sort()
        return l

    def get_available_layers(self): # list[Layer]
        l = list(self.layers.values())
        l.sort()
        return l

    def insert_tile(self, layer: int, coords: Tuple[int, int], tile: Tile):
        if layer in self.layers.keys():
            return self.layers[layer].insert(coords, tile)
            
    def replace_tile(self, layer: int, coords: Tuple[int, int], tile: Tile):
        if layer in self.layers.keys():
            return self.layers[layer].replace(coords, tile)
            
    def add_or_replace(self, layer: int, coords: Tuple[int, int], tile: Tile):
        if layer in self.layers.keys():
            return self.layers[layer].replace(coords, tile)
            
    def remove(self, layer: int, coords: Tuple[int, int]):
        if layer in self.layers.keys():
            return self.layers[layer].replace(coords)
            
    def try_remove(self, layer: int, coords: Tuple[int, int]):
        if layer in self.layers.keys():
            return self.layers[layer].replace(coords)

    def draw_grid(self, screen: pygame.Surface, camera: Camera) -> pygame.Surface:
        if not DRAW_DEBUG_GRID:
            return

        screen_width, screen_height = screen.get_size()

        for x_index in range(-CASE_SIZE, ((screen_width % CASE_SIZE) + CASE_SIZE)):
            x = x_index * CASE_SIZE + camera.x + (CASE_SIZE // 2)
            for y_index in range(-CASE_SIZE, ((screen_height % CASE_SIZE) + CASE_SIZE)):
                y = y_index * CASE_SIZE + camera.y + (CASE_SIZE // 4) - 4
                pygame.draw.line(
                    screen,
                    (20, 20, 20),
                    (x, y),
                    (x + screen_width, y),
                    2
                )
                pygame.draw.line(
                    screen,
                    (20, 20, 20),
                    (x, y),
                    (x, y + screen_height),
                    2
                )




    def draw(self, screen: pygame.Surface, assets: Assets, camera: Camera) -> None:
        self.draw_grid(screen, camera)
        
        # test
        #rock = assets.get("rock1")
        #screen.blit(rock, (32, 32))
        screen_width, screen_height = screen.get_size()

        for layer in self.get_available_layers():
            items = layer.map.items()
            for (x, y), tile in items:
                # Nous calculons la coordonnée relative de la tuile
                x_pos, y_pos = (
                    x + camera.x + (screen_width // 2) - (CASE_SIZE // 2),
                    y + camera.y + (screen_height // 2) - (CASE_SIZE // 2) + (CASE_SIZE * layer.y)
                )

                # Cette valeur permettront de savoir si l'élément est affiché DANS l'écran
                x_encadrement = [camera.x - screen_width - CASE_SIZE, camera.x + screen_width + CASE_SIZE]
                y_encadrement = [camera.y - screen_height - CASE_SIZE, camera.y + screen_height + CASE_SIZE]

                # Si la surface est clairement en dehors de l'écran, on ne dessine pas pour optimiser les performances
                if (y > y_encadrement[0] and y < y_encadrement[1]) and (x > x_encadrement[0] and x < x_encadrement[1]):
                    surface = assets.get(tile.asset)
                    # Si la surface existe, alors on la dessine aux coordonnées calculées plus haut
                    if not (surface is None):
                        if DRAW_DEBUG_BACKGROUND:
                            pygame.draw.rect(screen, (0,255,0), (x_pos, y_pos, surface.get_width(), surface.get_height()))
                            
                        if tile.asset in self.centered_assets:
                            assets.draw_centered(screen, surface, (x_pos, y_pos))
                        else:
                            screen.blit(surface, (x_pos, y_pos))


#
#
#       SPRITES
#
#

class SpriteLayer:
    def __init__(self) -> None:
        pass

class SpriteMap:
    def __init__(self) -> None:
        pass

    def draw(self, frequence: pygame.time.Clock, assets: GameAssets, camera: Camera) -> None:
        pass