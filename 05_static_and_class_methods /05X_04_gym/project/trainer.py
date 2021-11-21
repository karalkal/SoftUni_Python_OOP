class Trainer:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = Trainer.assign_id_and_increment()

    @staticmethod
    def assign_id_and_increment():
        result = Trainer.id
        Trainer.id += 1
        return result

    @staticmethod
    def get_next_id():
        return Trainer.id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
