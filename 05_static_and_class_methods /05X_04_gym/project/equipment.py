class Equipment:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = Equipment.assign_id_and_increment()

    @staticmethod
    def assign_id_and_increment():
        result = Equipment.id
        Equipment.id += 1
        return result

    @staticmethod
    def get_next_id():
        return Equipment.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
