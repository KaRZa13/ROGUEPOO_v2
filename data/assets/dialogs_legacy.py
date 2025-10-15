from rich import print

class Dialogs:
    @staticmethod
    def new_game():
        print('\n\nHi adventurer ! It\'s been a while ! \nWhat do you want to do ?')

    @staticmethod
    def choose_class():
        print(' \n Choose your class : \n')
        print(' - 1 : [dark_red]Warrior[/dark_red]')
        print(' - 2 : [blue3]Mage[/blue3]')
        print(' - 3 : [dark_green]Rogue[/dark_green] \n \n')

    @staticmethod
    def hud(player):
        print(f'\n[{player.color}]{player.name}[/{player.color}] : {player.current_hp}/{player.max_hp} ❤️ - {player.gold} 🪙 \n \n ')

    @staticmethod
    def main_menu():
        print(' \n Where do you want to go ? : \n')
        print(' - 1 : [dark_green]New adventure[/dark_green]')
        print(' - 2 : [dark_red]See the inventory[/dark_red]')
        print(' - 3 : [blue3]Go to shop[/blue3]')
        print('\n - 4 : [yellow1]Save and quit[/yellow1]\n')

    def new_adventure():
        print(' \n Choose your destination : \n')
        print(' - 1 : [dark_green]The dungeon[/dark_green]')
        print(' - 2 : [dark_red]The endless cave[/dark_red]')