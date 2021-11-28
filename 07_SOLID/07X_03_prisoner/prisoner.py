import copy


class Person:
    def __init__(self, position):
        self.position = position


class FreeMan(Person):
    def __init__(self, position):
        super().__init__(position)

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except AttributeError:
    print("The poor c**t cannot go anywhere")

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

print()
free_man = FreeMan([11, 11])
print("The FreeMan trying to walk to north by 10 and east by -3.")

free_man.walk_north(10)
free_man.walk_east(-3)

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the FreeMan: {free_man.position}")
