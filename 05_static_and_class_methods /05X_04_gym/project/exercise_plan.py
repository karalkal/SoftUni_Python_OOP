class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.assign_id_and_increment()

    @staticmethod
    def assign_id_and_increment():
        result = ExercisePlan.id
        ExercisePlan.id += 1
        return result

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours * 60)

    @staticmethod
    def get_next_id():
        return ExercisePlan.id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"


# my_plan = ExercisePlan(11, 4, 77)
# print(my_plan)
# print(my_plan.get_next_id())
