from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages

        matrix = []
        for r in range(pages):
            row = []
            for c in range(4):
                row.append("")
            matrix.append(row)
        self.photos = matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):
        for r in range(len(self.photos)):
            for c in range(4):
                if self.photos[r][c] == "":
                    self.photos[r][c] = label
                    return f"{label} photo added successfully on page {1 + r} slot {1 + c}"  # starting from 1

        return "No more free slots"

    def display(self):
        separator = "-----------"
        album_view = separator + "\n"
        for r in range(len(self.photos)):
            album_view += f"{' '.join(self.photos[r])}\n{separator}\n"
        return album_view.strip()


album = PhotoAlbum(2)
# whatever = PhotoAlbum.from_photos_count(9)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
# print(whatever.display())
