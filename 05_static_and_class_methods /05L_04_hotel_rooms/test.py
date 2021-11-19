from project.hotel import Hotel
from project.room import Room

# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# print(hotel.status())
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# print(hotel.status())
#
#
# hotel.free_room(1)
# print(hotel.status())
#

hotel1 = Hotel.from_stars(22)
room = Room(1, 3)
print(hotel1.status())

hotel1.add_room(room)
print("added room 1, cap. 3====>>>>")
print(hotel1.status())
print()

hotel1.take_room(1, 3)
print("taken room 1, 3 guests====>>>>")
print(hotel1.status())
print()

hotel1.free_room(1)
print("freed room 1, cap. 3 ====>>>>")
print(hotel1.status())
print()

print(hotel1.guests, 0)
print(hotel1.rooms[0].is_taken, "--------must be", False)
print(hotel1.rooms[0].guests, "--????--must be", 3)
print(hotel1.rooms[0].__dict__)
