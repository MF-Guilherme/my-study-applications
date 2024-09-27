from controllers import BookController, UserController
from prompt_toolkit import prompt

book_controller = BookController()

def show_menu():
    ipt = input(f'- Type "book" to manage books.\n'
                f'- Type "user" to manage users.\n'
                f'{'-' * 50}\n')
    if ipt == 'book' or ipt == 'books' or ipt == 'Book' or ipt == 'Books':
        print(f'- To add a new book enter 1.\n'
              f'- To list all books enter 2.\n'
              f'- To search for a book enter 3.\n'
              f'- To update a book enter 4.\n'
              f'- To delete a book enter 5.')
        print('-' * 50)
    elif ipt == 'user' or ipt == 'users' or ipt == 'User' or ipt == 'Users':
        print(f'- To add a new user enter 1.\n'
              f'- To list all users enter 2.\n'
              f'- To search for a user enter 3.\n'
              f'- To update a user enter 4.\n'
              f'- To delete a user enter 5')
        print('-' * 50)
    else:
        print('Invalid input! Please, enter "book" or "user".')
        print('-' * 50)
    return ipt

def get_book_infos():
    title = input("Book title: ")
    author = input("Author: ")
    year = input("Publication year: ")
    genre = input("Literary genre: ")
    code = input("ISBN code: ")
    return title, author, year, genre, code

def book_register(controller):
    title, author, year, genre, code = get_book_infos()
    controller.add_book(title, author, year, genre, code)
    print('Book registered!')

def show_books(controller):
    books = controller.list_books()
    if books:
        for book in books:
            print(f'Title: {book.title} | Author: {book.author} | ISBN: {book.code}')
    else: 
        print('There are no books registered yet')

def search_book(controller):
    ipt_code = input('Enter the book ISBN code: ')
    book = controller.search_by_book_code(ipt_code)
    if book:
        print(f'Title: {book.title} | Author: {book.author} | ISBN: {book.code}')
    else:
        print('Book not found')
    
def delete_book(controller):
    ipt_code = input('Enter the ISBN code of the book you want to delete: ')
    if not controller.delete_book(ipt_code):
        print("ISBN code doesn't exists.")
    else: print("Book deleted.")

def update_book(controller):
    ipt_code = input('Enter the book ISBN code you want to update: ')
    book = controller.search_by_book_code(ipt_code)
    if book:
        new_title = prompt("Book Title: ", default=book.title)
        new_author = prompt("Author: ", default=book.author)
        new_year = prompt("Publication Year: ", default=book.year)
        new_genre = prompt("Literary genre: ", default=book.genre)
        controller.update_book(ipt_code, new_title, new_author, new_year, new_genre)
        print('Book updated')
    else:
        print("Book not find")


if __name__ == "__main__":
    book_register(book_controller)
    print('-' * 50)
    show_books(book_controller)
    print('-' * 50)
    update_book(book_controller)
    show_books(book_controller)
