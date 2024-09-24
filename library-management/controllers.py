class BookController():
    def __init__(self) -> None:
        self.db = []

    def add_book(self, book):
        self.db.append(book)

    def list_books(self):
        for book in self.db:
            book.show_info()

    def search_book(self, title):
        for book in self.db:
            if book.title == title:
                return book

    def delete_book(self, code):
        code_find = False
        for book in self.db:
            if book.code == code:
                code_find = True
                self.db.remove(book)
                return code_find
        return code_find
