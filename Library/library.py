from Library.user import User


class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user: User):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                user.books.append(book_name)
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {book_name: days_to_return}
                self.rented_books[user.username][book_name] = days_to_return
                self.books_available[author].remove(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"
            else:
                for book in self.rented_books.values():
                    if book_name in book:
                        days_to_return = book[book_name]
                        return f"The book {book_name} is already rented and will be available in {days_to_return} days!"

    def return_book(self, author, book_name, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)
        else:
            return f"{user.username} doesn't have this book his/her records!"
