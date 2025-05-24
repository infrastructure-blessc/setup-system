from colorama import Fore, Style, init
init(autoreset=True)

def log_step(message):
    print(f"{Fore.CYAN}[➤] {message}")

def log_info(message):
    print(f"{Fore.GREEN}[✔] {message}")

def log_error(message):
    print(f"{Fore.RED}[✖] {message}")
