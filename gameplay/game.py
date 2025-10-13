from time import sleep
from utils.utils import Utils
from data.assets.ascii.ascii_titles import AsciiTitles
from data.assets.dialogs import Dialogs
from entities.classes.warrior import Warrior
from entities.classes.mage import Mage
from entities.classes.rogue import Rogue

class Game:
    def __init__(self):
        self.__player = None
        self.__current_menu = None

    @property
    def get_player(self):
        return self.__player

    @property
    def get_current_menu(self):
        return self.__current_menu

    @get_player.setter
    def player(self, value):
        self.__player = value

    @get_current_menu.setter
    def set_current_menu(self, value):
        self.__current_menu = value

    def match_menu(self, choice):
        match choice:
            case 1:
                self.set_current_menu('village')
            case 2:
                self.set_current_menu('dungeon')
            case 3:
                self.set_current_menu('cave')
            case 4:
                self.set_current_menu('shop')
            case _:
                Utils.wrong_entry()
                sleep(3)
                return self.main_menu()

    def match_shop_menu(self, choice):
        pass

    def display_context_menu(self, context_menu):
        Utils.clear_bash()
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

    def start(self):
        Utils.clear_bash()
        AsciiTitles.main_title()
        Dialogs.new_game()
        choice = int(input("Your choice : "))
        if choice == 1:
            # Load a save
            pass
        elif choice == 2:
            return self.create_character()
        else:
            return self.start()

    def create_character(self):
        Utils.clear_bash()
        AsciiTitles.main_title()
        name = str(input("Choose your name : "))
        Dialogs.choose_class()
        choice = int(input("Your choice : "))
        match choice:
            case 1:
                self.player = Warrior(name)
            case 2:
                self.player = Mage(name)
            case 3:
                self.player = Rogue(name)
            case _:
                Utils.wrong_entry()
                sleep(3)
                return self.create_character()
        self.set_current_menu('village')
        return self.main_menu()

    def main_menu(self):
        self.display_context_menu(self.__current_menu)
        Dialogs.main_menu()
        choice = int(input("Your choice : "))
        match choice:
            case 1:
                self.set_current_menu('inventory')
                return self.inventory_menu()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case _:
                Utils.wrong_entry()
                sleep(3)
                return self.main_menu()
            

    def inventory_menu(self):
        self.display_context_menu(self.__current_menu)
        