import fnmatch
import os
from Models import Book, File

# Constants
title_year_author_dict = {'t': 'title', 'y': 'year', 'a': 'author'}


def get_input_with_interrupt(prompt, return_to_main_menu):
    while not return_to_main_menu.is_set():
        user_input = input(prompt)
        if return_to_main_menu.is_set():
            return None
        return user_input
    return None

def heartPrinter():
    for row in range(6):
        for col in range(7):
            if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def findAllTextFiles():

    current_dir = os.getcwd()
    txt_files = []

    for file in os.listdir(current_dir):
        if fnmatch.fnmatch(file, '*.txt'):
            txt_files.append(file)

    return txt_files


def add_book(library, return_to_main_menu):
    while True:
        title = get_input_with_interrupt("Book title: ", return_to_main_menu)
        if title is None:
            return
        if title.strip():
            break
        print("Title cannot be empty. Please enter a valid title.")

    while True:
        author = get_input_with_interrupt("Author: ", return_to_main_menu)
        if author is None:
            return
        if author.strip() and not any(char.isdigit() for char in author):
            break
        if not author.strip():
            print("Author cannot be empty. Please enter a valid author name.")
        else:
            print("Author name cannot contain numbers. Please enter a valid author name.")

    while True:
        year_input = get_input_with_interrupt(
            "Publish year: ", return_to_main_menu)
        if year_input is None:
            return
        if year_input.strip().isdigit():
            year = int(year_input)
            break
        print("Year must be a valid integer. Please enter a valid publish year.")

    library.add_book(Book(title.strip(), author.strip(), year))
    print(f"\nBook '{title}' by {author} (published in {year}) added successfully!")


def find_books(library, return_to_main_menu):
    query = get_input_with_interrupt(
        "Enter Author name or Book title: ", return_to_main_menu)
    if query is None:
        return

    by = get_input_with_interrupt(
        "Search book based on (title(t)/author(a)/year(y)): ", return_to_main_menu)
    if by is None:
        return

    if by not in title_year_author_dict:
        print("Invalid search option.")
        return

    results = library.search_books(query, title_year_author_dict[by])

    if return_to_main_menu.is_set():
        return

    if results:
        for book in results:
            print(f"{book.title} by {book.author}, {book.year}")
    else:
        print("No matching books found.")


def display_books(library, return_to_main_menu):
    
    if return_to_main_menu.is_set():
        return
    
    if not library.books:
        print("\nThere are no books in your library right now!")
    else:
        sort_by = input("Sort based on (title(t)/author(a)/year(y)): ")
        library.display_books(title_year_author_dict[sort_by])


def remove_book(library, return_to_main_menu):
    title = get_input_with_interrupt("Title of book to be removed: ", return_to_main_menu)
    if title is None:
        return
    library.remove_book(title)
    print(f"\nBook '{title}' removed from the library.")


def update_book(library, return_to_main_menu):
    old_title = get_input_with_interrupt(
        "Title of book to be updated: ", return_to_main_menu)
    if old_title is None:
        return

    new_title = get_input_with_interrupt(
        "New title (optional): ", return_to_main_menu)
    if new_title is None:
        return

    new_author = get_input_with_interrupt(
        "New author (optional): ", return_to_main_menu)
    if new_author is None:
        return

    new_year = get_input_with_interrupt(
        "New publish year (optional): ", return_to_main_menu)
    if new_year is None:
        return

    if new_year and not new_year.strip().isdigit():
        print("Publish year must be a valid integer.")
    else:
        new_year = int(new_year) if new_year and new_year.strip() else None

    library.update_book(old_title, new_title.strip() if new_title else None,
                        new_author.strip() if new_author else None, new_year)
    print(f"\nBook '{old_title}' updated successfully!")


def save_books(library, return_to_main_menu):
    if not os.path.exists(library.bookFile.fileName) or library.bookFile.fileName != "":
        inputName = get_input_with_interrupt("File name for storing books: ", return_to_main_menu)
        if inputName is None:
            return
        library.bookFile = File(inputName, os.path.curdir)
    library.save_to_file(library.bookFile.fileName)
    print(f"\nBooks saved to file '{library.bookFile.fileName}' successfully!")


def retrieve_books(library, return_to_main_menu):
    current_txt_files = findAllTextFiles()
    if not current_txt_files:
        print("There are no text files in the current directory.")
    else:
        print("\nThese text files are available in your current directory:\n")
        for index, file in enumerate(current_txt_files):
            print(index + 1, ". ", file)
        wantedIndex = int(get_input_with_interrupt("\nChoose the number of the file: ", return_to_main_menu))
        if wantedIndex is None:
            return
        library.load_from_file(current_txt_files[wantedIndex - 1])
        print(f"\nBooks loaded from file '{current_txt_files[wantedIndex - 1]}' successfully!")
