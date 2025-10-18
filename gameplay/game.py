import json
from time import sleep

# Classes
from utils.utils import Utils
from utils.menu_handler import MenuHandler
from data.assets.ascii.ascii_titles import AsciiTitles
from data.assets.dialogs_legacy import Dialogs
from entities.player.classes.warrior import Warrior
from entities.player.classes.mage import Mage
from entities.player.classes.rogue import Rogue

# Constants
from utils.config import RARITY_COLORS

class Game:
    def __init__(self):
        self.player = None
        self.current_menu = None
        self.menu_handler = MenuHandler()

        with open('data/assets/json/dialogs.json', 'r', encoding='utf-8') as f:
            self.dialogs = json.load(f)

    def start(self):
        Utils.clear_bash()
        options = [
            ("Load a save", "blue3"),
            ("Start a new game", "dark_green")
        ]
        choice = self.menu_handler.select_option(options, self.dialogs["new_game"], self.current_menu)

        if choice == 0:
            # Load a save
            pass
        elif choice == 1:
            return self.create_character()
        elif choice is None:
            quit()

    def create_character(self):
        Utils.clear_bash()
        AsciiTitles.main_title()
        name = str(input("\nChoose your name : "))

        options = [
            ("Warrior", "dark_red"),
            ("Mage", "blue3"),
            ("Rogue", "dark_green")
        ]

        choice = self.menu_handler.select_option(options, self.dialogs["choose_class"], self.current_menu)
        match choice:
            case 0:
                self.player = Warrior(name, 30, 2)
            case 1:
                self.player = Mage(name, 30, 2)
            case 2:
                self.player = Rogue(name, 30, 2)
            case _:
                return self.create_character()
        self.current_menu = 'village'
        return self.main_menu()

    def main_menu(self):
        options = [
            ("New adventure", "dark_green"),
            ("See the inventory", "dark_red"),
            ("Go to shop", "blue3"),
            ("Save and quit", "grey66")
        ]

        hud = self.dialogs["hud"].format(player=self.player)
        choice = self.menu_handler.select_option(options, self.dialogs["main_menu"], hud, self.current_menu)
        match choice:
            case 0:
                self.new_adventure()
            case 1:
                self.current_menu ='inventory'
                return self.inventory_menu()
            case 2:
                self.current_menu = 'shop'
                return self.shop_menu()
            case 3:
                # TODO Save the game
                AsciiTitles.bye()
                sleep(3)
                Utils.clear_bash()
                quit()
            case _:
                quit()

    def display_context_menu(self, context_menu):
        AsciiTitles.main_title()
        match context_menu:
            case 'village':
                AsciiTitles.village_title()
            case 'inventory':
                AsciiTitles.inventory_title()
            case 'dungeon':
                AsciiTitles.dungeon_title()
            case 'cave':
                AsciiTitles.cave_title()
            case 'shop':
                AsciiTitles.shop_title()
            case _:
                pass
        Dialogs.hud(self.player)

    def inventory_menu(self):
        self.display_context_menu(self.__current_menu)

    def shop_menu(self):
        options = [
            ("Swords", "dark_red"),
            ("Staffs", "blue3"),
            ("Daggers", "dark_green"),
            ("Shields", "dark_magenta"),
            ("Helmets", "purple4"),
            ("Chestplates", "purple4"),
            ("Leggings", "purple4"),
            ("Boots", "purple4"),
            ("Potions", "bright_green"),
            ("Back to village", "grey66")
        ]

        hud = self.dialogs["hud"].format(player=self.player)
        choice = self.menu_handler.select_option(options, self.dialogs["shop_menu"], hud, self.current_menu)

        match choice:
            case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8:
                self.shop_section(choice)
            case 9:
                self.current_menu = 'village'
                return self.main_menu()
            case _:
                quit()

    def shop_section(self, section):
        pass


    def new_adventure(self):
        pass
