import pygame
from math import *
from typing import List, Tuple
from enum import Enum

from mod.assets import Assets
from mod.camera import *
from constants import *
from mod.utils import *

class Movement(Enum):
    UP = 0
    UP_RIGHT = 1
    UP_LEFT = 2
    LEFT = 3
    RIGHT = 4
    BOTTOM_RIGHT = 5
    BOTTOM_LEFT = 6
    BOTTOM = 7

class SpriteType(Enum):
    PLAYER = 0
    SPIRIT = 1

class Entity:
    def __init__(self, coords: Tuple[int, int], life: int,  type: SpriteType, asset: str = "") -> None:
        self.x = coords[0]
        self.y = coords[1]

        self.life = life
        self.type = type
        self.asset = asset

        self.movement = Movement.BOTTOM

    def move_x(self, x: int) -> None:
        self.coords[0] += x

    def move_y(self, y: int) -> None:
        self.coords[1] += y

#
#
#   INVENTAIRE
#
#

class ItemType(Enum):
    WOOD = 0
    WOOD_SWORD = 1

    def __repr__(self) -> str:
        return str(self)

class Item:
    def __init__(self, asset: str, type: ItemType, quantity: int = 1) -> None:
        self.quantity = quantity
        self.asset = asset
        self.type = type
    
    def edit_stocks(self, n: int) -> bool:
        """
        Ajoute ou retire une partie du stock
        Si "op" est négatif, alors la quantité sera réduire
        Si "op" est positif, alors la quantité sera augmentée
        """
        if self.quantity + n < 0:
            return False
        else:
            self.quantity += n
            return True
        
    def __repr__(self) -> str:
        return f"[{self.type}; {self.asset}]({self.quantity})"
        
class Wood(Item):
    def __init__(self, quantity: int = 1) -> None:
        super().__init__("item_wood", ItemType.WOOD, quantity)

class WoodSword(Item):
    def __init__(self, damage = 10, durability = 100) -> None:
        super().__init__("item_wood_sword", ItemType.WOOD_SWORD, 1)

        self.damage = damage
        self.durability = durability

class Inventory:
    def __init__(self) -> None:
        self.items = {}
    
    def add_item(self, item: Item, force = False) -> bool:
        if not(item.type in self.items.keys()) or force:
            self.items[item.type] = item
            return True
        return False
    
    def remove_item(self, type: ItemType):
        if (type in self.items.keys()):
            del self.items[type]

    def __repr__(self) -> str:
        return str(self.items)




