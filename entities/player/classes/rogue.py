from entities.player.player import Player

class Rogue(Player):
    def __init__(self, name: str, max_hp: int, armor: int) -> None:
        super().__init__(name, max_hp, armor)
        self.set_classname: str = 'Rogue'
        self.set_color: str = 'dark_green'