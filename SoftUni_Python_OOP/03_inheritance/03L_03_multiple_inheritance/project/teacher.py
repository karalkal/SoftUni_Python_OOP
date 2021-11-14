from project.employee import Employee
from project.person import Person

class Teacher(Employee, Person):
    def teach(self):
        return "teaching..."

# bay_ivan = Teacher()
# print(bay_ivan.teach())
# print(bay_ivan.get_fired())