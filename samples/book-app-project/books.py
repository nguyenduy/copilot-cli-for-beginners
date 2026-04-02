import json
from datetime import date
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional

SEED_DATA_FILE = Path(__file__).with_name("data.json")
DATA_FILE = Path(__file__).with_name("data.runtime.json")


@dataclass
class Book:
    title: str
    author: str
    year: int
    read: bool = False


class BookCollection:
    def __init__(self):
        self.books: List[Book] = []
        self.load_books()

    def load_books(self):
        """Load books from the JSON file if it exists."""
        source_file = Path(DATA_FILE)
        if not source_file.exists():
            source_file = Path(SEED_DATA_FILE)

        try:
            with open(source_file, "r") as f:
                data = json.load(f)
                self.books = [Book(**b) for b in data]
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            print("Warning: data.json is corrupted. Starting with empty collection.")
            self.books = []

    def save_books(self):
        """Save the current book collection to JSON."""
        with open(Path(DATA_FILE), "w") as f:
            json.dump([asdict(b) for b in self.books], f, indent=2)

    def add_book(self, title: str, author: str, year: int) -> Book:
        title = title.strip()
        if not title:
            raise ValueError("Title cannot be empty.")

        author = author.strip()
        if not author:
            raise ValueError("Author cannot be empty.")

        current_year = date.today().year
        if year < 1 or year > current_year + 1:
            raise ValueError(f"Year must be between 1 and {current_year + 1}.")

        book = Book(title=title, author=author, year=year)
        self.books.append(book)
        self.save_books()
        return book

    def list_books(self) -> List[Book]:
        return self.books

    def list_by_year(self) -> List[Book]:
        """Return books sorted by publication year, oldest first."""
        return sorted(self.books, key=lambda book: (book.year, book.title.lower()))

    def find_book_by_title(self, title: str) -> Optional[Book]:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def mark_as_read(self, title: str) -> bool:
        book = self.find_book_by_title(title)
        if book:
            book.read = True
            self.save_books()
            return True
        return False

    def remove_book(self, title: str) -> bool:
        """Remove a book by title."""
        book = self.find_book_by_title(title)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def find_by_author(self, author: str) -> List[Book]:
        """Find all books by a given author."""
        return [b for b in self.books if b.author.lower() == author.lower()]

    def search_books(self, term: str) -> List[Book]:
        """Find books whose title or author contains the given term."""
        normalized_term = term.lower()
        if not normalized_term.strip():
            return []

        return [
            book
            for book in self.books
            if normalized_term in book.title.lower() or normalized_term in book.author.lower()
        ]
