from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book):
        pass
    
    @abstractmethod
    def remove_book(self, title):
        pass
    
    @abstractmethod
    def get_all_books(self):
        pass
    
    @abstractmethod
    def book_exists(self, title):
        pass

class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def get_all_books(self):
        return self.books
    
    def book_exists(self, title):
        return any(book.title == title for book in self.books)

class BookDisplayInterface(ABC):
    @abstractmethod
    def display_books(self, books):
        pass

class ConsoleBookDisplay(BookDisplayInterface):
    def display_books(self, books):
        if not books:
            print("No books in the library.")
            return
            
        for book in books:
            print(f'Title: {book.title}, Author: {book.author}, Year: {book.year}')

class LibraryManager:
    def __init__(self, library, display):
        self.library = library
        self.display = display

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title):
        if self.library.book_exists(title):
            self.library.remove_book(title)
            return True
        return False

    def show_books(self):
        books = self.library.get_all_books()
        self.display.display_books(books)

def main():
    library = Library()
    display = ConsoleBookDisplay()
    manager = LibraryManager(library, display)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
                print(f"Book '{title}' by {author} ({year}) added successfully.")
            case "remove":
                title = input("Enter book title to remove: ").strip()
                if manager.remove_book(title):
                    print(f"Book '{title}' removed successfully.")
                else:
                    print(f"Book '{title}' not found in the library.")
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
