import pygame
from math import *
from typing import List, Tuple
from enum import Enum

from mod.assets import Assets
from mod.entities import Player, Entity
from mod.map import Map

class UiAssets(Assets):
    def __init__(self) -> None:
        self.assets = {
            "inventory": pygame.image.load("assets/ui/inventory.png").convert_alpha(),
        }

        self.fonts = {
            "RETRO_10": pygame.font.Font("./RetroGaming.ttf", 10),
            "RETRO_20": pygame.font.Font("./RetroGaming.ttf", 20),
            "RETRO_30": pygame.font.Font("./RetroGaming.ttf", 30),
            "RETRO_40": pygame.font.Font("./RetroGaming.ttf", 40),
        }


    def get(self, key: str) -> pygame.Surface: # | None
        """Get an asset from a key"""
        if key in self.assets.keys():
            return self.assets[key]

    def get_font(self, font_name: str, size: int) -> pygame.Surface: # | None
        """Get an asset from a key"""
        name = f"{font_name}_{size}"
        if name in self.fonts.keys():
            return self.fonts[name]

class UiDrawArguments:
    def __init__(self, player: Player, assets: UiAssets, screen: pygame.Surface) -> None:
        self.player = player
        self.assets = assets
        self.screen = screen

    def get(self) -> Tuple[Player, UiAssets, pygame.Surface]:
        return (self.player, self.assets, self.screen)


class Component:
    pass

class MessageComponentType(Enum):
    BUTTON = 1 # Boutons
    SELECT_MENU = 2 # Menu de sélection (drop down)
    MODAL = 3 # Boite de dialogue avec entrée de texte

class GameMessageComponent:
    def __init__(self, label: str, onclick: int, type) -> None:
        self.label = label
        self.onclick = onclick
    
class GameMessageButton(GameMessageComponent):
    def __init__(self, label: str, onclick: int) -> None:
        super().__init__(label, onclick)

class GameMessageStyle(Enum):
    CLASSIC = 1

    def get_color(self) -> Tuple[int, int, int]:
        if self == GameMessageStyle.CLASSIC:
            return (240, 240, 240)

class GameMessage(Component):
    """Class afin de gérer l'intégration de message dans """
    def __init__(self, text: str, relativeCoordinates: Tuple[int, int], style: GameMessageStyle = GameMessageStyle.CLASSIC, components: List[GameMessageComponent] = []) -> None:
        """
        Créer un nouveau message grâce à un texte, des coordonées relatives et à un style
        [!] Les coordonnées relatives sont basées sur l'écran, pas sur la carte! 
        """
        self.message = text
        self.coords = relativeCoordinates
        self.style = style
        self.componentys = components

    def draw(self, game: UiDrawArguments):
        player, assets, screen = game.get()

        text = assets.get_font("RETRO", 20).render(
            self.message
                .replace("{fps}", str(floor(player.fps)))
                .replace("{x}", str(round(player.x)))
                .replace("{y}", str(round(player.y))),
            True,
            self.style.get_color()
        )

        width, height = text.get_size()

        screen.blit(
            text,
            self.coords
        )


        pass

    def update(self, frequence: pygame.time.Clock, player: Player):
        pass



class UI:
    def __init__(self) -> None:
        self.components: List[Component] = []

        self.components.append(GameMessage("fps: {fps}; ({x}, {y})", (5, 5), GameMessageStyle.CLASSIC, ))

    def draw(self, game: UiDrawArguments) -> None:
        for cmp in self.components:
            cmp.draw(game)

        if game.player.inventory_open:
            # dessiner l'interface de l'inventaire
            self.draw_inventory(game)

    def draw_inventory(self, game: UiDrawArguments):
        player, assets, screen = game.get()
        asset = assets.get("inventory")
        if asset is None: return;
    
        # On rajoute un fond légèrement noir
        back_surface = pygame.Surface(screen.get_size())
        back_surface.set_alpha(128)
        back_surface.fill((0,0,0))

        screen.blit(back_surface, (0,0))

    
        # Dessiner l'emplacement de la case où seront les items        
        screen.blit(
            asset,
            (
                (screen.get_width() // 2) - (asset.get_width() // 2),
                (screen.get_height() // 2) - (asset.get_height() // 2) 
            )
        )

    def update(self, frequence: pygame.time.Clock, player: Player, map: Map):
        for cmp in self.components:
            cmp.update(frequence, player)