from project.album import Album
from project.band import Band
from project.song import Song

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)

print(album.add_song(second_song))
print(album.details())

print(album.publish())
print(album.publish())

band = Band("Manuel")
print(band.add_album(album))
print(band.add_album(album))

print(band.remove_album("Initial D"))
print(band.details())

print()
print()

song88 = Song("A", 3.15, False)
print(song88.get_info())
album88 = Album("The Sound of Perseverance")
print(album88.details())
song101 = Song("Scavenger of Human Sorrow", 6.56, False)
song202 = Song("Scavenger of Human Sorrow", 6.56, False)

print(album88.add_song(song101))
print(album88.add_song(song101))
print(album88.add_song(song202))
# REMEMBER: if different object with same name, parent object will append it (if lsi as in this case)

song22 = Song("Scavenger of Human Sorrow", 6.56, True)
print(album88.add_song(song22))
# expected = "Cannot add Scavenger of Human Sorrow. It's a single"

print(album88.publish())
print(album88.add_song(song88))
# expected = "Cannot add songs. Album is published."

print(album88.remove_song("Scavenger of Human Sorrow"))
# expected = "Removed song Scavenger of Human Sorrow from album The Sound of Perseverance."
print()

print(album88.remove_song("Scavenger of Human Sorrow"))
# expected = "Song is not in the album."
print()

print(album.add_song(song))
print(album.publish())
print(album.remove_song("Scavenger of Human Sorrow"))
# expected = "Cannot remove songs. Album is published."

print()
band = Band("Death")
album = Album("The Sound of Perseverance")
print(band.add_album(album))
# expected = "Band Death has added their newest album The Sound of Perseverance."
print()

band = Band("Death")
album = Album("The Sound of Perseverance")
band.add_album(album)
print(band.remove_album("The Sound of Perseverance"))
# expected = "Album The Sound of Perseverance has been removed."
print()

print(band.remove_album("The Sound of Perseverance"))
# expected = "Album The Sound of Perseverance is not found."
print()

band = Band("Death")
album = Album("The Sound of Perseverance")
album.publish()
band.add_album(album)
print(band.remove_album("The Sound of Perseverance"))
# expected = "Album has been published. It cannot be removed."
print()
