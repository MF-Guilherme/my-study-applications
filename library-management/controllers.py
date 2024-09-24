class BookController():
    def __init__(self) -> None:
        self.db = []

    def add_book(self, book):
        self.db.append(book)

    def list_books(self):
        if self.db:
            return self.db
        else:
            return None
        
    def search_book(self, title):
        for book in self.db:
            if book.title == title:
                return book
        return None

    def delete_book(self, code):
        for book in self.db:
            if book.code == code:
                self.db.remove(book)
                return True
        return False
