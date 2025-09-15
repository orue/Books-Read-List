import datetime

import database

menu = """Please select one of the following options:
1) Add new book.
2) View upcoming books.
3) View all books
4) Read a book
5) View read books.
6) Exit.

Your selection: """
welcome = "Welcome to the ReadList app!"


print(welcome)
database.create_tables()


def prompt_add_book():
    title = input("Book Title: ")
    release_date = input("Release date (mm-dd-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%m-%d-%Y")
    timestamp = parsed_date.timestamp()

    database.add_book(title, timestamp)


def print_book_list(heading, books):
    print(f"-- {heading} Books --")
    for book in books:
        book_date = datetime.datetime.fromtimestamp(book[1])
        human_date = book_date.strftime("%b %d %Y")
        print(f"{book[0]} (release date: {human_date})")
    print("---- \n")


def print_read_book_list(username, books):
    print(f"-- {username}'s read book list --")
    for book in books:
        print(f"{book[1]}")
    print("---- \n")


def prompt_read_book():
    username = input("Username: ")
    book_title = input("Enter book title that you've read: ")
    database.read_book(username, book_title)


while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_book()
    elif user_input == "2":
        books = database.get_books(True)
        print_book_list("Upcoming", books)
    elif user_input == "3":
        books = database.get_books()
        print_book_list("All", books)
    elif user_input == "4":
        prompt_read_book()
    elif user_input == "5":
        username = input("Username: ")
        books = database.get_read_books(username)
        print_read_book_list(username, books)
    else:
        print("Invalid input, please try again!")
