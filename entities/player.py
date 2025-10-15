from gameplay.inventory import Inventory

class Player:
    def __init__(self, name: str, max_hp: int, armor: int) -> None:
        self.__name: str = name
        self.__classname: str = ''
        self.__color: str = ''
        self.__max_hp: int = max_hp
        self.__current_hp: int = self.max_hp
        self.__armor: int = armor
        self.__attack_inventory = []
        self.inventory: object = Inventory()
        self.__gold: int = 0

    def is_alive(self) -> bool:
        return self.current_hp > 0

    def take_damage(self, amount) -> None:
        self.set_current_hp(self.current_hp - amount)

    # region Getters and Setters
    @property
    def name(self) -> str:
        return self.__name

    @property
    def classname(self) -> str:
        return self.__classname

    @property
    def color(self) -> str:
        return self.__color

    @property
    def max_hp(self) -> int:
        return self.__max_hp

    @property
    def current_hp(self) -> int:
        return self.__current_hp

    @property
    def armor(self) -> int:
        return self.__armor

    @property
    def attack_inventory(self) -> list:
        return self.__attack_inventory

    @property
    def gold(self) -> int:
        return self.__gold

    @classname.setter
    def set_classname(self, value) -> None:
        self.__classname = value

    @color.setter
    def set_color(self, value) -> None:
        self.__color = value

    @current_hp.setter
    def set_current_hp(self, value) -> None:
        self.__current_hp = value

    @armor.setter
    def set_armor(self, value) -> None:
        self.__armor = value

    @attack_inventory.setter
    def set_attack_inventory(self, value) -> None:
        self.__attack_inventory.append(value)

    @attack_inventory.deleter
    def del_attack_inventory(self, value) -> None:
        self.__attack_inventory.remove(value)

    @gold.setter
    def set_gold(self, value) -> None:
        self.__gold += value

    @gold.deleter
    def del_gold(self, value) -> None:
        self.__gold -= value

    # endregion