class Player(Entity):
    def __init__(
            self,
            coords: Tuple[int, int] = PLAYER_START_COORDS,
            layer: int = 0,
            name: str = "Player",
            defense: int = DEFAULT_PLAYER_DEFENSE,
            life: int = DEFAULT_PLAYER_LIFE
        ) -> None:
            super().__init__(coords, life, SpriteType.PLAYER, "")
            
            self.DEFAULT_LIFE = life
            self.DEFAULT_DEFENSE = defense
            self.fps = -1

            self.layer = layer
            self.name = name
            self.defense = defense
    
            self.idling = True
            self.ticks = 0

            self.animation_frame = 0
            self.MAX_ANIMATION_FRAME = 4
            self.last_movement_tick = 0

            self.inventory = Inventory()
            self.current_item = WoodSword()
            self.inventory_open = False

    def get_movement_animation(self) -> str:
        if self.idling or self.inventory_open:
            if self.movement == Movement.LEFT:
                return "player_left_idle"
            elif self.movement == Movement.RIGHT:
                return "player_right_idle"
            elif self.movement in [Movement.UP, Movement.UP_LEFT, Movement.UP_RIGHT]:
                return "player_up_idle"
            else:
                return "player_down_idle"
        elif not self.inventory_open:
            if self.movement == Movement.LEFT:
                return f"player_left_{self.animation_frame}"
            elif self.movement == Movement.RIGHT:
                return f"player_right_{self.animation_frame}"
            elif self.movement in [Movement.UP, Movement.UP_LEFT, Movement.UP_RIGHT]:
                return f"player_up_{self.animation_frame}"
            else:
                return f"player_down_{self.animation_frame}"
            
    def is_health_bars_needed(self, map, coords: Tuple[int, int]) -> bool:
        return True
    
    def draw_remaining_defense(self, x: int, y: int, screen: pygame.Surface, player_surface: pygame.Surface):
        pygame.draw.rect(
            screen,
            (0,0,0),
            (
                x - 35 + (player_surface.get_width() // 2),
                y + 17 - (player_surface.get_height() // 2),
                70,
                9
            )
        )
        pygame.draw.rect(
            screen,
            PLAYER_SHIELD_COLOR,
            (
                x - 34 + (player_surface.get_width() // 2),
                y + 18 - (player_surface.get_height() // 2),
                floor(68 * (self.defense / self.DEFAULT_DEFENSE)),
                7
            )
        )
    
    def draw_remaining_life(self, x: int, y: int, screen: pygame.Surface, player_surface: pygame.Surface):
        pygame.draw.rect(
            screen,
            (0,0,0),
            (
                x - 35 + (player_surface.get_width() // 2),
                y + 5 - (player_surface.get_height() // 2),
                70,
                9
            )
        )
        pygame.draw.rect(
            screen,
            PLAYER_LIFE_COLOR,
            (
                x - 34 + (player_surface.get_width() // 2),
                y + 6 - (player_surface.get_height() // 2),
                floor(68 * (self.life / self.DEFAULT_LIFE)),
                7
            )
        )

    def draw_current_item(self, screen: pygame.Surface, player_surface: pygame.Surface, x: int, y: int, assets: Assets):
        # dessiner le cadre
        in_hand_asset = assets.get("in_hand")
        if not(in_hand_asset is None):
            screen.blit(
                in_hand_asset,
                (10, screen.get_height() - 10 - (in_hand_asset.get_height()))
            )

        # dessiner l'item
        if not(self.current_item is None):
            current_item_surface = assets.get(self.current_item.asset)
            if not(current_item_surface is None):
                
                #pygame.draw.rect(
                #    screen,
                #    (255, 0, 0),
                #    (
                #    10 + (124 - in_hand_asset.get_width()) + (in_hand_asset.get_width() // 4),
                #    screen.get_height() - 10 - (124 - in_hand_asset.get_height()) - (in_hand_asset.get_height()) - (124 // -4),
                #    64, 64
                #    )
                #)

                screen.blit(
                    current_item_surface,(
                        10 + (124 - in_hand_asset.get_width()) + (in_hand_asset.get_width() // 4),
                        screen.get_height() - 10 - (124 - in_hand_asset.get_height()) - (in_hand_asset.get_height()) - (124 // -4)
                    )
                )

    def draw(self, screen: pygame.Surface, assets: Assets, camera: Camera, map):
        player_surface = assets.get(self.get_movement_animation())
        x = (screen.get_width() // 2) - (CASE_SIZE // 2) + (player_surface.get_width() // 2)
        y = (screen.get_height() // 2) - (CASE_SIZE // 2) + (player_surface.get_height() // 2)
        if not (player_surface is None):
            screen.blit(player_surface, (x, y))
            # draw life & defense bar
            self.draw_remaining_defense(x, y, screen, player_surface)
            self.draw_remaining_life(x, y, screen, player_surface)
        
        self.draw_current_item(screen, player_surface, x, y, assets)
    
    def move(self, movement: Movement, vector: Tuple[int, int], camera: Camera, fps: int):
        if self.inventory_open:
            return

        self.last_movement_tick = self.ticks

        if movement != self.movement:
            self.movement = movement
        
        if self.idling:
            self.idling = False
        
        self.x += vector[0] / fps_coeff(fps)
        camera.x += vector[0] / fps_coeff(fps)
        
        self.y += vector[1] / fps_coeff(fps)
        camera.y += vector[1] / fps_coeff(fps)
    
    def update(self, frequence: pygame.time.Clock):
        self.fps = frequence.get_fps()

        self.ticks += 1

        if floor(self.ticks) % 15 == 0:
            self.animation_frame = (self.animation_frame + 1) % self.MAX_ANIMATION_FRAME

        if (self.ticks - self.last_movement_tick >= 2) and (not self.idling):
            self.idling = True



class Spirit(Entity):
    def __init__(self, x = 0, y = 0) -> None:
        super().__init__((x, y), 5, SpriteType.SPIRIT, "test_spirit")
    
    def update(self, frequence: pygame.time.Clock):
        pass

    def draw(self, screen: pygame.Surface, assets: Assets, camera: Camera):
        player_surface = assets.get(self.asset)
        if not (player_surface is None):
            screen.blit(
                        player_surface,
                        (
                            self.x + (screen.get_width() // 2) - (CASE_SIZE // 2) + camera.x,
                            self.y + (screen.get_height() // 2) - (CASE_SIZE // 2) + camera.y
                        )
                    )