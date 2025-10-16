from entities.player.player import Player

class Mage(Player):
    def __init__(self, name: str, max_hp: int, max_mana: int, armor: int) -> None:
        super().__init__(name, max_hp, armor)
        self.set_classname: str = 'Mage'
        self.set_color: str = 'blue3'
        self.__max_mana: int = max_mana
        self.__current_mana: int = self.max_mana

    @property
    def max_mana(self) -> int:
        return self.__max_mana

    @property
    def current_mana(self) -> int:
        return self.__current_mana

    @current_mana.setter
    def add_mana(self, value) -> None:
        self.__current_mana += value

    @current_mana.deleter
    def reduce_mana(self, value) -> None:
        self.__current_mana -= value
