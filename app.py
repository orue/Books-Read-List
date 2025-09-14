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


while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_book()
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    else:
        print("Invalid input, please try again!")
