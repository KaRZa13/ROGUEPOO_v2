from ..gameplay.inventory import Inventory

class Player:
    def __init__(self, name, max_hp):
        self.__name = name
        self.__classname = ''
        self.__max_hp = max_hp
        self.__current_hp = self.max_hp
        self.__attack_inventory = []
        self.inventory = Inventory()
        self.__gold = 0

    def __str__(self):
        return f'I\'m {self.name}, I\'m a {self.classname} I\'ve got {self.current_hp} ❤️ and {self.gold} 🪙.'

    def is_alive(self):
        return self.current_hp > 0

    def take_damage(self, amount):
        self.set_current_hp(self.current_hp - amount)

    @property
    def name(self):
        return self.__name

    @property
    def classname(self):
        return self.__classname

    @property
    def max_hp(self):
        return self.__max_hp

    @property
    def current_hp(self):
        return self.__current_hp

    @property
    def attack_inventory(self):
        return self.__attack_inventory

    @property
    def gold(self):
        return self.__gold

    @classname.setter
    def set_classname(self, value):
        self.__classname = value

    @current_hp.setter
    def set_current_hp(self, value):
        self.__current_hp = value

    @attack_inventory.setter
    def set_attack_inventory(self, value):
        self.__attack_inventory.append(value)

    @attack_inventory.deleter
    def del_attack_inventory(self, value):
        self.__attack_inventory.remove(value)

    @gold.setter
    def set_gold(self, value):
        self.__gold += value

    @gold.deleter
    def del_gold(self, value):
        self.__gold -= value