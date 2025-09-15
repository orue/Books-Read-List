import datetime
import sqlite3

CREATE_BOOKS_TABLE = """CREATE TABLE IF NOT EXISTS books (
  title TEXT,
  release_timestamp REAL
);"""

CREATE_READ_TABLE = """CREATE TABLE IF NOT EXISTS reads (
    username = TEXT,
    title TEXT
    );"""

INSERT_BOOKS = "INSERT INTO books (title, release_timestamp, read) VALUES (?,?);"
DELETE_BOOK = "DELETE FROM books WHERE title = ?;"
SELECT_ALL_BOOKS = "SELECT * FROM books;"
SELECT_UPCOMING_BOOKS = "SELECT * FROM books WHERE release_timestamp > ?;"
SELECT_READ_BOOKS = "SELECT * FROM reads WHERE username = ?;"
INSERT_READS = "INSERT INTO reads (user_name, title) VALUES (?,?)"
SET_BOOK_READ = "UPDATE books SET read = 1 WHERE title = ?;"


connection = sqlite3.connect("books.db")


def create_tables():
    with connection:
        connection.execute(CREATE_BOOKS_TABLE)
        connection.execute(CREATE_READ_TABLE)


def add_book(title, release_timestamp):
    with connection:
        connection.execute(INSERT_BOOKS, (title, release_timestamp))


def get_books(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_BOOKS, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_BOOKS)
        return cursor.fetchall()


def read_book(username, title):
    with connection:
        connection.execute(DELETE_BOOK, (title,))
        connection.execute(
            INSERT_READS,
            (
                username,
                title,
            ),
        )


def get_read_books(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_READ_BOOKS, (username,))
        return cursor.fetchall()
