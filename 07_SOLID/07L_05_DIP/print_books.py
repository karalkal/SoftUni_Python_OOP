class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class RegularFormatter(Formatter):
    pass


class UpperCaseFormatter(Formatter):
    def format(self, book: Book) -> str:
        return super().format(book).upper()


class LowerCaseFormatter(Formatter):
    def format(self, book):
        return super().format(book).lower()


class ReversingFormatter(Formatter):
    def format(self, book):
        return super().format(book)[::-1]


class Printer:
    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        formatted_book = self.formatter.format(book)
        return formatted_book


new_book = Book("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt...")

upperc_f = UpperCaseFormatter()
lowerc_f = LowerCaseFormatter()
reg_f = RegularFormatter()
rev_f = ReversingFormatter()

printer1 = Printer(upperc_f)
printer2 = Printer(lowerc_f)
printer3 = Printer(reg_f)
printer4 = Printer(rev_f)

print(printer1.get_book(new_book))
print()
print(printer2.get_book(new_book))
print()
print(printer3.get_book(new_book))
print()
print(printer4.get_book(new_book))
print()
