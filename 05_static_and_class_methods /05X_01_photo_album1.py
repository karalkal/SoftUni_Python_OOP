from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages

        matrix = []
        for i in range(pages):
            matrix.append([])
        self.photos = matrix

        self.row = 0
        self.column = 0
        self.counter = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):
        if self.counter >= self.pages * 4:
            return "No more free slots"

        else:
            self.counter += 1

            if self.column == 4:
                self.row += 1
                self.column = 1
            else:
                self.column += 1

            self.photos[self.row].append(label)
            return f"{label} photo added successfully on page {1 + self.row} slot {self.column}"  # starting from 1

    def display(self):
        separator = "-----------"
        result = ""
        for page in range(len(self.photos)):
            result += separator
            page_content = ["[]" for x in self.photos[page]]
            result += "\n" + " ".join(page_content) + "\n"
        result += separator

        return result
