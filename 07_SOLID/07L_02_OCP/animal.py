class Animal:
    _sound = ""
    _species = ""

    def get_speies(self):
        return self._species

    def get_sound(self):
        return self._sound


class Cat(Animal):
    _sound = 'meow'
    _species = 'cat'


class Dog(Animal):
    _sound = 'woof-woof'
    _species = 'dog'


class Chicken(Animal):
    _sound = 'chik-chirik'
    _species = 'chicken'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_sound())


animals = [Cat(), Dog()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)
