from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.expenses + room.room_cost
        return f"Monthly consumtions: {result:.2f}$."  # typo in expected output

    def pay(self):
        str_to_return = ""
        for room in self.rooms:
            bill = room.expenses + room.room_cost
            budget = room.budget - bill
            if budget > 0:
                str_to_return += f"{room.family_name} paid {bill:.2f}$ and have {budget:.2f}$ left.\n"
                room.budget = budget
            else:
                str_to_return += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)

        return str_to_return.strip()

    def status(self):
        str_to_return = f"Total population: {sum(r.members_count for r in self.rooms)}\n"
        for room in self.rooms:
            room_name = room.family_name
            members = room.members_count
            current_budget = room.budget
            expenses = room.expenses
            str_to_return += f"{room_name} with {members} members. Budget: {current_budget:.2f}$, Expenses: {expenses:.2f}$\n"
            if room.children:
                n = 0
                for ch in room.children:
                    n += 1
                    str_to_return += f"--- Child {n} monthly cost: {ch.cost * 30:.2f}$\n"
            if room.appliances:
                cost_of_all_appliances_for_one_month = 0
                for app in room.appliances:
                    cost_of_all_appliances_for_one_month += app.get_monthly_expense()
                str_to_return += f"--- Appliances monthly cost: {cost_of_all_appliances_for_one_month:.2f}$\n"

        return str_to_return.strip()
