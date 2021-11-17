from project.album import Album


class Band:
    def __init__(self, band_name):
        self.name = band_name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.album_name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.album_name}."

    def remove_album(self, remove_album_with_this_name: str):
        for album_obj in self.albums:
            if album_obj.album_name == remove_album_with_this_name:
                if album_obj.published:
                    return "Album has been published. It cannot be removed."
                # if it is not published:
                self.albums.remove(album_obj)
                return f"Album {remove_album_with_this_name} has been removed."
        # if it is not found at all
        return f"Album {remove_album_with_this_name} is not found."

    def details(self):
        band_info = f"Band {self.name}"
        for album in self.albums:
            band_info += f"\n{album.details()}"
        return band_info
