from utils.config import RARITY_COLORS

class Item:
    def __init__(self, name, description, durability, tier, value, item_type):
        self.name = name
        self.description = description
        self.durability = durability
        self.tier = tier
        self.tier_color = RARITY_COLORS.get(self.tier, "white")
        self.value = value
        self.item_type = item_type
        self.item_class = self.__class__.__name__