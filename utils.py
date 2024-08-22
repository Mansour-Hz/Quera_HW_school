import json
import fnmatch
import os
from typing import Optional


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class File:
    def __init__(self, file_name="", file_path="") -> None:
        self.fileName = file_name
        self.filePath = file_path

class Library:
    def __init__(self):
        self.books = []
        self.bookFile = File()

    def add_book(self, book: Book):
        if not any(b.title == book.title and b.author == book.author for b in self.books):
            self.books.append(book)
            print(f"Book '{book.title}' added.")
        else:
            print("This book has been added before")

    def search_books(self, query: str, by='title'):
        results = [book for book in self.books if query.lower()
                   in getattr(book, by).lower()]
        return results

    def display_books(self, sort_by='title'):
        sorted_books = sorted(self.books, key=lambda x: getattr(x, sort_by))
        for book in sorted_books:
            print(f"{book.title} by {book.author}, {book.year}")

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]
        print(f"book '{title}' removed.")

    def update_book(self, old_title: str, new_title: Optional[str] = None,
                     new_author: Optional[str] =None, new_year: Optional[str] =None):
        for book in self.books:
            if book.title == old_title:
                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                if new_year:
                    book.year = new_year
                print(f"Book '{old_title}' Updated.")
                return
        print("Book was not found")

    def save_to_file(self, filename:str):
        newFileName = os.path.splitext(filename)[0] + '.txt'
        with open(newFileName, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file)
        print("Library saved.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.books = [Book(**data) for data in json.load(file)]
            print("Library restored.")
        except FileNotFoundError:
            print("File was not found.")


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
