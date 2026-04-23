from pathlib import Path
import sys
from colorama import Fore
from tree import show_structure


def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Specify the path to the directory.")
        return

    dir_path = Path(sys.argv[1])

    if not dir_path.exists() or not dir_path.is_dir():
        print(Fore.RED + "Incorrect path")
        return

    print(Fore.YELLOW + f"📦 {dir_path.name}")

    show_structure(dir_path)


if __name__ == "__main__":
    main()