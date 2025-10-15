import os
from rich import print as pprint

class Utils:
    @staticmethod
    def clear_bash():
        os.system("cls")

    @staticmethod
    def wrong_entry():
        pprint("[red]Wrong entry, try again ![/red]")
