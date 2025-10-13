from entities.player import Player

class Mage(Player):
    def __init__(self, name, max_hp, max_mana, armor):
        super().__init__(name, max_hp, armor)
        self.set_classname = 'Mage'
        self.__max_mana = max_mana
        self.__current_mana = self.max_mana

    @property
    def max_mana(self):
        return self.__max_mana

    @property
    def current_mana(self):
        return self.__current_mana

    @current_mana.setter
    def add_mana(self, value):
        self.__current_mana += value

    @current_mana.deleter
    def reduce_mana(self, value):
        self.__current_mana -= value
