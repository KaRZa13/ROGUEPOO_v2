import os

RARITY_LEVELS = {
    "Common" : "white",
    "Uncommon" : "green4",
    "Rare" : "blue1",
    "Epic" : "purple",
    "Legendary" : "yellow1",
    "Mythic" :  "red1",
}


class Utils:
    @staticmethod
    def clear_bash():
        os.system("cls")