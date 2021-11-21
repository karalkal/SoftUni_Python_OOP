class Customer:
    id = 1

    def __init__(self, name, address, email):
        self.email = email
        self.name = name
        self.address = address
        self.id = Customer.assign_id_and_increment()

    @staticmethod
    def assign_id_and_increment():
        result = Customer.id
        Customer.id += 1
        return result

    @staticmethod
    def get_next_id():
        return Customer.id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


# c1 = Customer("c1", "hg", "kjkjk")
# c2 = Customer("c2", "hg", "kjkjk")
# c3 = Customer("c3", "hg", "kjkjk")
# c4 = Customer("c4", "hg", "kjkjk")
# print(c1.id)
# print(c2.id)
# print(c3.id)
# print(c4.id)
