from models import Book, User


class BookController():
    def __init__(self) -> None:
        self.db = []

    def add_book(self, book):
        self.db.append(book)

    def list_books(self):
        for book in self.db:
            print(book.show_info())
            print('-' * 50)
