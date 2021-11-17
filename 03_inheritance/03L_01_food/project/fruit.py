from project.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        self.name = name
        super(Fruit, self).__init__(expiration_date)

#     def __str__(self):
#         return f"The {self.name} has expiry date of {self.expiration_date}"
#
#
# fig = Fruit("Fig", 33)
# print(fig)
