'''
I could be wrong but I didn't see much point of this exercise and have created some really basic functionality instead
'''


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return f"{book.title}, written by {book.author}"


bible = Book("Bible", "God")
the_body = Book("The Body", "Bryson")
svejk = Book("Svejk", "Hasek")
my_lib = Library([bible, the_body, svejk])
print(my_lib.find_book("Bible"))
