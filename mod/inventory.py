from enum import Enum

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