import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import books_buggy as books
from books_buggy import BookCollection


@pytest.fixture(autouse=True)
def use_temp_data_file(tmp_path, monkeypatch):
    """Use a temporary data file for each test."""
    temp_file = tmp_path / "data.json"
    temp_file.write_text("[]")
    monkeypatch.setattr(books, "DATA_FILE", str(temp_file))


class TestAddBook:
    """Tests for BookCollection.add_book."""

    def test_happy_path_adds_book(self):
        collection = BookCollection()

        result = collection.add_book("1984", "George Orwell", 1949)

        assert result.title == "1984"
        assert result.author == "George Orwell"
        assert result.year == 1949
        assert result.read is False
        assert collection.find_book_by_title("1984") == result

    @pytest.mark.parametrize(
        "title,author,year",
        [
            ("", "George Orwell", 1949),
            ("   ", "George Orwell", 1949),
            ("1984", "", 1949),
            ("1984", "   ", 1949),
        ],
    )
    def test_rejects_empty_title_or_author(self, title, author, year):
        collection = BookCollection()

        with pytest.raises(ValueError):
            collection.add_book(title, author, year)

    @pytest.mark.parametrize("year", [0, -1, 3000])
    def test_rejects_invalid_years(self, year):
        collection = BookCollection()

        with pytest.raises(ValueError):
            collection.add_book("1984", "George Orwell", year)

