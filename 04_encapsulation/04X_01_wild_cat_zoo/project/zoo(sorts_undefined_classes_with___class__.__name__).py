"""
It won't work with the current file name as it cannot be imported properly.
In this script we create a dict with keys which will be read from an object name.
In the problem I had to solve for SoftUni the keys were predefined, hence the other zoo.py file
"""

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price > self.__budget:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        # return f"{self.name} the {type(worker).__name__} hired successfully"  # SAME AS THE ABOVE

    def fire_worker(self, worker_name):
        for guy in self.workers:
            if guy.name == worker_name:
                self.workers.remove(guy)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        money_owed = 0
        for guy in self.workers:
            money_owed += guy.salary
        if money_owed > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        else:
            self.__budget -= money_owed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        money_needed = 0
        for beast in self.animals:
            money_needed += beast.money_for_care
        if money_needed > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        else:
            self.__budget -= money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_result = f"You have {len(self.animals)} animals\n"
        dict_animals = {}
        for beast in self.animals:
            if beast.__class__.__name__ not in dict_animals:
                dict_animals[beast.__class__.__name__] = []
            dict_animals[beast.__class__.__name__].append(beast)

        for key, value in dict_animals.items():
            animals_result += f"----- {len(value)} {key}s:\n"
            for this_animal in value:
                animals_result += f"Name: {this_animal.name}, Age: {this_animal.age}, Gender: {this_animal.gender}\n"

        return animals_result.strip()
        # return dict_animals

    def workers_status(self):
        workers_result = f"You have {len(self.workers)} workers\n"
        dict_workers = {}
        for guy in self.workers:
            if guy.__class__.__name__ not in dict_workers:
                dict_workers[guy.__class__.__name__] = []
            dict_workers[guy.__class__.__name__].append(guy)

        for key, value in dict_workers.items():
            workers_result += f"----- {len(value)} {key}s:\n"
            for this_guy in value:
                workers_result += f"Name: {this_guy.name}, Age: {this_guy.age}, Salary: {this_guy.salary}\n"

        return workers_result.strip()
        # return dict_animals
