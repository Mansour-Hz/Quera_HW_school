import keyboard as kb
from utils import *
import threading
from Models import Library

# Flag to control returning to the main menu
return_to_main_menu = threading.Event()


def handle_ctrl_b():
    return_to_main_menu.set()
    print("\nCtrl+B detected, returning to the main menu...\n")


def menu_main(library):
    while True:
        return_to_main_menu.clear()

        print("\n1. Add Books")
        print("2. Find Books")
        print("3. Display all books")
        print("4. Remove Book")
        print("5. Update Book")
        print("6. Save Books to file")
        print("7. Retrieve Books from file")
        print("8. Exit")

        choice = input("Choose one option: ")

        if return_to_main_menu.is_set():
            continue

        match choice:
            case '1':
                add_book(library, return_to_main_menu)
            case '2':
                find_books(library, return_to_main_menu)
            case '3':
                display_books(library, return_to_main_menu)
            case '4':
                remove_book(library, return_to_main_menu)
            case '5':
                update_book(library, return_to_main_menu)
            case '6':
                save_books(library, return_to_main_menu)
            case '7':
                retrieve_books(library, return_to_main_menu)
            case '8':
                print("Come back soon...")
                heartPrinter()
                break
            case _:
                print("Invalid choice.")

        # Check if Ctrl+B was pressed during the operation
        if return_to_main_menu.is_set():
            continue


if __name__ == "__main__":
    kb.add_hotkey("ctrl+b", handle_ctrl_b)

    library = Library()
    menu_main(library)
