from entities.items.item import Item

class Armor(Item):
    def __init__(self, name, description, durability, tier, value, armor_modifier):
        super().__init__(name, description, durability, tier, value)
        self.armor_modifier = armor_modifier