from rich.pretty import pprint

class Dialogs:
    @staticmethod
    def new_game():
        print('Hi adventurer! It\'s been a while ! \n What do you want to do ?')
        pprint(' - 1 : [blue]Load a save[/blue]')
        pprint(' - 2 : [green]Start a new game[/green]')

    @staticmethod
    def choose_class():
        pprint(' \n Choose your class : \n')
        pprint(' - 1 : [red]Warrior[/red]')
        pprint(' - 2 : [blue]Mage[/blue]')
        pprint(' - 3 : [green]Rogue[/green] \n \n')

    @staticmethod
    def hud(player):
        pprint(f'[{player.color}]{player.name}[/{player.color}] : {player.hp}/{player.max_hp} ❤️ - {player.gold} 🪙 \n \n ')

    @staticmethod
    def main_menu():
        pprint(' \n Where do you want to go ? : \n')
        pprint(' - 1 : [green]New adventure[/green]')
        pprint(' - 2 : [red]See the inventory[/red]')
        pprint(' - 3 : [blue]Go to shop[/blue] \n \n \n')
        pprint('\n - 4 : [yellow1]Save and quit[/yellow1]')

    def new_adventure():
        pprint(' \n Choose your destination : \n')
        pprint(' - 1 : [green]The dungeon[/green]')
        pprint(' - 2 : [red]The endless cave[/red]')