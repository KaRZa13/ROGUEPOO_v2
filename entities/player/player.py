from entities.inventory import Inventory

class Player:
    def __init__(self, name, max_hp, armor):
        self.name = name
        self.classname = ''
        self.color = ''
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.armor = armor
        self.attack_inventory = []
        self.inventory = Inventory()
        self.gold = 0

    def is_alive(self):
        return self.current_hp > 0

    def take_damage(self, amount):
        self.set_current_hp(self.current_hp - amount)
