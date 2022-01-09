from typing import List

from project.rooms.room import Room


class Everland:
    def __init__(self) -> object:
        self.rooms: List[Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption}$.\n"

    def pay(self):
        result = ""
        for room in self.rooms:
            bill = room.expenses + room.room_cost
            if bill > room.budget:
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)
            else:
                room.budget -= bill
                result += f"{room.family_name} paid {bill:.2f}$ and have {room.budget:.2f}$ left.\n"
        return result.strip()

    def status(self):
        result = f"Total population: {sum(r.members_count for r in self.rooms)}\n"
        for room in self.rooms:
            result += str(room)

        return result

