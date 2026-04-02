import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from books import BookCollection
from utils import print_books


collection = BookCollection()


def handle_list() -> None:
    books = collection.list_books()
    print_books(books)


def handle_list_by_year() -> None:
    print("\nBooks by Year\n")

    books = collection.list_by_year()
    print_books(books)


def handle_add() -> None:
    print("\nAdd a New Book\n")

    title = input("Title: ").strip()
    author = input("Author: ").strip()
    year_str = input("Year: ").strip()

    try:
        year = int(year_str) if year_str else 0
        collection.add_book(title, author, year)
        print("\nBook added successfully.\n")
    except ValueError as e:
        print(f"\nError: {e}\n")


def handle_remove() -> None:
    print("\nRemove a Book\n")

    title = input("Enter the title of the book to remove: ").strip()
    collection.remove_book(title)

    print("\nBook removed if it existed.\n")


def handle_find() -> None:
    print("\nFind Books by Author\n")

    author = input("Author name: ").strip()
    books = collection.find_by_author(author)

    print_books(books)


def handle_search() -> None:
    print("\nSearch Books\n")

    term = input("Search term: ").strip()
    books = collection.search_books(term)

    print_books(books)


def handle_mark_read() -> None:
    print("\nMark a Book as Read\n")

    title = input("Enter the title of the book to mark as read: ").strip()
    if collection.mark_as_read(title):
        print("\nBook marked as read.\n")
    else:
        print("\nBook not found.\n")


def show_help() -> None:
    print("""
Book Collection Helper

Commands:
  list     - Show all books
  by-year  - Show books sorted by publication year
  add      - Add a new book
  read     - Mark a book as read
  search   - Search books by title or author
  remove   - Remove a book by title
  find     - Find books by author
  help     - Show this help message
""")


COMMANDS = {
    "list": handle_list,
    "by-year": handle_list_by_year,
    "add": handle_add,
    "read": handle_mark_read,
    "mark-read": handle_mark_read,
    "search": handle_search,
    "remove": handle_remove,
    "find": handle_find,
    "help": show_help,
}


def get_command_handler(command: str):
    return COMMANDS.get(command)


def main() -> None:
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    handler = get_command_handler(command)
    if handler is None:
        print("Unknown command.\n")
        show_help()
        return

    handler()


if __name__ == "__main__":
    main()
