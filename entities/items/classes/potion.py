from entities.items.item import Item

class Potion(Item):
    def __init__(self, name, description, durability, tier, value, heal_amount):
        super().__init__(name, description, durability, tier, value)
        self.heal_amount = heal_amount