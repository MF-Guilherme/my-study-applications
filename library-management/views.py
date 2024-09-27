from controllers import BookController, UserController
from prompt_toolkit import prompt

book_controller = BookController()
user_controller = UserController()

# BOOK VIEWS

def show_menu():
    ipt = input(f'- Type "book" to manage books.\n'
                f'- Type "user" to manage users.\n'
                f'- Type 0 "zero" to exit system.\n'
                f'{'-' * 50}\n')
    if ipt.lower() in ['book', 'books']:
        print(f'- To add a new book enter 1.\n'
              f'- To list all books enter 2.\n'
              f'- To search for a book enter 3.\n'
              f'- To update a book enter 4.\n'
              f'- To delete a book enter 5.')
        print('-' * 50)
    elif ipt.lower() in ['user', 'users']:
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
        new_title = prompt("Book Title: ", default=book.title).strip() or book.title
        new_author = prompt("Author: ", default=book.author).strip() or book.author
        new_year = prompt("Publication Year: ", default=book.year).strip() or book.year
        new_genre = prompt("Literary genre: ", default=book.genre).strip() or book.genre
        controller.update_book(ipt_code, new_title, new_author, new_year, new_genre)
        print('Book updated')
    else:
        print("Book not found")

# USER VIEWS
    
def get_user_infos():
    name = input("Name: ")
    email = input("E-mail: ")
    phone = input("Phone number: ")
    user_code = input("User code: ")
    return name, email, phone, user_code

def user_register(controller):
    name, email, phone, user_code = get_user_infos()
    controller.register_user(name, email, phone, user_code)
    print('User registered!')

def show_users(controller):
    users = controller.list_users()
    if users:
        for user in users:
            print(f'Name: {user.name} | Email: {user.email} | User code: {user.user_code}')
    else: 
        print('There are no users registered yet')

def search_user(controller):
    ipt_code = input('Enter the user code: ')
    user = controller.find_by_user_code(ipt_code)
    if user:
        print(f' User code: {user.user_code} | Name: {user.name} | Email: {user.email} | Phone number: {user.phone}')
    else:
        print('User not found')
    
def delete_user(controller):
    ipt_code = input('Enter the user code you want to delete: ')
    if not controller.delete_user(ipt_code):
        print("User not found.")
    else: print("User deleted.")

def update_user(controller):
    ipt_code = input('Enter the user code you want to update: ')
    user = controller.find_by_user_code(ipt_code)
    if user:
        new_name = prompt("Name: ", default=user.name).strip() or user.name
        new_email = prompt("E-mail: ", default=user.email).strip() or user.email
        new_phone = prompt("Phone number: ", default=user.phone).strip() or user.phone
        controller.update_user(ipt_code, new_name, new_email, new_phone)
        print('User updated')
    else:
        print("User not found")
