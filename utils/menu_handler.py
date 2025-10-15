from blessed import Terminal
from rich import print as rprint
from data.assets.ascii.ascii_titles import AsciiTitles
from data.assets.dialogs_legacy import Dialogs

class MenuHandler:
    def __init__(self):
        self.term = Terminal()

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
        # Dialogs.hud(self.player)

    def select_option(self, options, title=None, context_menu=None):
        """
        Affiche un menu avec navigation au clavier
        Args:
            options: Liste de tuples (label, color)
                    ex: [("Warrior", "dark_red"), ("Mage", "blue3")]
            title: Titre du menu
        Returns:
            Index de l'option sélectionnée (commence à 0)
        """

        selected = 0

        with self.term.cbreak(), self.term.hidden_cursor():
            while True:
                print(self.term.home + self.term.clear, end='')
                self.display_context_menu(context_menu)
                print(f"\n{title}\n")
                
                # Afficher les options
                for i, (label, color) in enumerate(options):
                    if i == selected:
                        # Option sélectionnée avec un curseur
                        rprint(f"  → [{color}]{label}[/{color}]")
                    else:
                        rprint(f"    [{color}]{label}[/{color}]")
                
                rprint("\n[dim]↑/↓: Navigate | Enter: Select | Q: Quit[/dim]")
                
                # Capturer l'input
                key = self.term.inkey()
                
                if key.name == 'KEY_UP':
                    selected = (selected - 1) % len(options)
                elif key.name == 'KEY_DOWN':
                    selected = (selected + 1) % len(options)
                elif key.name == 'KEY_ENTER':
                    return selected
                elif key.lower() == 'q':
                    return None