from ..player import Player

class Warrior(Player):
    def __init__(self, name, max_hp, armor):
        super().__init__(name, max_hp, armor)
        self.set_classname = 'Warrior'