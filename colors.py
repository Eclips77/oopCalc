# colors.py
from colorama import init, Fore, Style

init(autoreset=True) 

class Colors:
    @staticmethod
    def error(text):
        return Fore.RED + Style.BRIGHT + text

    @staticmethod
    def success(text):
        return Fore.GREEN + text

    @staticmethod
    def warning(text):
        return Fore.YELLOW + text

    @staticmethod
    def info(text):
        return Fore.CYAN + text

    @staticmethod
    def title(text):
        return Fore.MAGENTA + Style.BRIGHT + text
