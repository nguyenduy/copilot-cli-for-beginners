from books import Book


def print_menu() -> None:
    print("\n📚 Book Collection App")
    print("1. Add a book")
    print("2. List books")
    print("3. Mark book as read")
    print("4. Remove a book")
    print("5. Exit")


def get_user_choice() -> str:
    while True:
        choice = input("Choose an option (1-5): ").strip()
        if not choice:
            print("Please enter a number between 1 and 5.")
            continue

        if not choice.isdigit():
            print("Please enter a valid number between 1 and 5.")
            continue

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Please enter a number between 1 and 5.")
            continue

        return choice


def _prompt_non_empty(prompt: str, field_name: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"{field_name} cannot be empty. Please try again.")


def _prompt_year(prompt: str) -> int:
    while True:
        year_input = input(prompt).strip()
        try:
            return int(year_input)
        except ValueError:
            print("Invalid year. Please enter a whole number.")


def get_book_details() -> tuple[str, str, int]:
    """Collect and validate the information needed to add a book.

    The function prompts the user for:
    - title: a non-empty string entered at the book title prompt
    - author: a non-empty string entered at the author prompt
    - year: a whole number entered at the publication year prompt

    Returns:
        tuple[str, str, int]: A 3-item tuple containing the title, author,
        and publication year in that order.
    """
    title = _prompt_non_empty("Enter book title: ", "Title")
    author = _prompt_non_empty("Enter author: ", "Author")
    year = _prompt_year("Enter publication year: ")
    return title, author, year


def print_books(books: list[Book]) -> None:
    if not books:
        print("No books found.")
        return

    print("\nYour Book Collection:\n")

    for index, book in enumerate(books, start=1):
        status = "✓" if book.read else " "
        print(f"{index}. [{status}] {book.title} by {book.author} ({book.year})")

    print()
