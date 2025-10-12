from time import sleep
from ..utils.utils import Utils
from ..data.assets.ascii.ascii_title import AsciiTitles
from ..data.assets.dialogs import Dialogs
from ..entities.classes.warrior import Warrior
from ..entities.classes.mage import Mage
from ..entities.classes.rogue import Rogue

class Game:
    def __init__(self):
        self.__player = None
        self.__current_menu = None

    @property
    def player(self):
        return self.__player

    @property
    def current_menu(self):
        return self.__current_menu

    @player.setter
    def player(self, value):
        self.__player = value

    @current_menu.setter
    def current_menu(self, value):
        self.__current_menu = value

    def match_menu(self, choice):
        match choice:
            case 1:
                self.current_menu('village')
            case 2:
                self.current_menu('dungeon')
            case 3:
                self.current_menu('cave')
            case 4:
                self.current_menu('shop')
            case _:
                Utils.wrong_entry()
                sleep(3)
                return self.main_menu()

    def match_shop_menu(self, choice):
        pass

    def display_hud(self, current_menu):
        Utils.clear_bash()
        AsciiTitles.main_title()
        


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
        return self.main_menu()

    def main_menu(self):
        Utils.clear_bash()
        AsciiTitles.main_title()
        # ASCII village title
        Dialogs.hud(self.player)
        Dialogs.main_menu()
        choice = int(input("Your choice : "))
        match choice:
            case 1:
                # inventaire
                pass
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