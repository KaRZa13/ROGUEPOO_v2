from ..gameplay.inventory import Inventory

class Character:
    def __init__(self, name, max_hp, armor):
        self.__name = name
        self.__max_hp = max_hp
        self.__current_hp = self.max_hp
        self.__armor = armor
        self.__attack_inventory = []
        self.__inventory = Inventory()
        
    

