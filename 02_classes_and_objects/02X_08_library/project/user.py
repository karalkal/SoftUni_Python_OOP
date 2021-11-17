import project.library


class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        for this_author in library.books_available.keys():
            for this_book in library.books_available.values():
                if this_author == author and this_book == book_name:
                    # move_book = library.books_available[author][book_name]
                    del library.books_available[author][book_name]
                    record_in_library_rented = {book_name: days_to_return}
                    project.library.Library.__init__().rented_books[self.username] = record_in_library_rented
                    # will fail if user already has rented a book
