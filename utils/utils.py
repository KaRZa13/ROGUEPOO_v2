import os
from rich.pretty import pprint

class Utils:
    @staticmethod
    def clear_bash():
        os.system("cls")

    @staticmethod
    def wrong_entry():
        pprint("[red]Wrong entry, try again ![/red]")
