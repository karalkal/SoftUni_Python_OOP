class Circle:
    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return Circle.pi * self.radius * self.radius  # using class attribute
        # return f"{self.pi * self.radius * self.radius:.2f}"  # using instance attribute

    def get_circumference(self):
        return 2 * Circle.pi * self.radius
