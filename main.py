from utils import *


#constants
title_year_author_dict = {'t':'title', 'y':'year', 'a': 'author'}

def main():
    
    library = Library()

    while True:
        print("\n1. Add Books")
        print("2. Find Books")
        print("3. Display all books")
        print("4. Remove Book")
        print("5. Update Book")
        print("6. Save Books to file")
        print("7. Retrieve Books from file")
        print("8. Exit")
        
        choice = input("Choose one option: ")

        match choice:
            
            case '1':
                title = input("Book title: ")
                author = input("Author: ")
                year = int(input("Publish year: "))
                library.add_book(Book(title, author, year))
            
            case '2':
                query = input("Enter Author name or Book title: ")
                by = input("Search book based on (title(t)/author(a)/year(y): ")
                results = library.search_books(query, title_year_author_dict[by])
                for book in results:
                    print(f"{book.title} by {book.author}, {book.year}")
            
            case '3':
                if not library.books:
                    print("\nThere is no any books in your library right now!")
                else:
                    sort_by = input("Sort based on (title(t)/author(a)/year(y): ")
                    library.display_books(title_year_author_dict[sort_by])
                
            case '4':
                title = input("Title of book to be removed: ")
                library.remove_book(title)
            
            case '5':
                old_title = input("Title of book to be updated: ")
                new_title = input("New title (optional): ")
                new_author = input("New author (optional): ")
                new_year = input("New publish year (optional): ")
                library.update_book(old_title, new_title, new_author, new_year)
            
            case '6':
                if not os.path.exists(library.bookFile.fileName) or library.bookFile.fileName != "":
                    inputName = input("File name to for storing books: ")
                    library.bookFile = File(inputName, os.path.curdir)
                library.save_to_file(library.bookFile.fileName)


            case '7':
                current_txt_files = findAllTextFiles()
                if not current_txt_files:
                    print("There is no any text file in currnet dir")
                else:
                    print("\nThis text files are available in your current directory:\n")
                    for index, file in enumerate(current_txt_files):
                        print(index+1,". ", file)
                    wantedIndex = int(input("\nChoose the number of file: "))
                    library.load_from_file(current_txt_files[wantedIndex-1])
            
            case '8':
                print("Come back soon...")
                heartPrinter()
                break
            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
