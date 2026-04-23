from pathlib import Path
from colorama import Fore


def show_structure(path: Path) -> None:
    try:
        for item in path.iterdir():

            if item.is_dir():
                print(Fore.BLUE + f"📁 {item.name}")

                for sub_item in item.iterdir():
                    if sub_item.is_dir():
                        print(Fore.BLUE + f" ┣ 📁 {sub_item.name}")
                    else:
                        print(Fore.GREEN + f" ┃ ┣ 📜 {sub_item.name}")

            else:
                print(Fore.GREEN + f"📜 {item.name}")

    except PermissionError:
        print(Fore.RED + "No access")