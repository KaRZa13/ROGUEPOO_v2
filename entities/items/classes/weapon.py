from entities.items.item import Item

class Weapon(Item):
    def __init__(self, name, description, durability, tier, value, attack_modifier):
        super().__init__(name, description, durability, tier, value)
        self.attack_modifier = attack_modifier