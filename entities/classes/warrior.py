from entities.player import Player

class Warrior(Player):
    def __init__(self, name: str, max_hp: int, armor: int) -> None:
        super().__init__(name, max_hp, armor)
        self.set_classname: str = 'Warrior'
        self.set_color: str = 'dark_red'