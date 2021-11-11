from project.song import Song


class Album:
    def __init__(self, album_name, *songs_in_album: Song):
        self.album_name = album_name
        self.songs_in_album = []
        if songs_in_album:
            for song in songs_in_album:
                self.songs_in_album.append(song)
        self.published = False

    def add_song(self, song_to_add: Song):
        if song_to_add.is_single:
            return f"Cannot add {song_to_add.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        # if song_to_add in self.songs_in_album:  # probably not good idea to check for whole object
        #     return "Song is already in the album."
        for song_object in self.songs_in_album:
            if song_to_add.name == song_object.name:
                return "Song is already in the album."

        self.songs_in_album.append(song_to_add)
        return f"Song {song_to_add.name} has been added to the album {self.album_name}."

    def details(self):
        album_info = f"Album {self.album_name}"
        for tune in self.songs_in_album:
            album_info += f"\n== {tune.get_info()}"
        return album_info

    def remove_song(self, song_to_remove):
        if self.published:
            return "Cannot remove songs. Album is published."

        for song in self.songs_in_album:
            if song.name == song_to_remove:
                self.songs_in_album.remove(song)
                return f"Removed song {song_to_remove} from album {self.album_name}."
        # if not found
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.album_name} is already published."
        self.published = True
        return f"Album {self.album_name} has been published."
