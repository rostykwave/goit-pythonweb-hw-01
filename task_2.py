from abc import ABC, abstractmethod
from typing import List
from logger import logger


class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

    @abstractmethod
    def book_exists(self, title: str) -> bool:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]

    def get_all_books(self) -> List[Book]:
        return self.books

    def book_exists(self, title: str) -> bool:
        return any(book.title == title for book in self.books)


class BookDisplayInterface(ABC):
    @abstractmethod
    def display_books(self, books: List[Book]) -> None:
        pass


class ConsoleBookDisplay(BookDisplayInterface):
    def display_books(self, books: List[Book]) -> None:
        if not books:
            logger.info("No books in the library.")
            return

        for book in books:
            logger.info(
                f"Title: {book.title}, Author: {book.author}, Year: {book.year}"
            )


class LibraryManager:
    def __init__(
        self, library: LibraryInterface, display: BookDisplayInterface
    ) -> None:
        self.library = library
        self.display = display

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> bool:
        if self.library.book_exists(title):
            self.library.remove_book(title)
            return True
        return False

    def show_books(self) -> None:
        books = self.library.get_all_books()
        self.display.display_books(books)


def main() -> None:
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
                logger.info(f"Book '{title}' by {author} ({year}) added successfully.")
            case "remove":
                title = input("Enter book title to remove: ").strip()
                if manager.remove_book(title):
                    logger.info(f"Book '{title}' removed successfully.")
                else:
                    logger.info(f"Book '{title}' not found in the library.")
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
