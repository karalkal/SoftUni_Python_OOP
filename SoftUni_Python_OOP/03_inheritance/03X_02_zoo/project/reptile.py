from project.animal import Animal


class Reptile(Animal):
    def __init__(self, name):
        super(Reptile, self).__init__(name)