import json
from constants import CASE_SIZE
from mod.map import Map, EntitiesContainer, Entity, Tile, Layer
from typing import Tuple, List
from mod.assets import IDS_FROM_SAVE, IDS_ASSETS
import pygame

def open_file(dir: str) -> str | None:
    with open("map.json", "r") as file:
        return json.load(file)

def convert_tiled_to_map(tiled_json, screen: pygame.Surface) -> Map:
    map = Map()
    return map
    for layer_data in tiled_json["layers"]:
        layer = Layer(layer_data["id"])
        for i, tile_data in enumerate(layer_data["data"]):
            x, y = i % layer_data["width"], i // layer_data["width"]
            if tile_data:
                tileset = next(tileset for tileset in tiled_json["tilesets"] if tile_data >= tileset["firstgid"])

                if tile_data in IDS_ASSETS:
                    asset = IDS_ASSETS[tile_data]
                    tile = Tile(asset)
                else:
                    tile = Tile(str(tile_data))
                layer.map[(x * CASE_SIZE, y * CASE_SIZE)] = tile

                if not(tile_data in IDS_FROM_SAVE):
                    IDS_FROM_SAVE.append(tile_data)
        map.layers[layer_data["id"]] = layer
    return map