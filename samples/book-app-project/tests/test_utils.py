import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import book_app
import utils


def test_get_user_choice_reprompts_for_empty_and_invalid_input(monkeypatch, capsys):
    responses = iter(["", "abc", "9", "2"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))

    choice = utils.get_user_choice()

    assert choice == "2"
    output = capsys.readouterr().out
    assert "Please enter a number between 1 and 5." in output
    assert "Please enter a valid number between 1 and 5." in output


def test_get_book_details_reprompts_for_empty_title(monkeypatch, capsys):
    responses = iter(["", "Dune", "Frank Herbert", "1965"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))

    title, author, year = utils.get_book_details()

    assert title == "Dune"
    assert author == "Frank Herbert"
    assert year == 1965
    assert "Title cannot be empty. Please try again." in capsys.readouterr().out


def test_handle_list_by_year(monkeypatch, capsys):
    class DummyBook:
        def __init__(self, title, author, year, read=False):
            self.title = title
            self.author = author
            self.year = year
            self.read = read

    class DummyCollection:
        def list_by_year(self):
            return [
                DummyBook("Old", "A", 1980),
                DummyBook("New", "B", 2000),
            ]

    monkeypatch.setattr(book_app, "collection", DummyCollection())

    book_app.handle_list_by_year()

    output = capsys.readouterr().out
    assert "Books by Year" in output
    assert "Old by A (1980)" in output
    assert "New by B (2000)" in output
