from project.dvd import DVD


class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []  # accepts DVD objects

    def __repr__(self):
        names_of_rented_films = set(film.name for film in self.rented_dvds)

        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's " \
               f"({', '.join(names_of_rented_films)})"
