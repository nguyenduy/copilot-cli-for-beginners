import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import pytest
import books
from books import BookCollection
from books import Book
from utils import print_books


@pytest.fixture(autouse=True)
def use_temp_data_file(tmp_path, monkeypatch):
    """Use a temporary data file for each test."""
    temp_file = tmp_path / "data.json"
    temp_file.write_text("[]")
    monkeypatch.setattr(books, "DATA_FILE", str(temp_file))
    monkeypatch.setattr(books, "SEED_DATA_FILE", str(temp_file))


def test_add_book():
    collection = BookCollection()
    initial_count = len(collection.books)
    collection.add_book("1984", "George Orwell", 1949)
    assert len(collection.books) == initial_count + 1
    book = collection.find_book_by_title("1984")
    assert book is not None
    assert book.author == "George Orwell"
    assert book.year == 1949
    assert book.read is False


def test_add_book_writes_to_runtime_file(tmp_path, monkeypatch):
    seed_file = tmp_path / "seed.json"
    seed_file.write_text(
        """
[
  {
    "title": "Seed",
    "author": "Author",
    "year": 2000,
    "read": false
  }
]
""".strip()
    )
    runtime_file = tmp_path / "runtime.json"
    monkeypatch.setattr(books, "SEED_DATA_FILE", str(seed_file))
    monkeypatch.setattr(books, "DATA_FILE", str(runtime_file))

    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)

    assert json.loads(seed_file.read_text()) == [
        {"title": "Seed", "author": "Author", "year": 2000, "read": False}
    ]
    assert [book.title for book in collection.list_books()] == ["Seed", "1984"]


def test_add_book_rejects_empty_title():
    collection = BookCollection()

    with pytest.raises(ValueError, match="Title cannot be empty."):
        collection.add_book("   ", "George Orwell", 1949)


def test_add_book_rejects_empty_author():
    collection = BookCollection()

    with pytest.raises(ValueError, match="Author cannot be empty."):
        collection.add_book("1984", "   ", 1949)


@pytest.mark.parametrize("year", [0, -1, 3000])
def test_add_book_rejects_invalid_years(year):
    collection = BookCollection()

    with pytest.raises(ValueError, match="Year must be between 1 and"):
        collection.add_book("1984", "George Orwell", year)


def test_mark_book_as_read():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    result = collection.mark_as_read("Dune")
    assert result is True
    book = collection.find_book_by_title("Dune")
    assert book.read is True

def test_mark_book_as_read_invalid():
    collection = BookCollection()
    result = collection.mark_as_read("Nonexistent Book")
    assert result is False

def test_remove_book():
    collection = BookCollection()
    collection.add_book("The Hobbit", "J.R.R. Tolkien", 1937)
    result = collection.remove_book("The Hobbit")
    assert result is True
    book = collection.find_book_by_title("The Hobbit")
    assert book is None

def test_remove_book_invalid():
    collection = BookCollection()
    result = collection.remove_book("Nonexistent Book")
    assert result is False


def test_search_books_by_title():
    collection = BookCollection()
    collection.add_book("The Pragmatic Programmer", "Andrew Hunt", 1999)
    results = collection.search_books("pragmatic")
    assert len(results) == 1
    assert results[0].title == "The Pragmatic Programmer"


def test_search_books_by_author():
    collection = BookCollection()
    collection.add_book("Clean Code", "Robert C. Martin", 2008)
    results = collection.search_books("martin")
    assert len(results) == 1
    assert results[0].author == "Robert C. Martin"


def test_search_books_no_match():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    results = collection.search_books("nonexistent")
    assert results == []


def test_search_books_empty_term_returns_no_results():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)

    results = collection.search_books("")

    assert results == []


def test_list_books_by_year():
    collection = BookCollection()
    collection.add_book("Book C", "Author C", 2005)
    collection.add_book("Book A", "Author A", 1990)
    collection.add_book("Book B", "Author B", 1990)

    results = collection.list_by_year()

    assert [book.title for book in results] == ["Book A", "Book B", "Book C"]


def test_print_books_shows_empty_message(capsys):
    print_books([])

    captured = capsys.readouterr()
    assert captured.out.strip() == "No books found."


def test_print_books_formats_book_list(capsys):
    print_books(
        [
            Book(title="1984", author="George Orwell", year=1949, read=True),
            Book(title="Dune", author="Frank Herbert", year=1965, read=False),
        ]
    )

    captured = capsys.readouterr()
    assert captured.out == (
        "\nYour Book Collection:\n\n"
        "1. [✓] 1984 by George Orwell (1949)\n"
        "2. [ ] Dune by Frank Herbert (1965)\n"
        "\n"
    )


def test_handle_list_uses_shared_printer(monkeypatch):
    import book_app

    calls = []

    monkeypatch.setattr(book_app.collection, "list_books", lambda: ["book-list"])
    monkeypatch.setattr(book_app, "print_books", lambda books: calls.append(books))

    book_app.handle_list()

    assert calls == [["book-list"]]


def test_handle_search_uses_shared_printer(monkeypatch):
    import book_app

    calls = []

    monkeypatch.setattr(book_app.collection, "search_books", lambda term: ["search-results"])
    monkeypatch.setattr("builtins.input", lambda prompt="": "dune")
    monkeypatch.setattr(book_app, "print_books", lambda books: calls.append(books))

    book_app.handle_search()

    assert calls == [["search-results"]]


def test_get_command_handler_returns_known_handler():
    import book_app

    assert book_app.get_command_handler("list") is book_app.handle_list


def test_get_command_handler_returns_none_for_unknown_command():
    import book_app

    assert book_app.get_command_handler("unknown") is None
