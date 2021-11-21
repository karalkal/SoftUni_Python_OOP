from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    # function to find customer we are looking for
    def find_customer(self, customer_id):
        for person in self.customers:
            if person.id == customer_id:
                return person

    def rent_dvd(self, customer_id, dvd_id):
        our_man = self.find_customer(customer_id)
        # what if no customer or dvd with these ids?

        for this_movie in self.dvds:
            if dvd_id == this_movie.id:
                # dvd is found, check if rented
                if this_movie.is_rented:
                    if this_movie in our_man.rented_dvds and our_man.id == customer_id:
                        return f"{our_man.name} has already rented {this_movie.name}"
                    else:
                        return "DVD is already rented"

                # age restriction
                elif this_movie.age_restriction > our_man.age:
                    return f"{our_man.name} should be at least {this_movie.age_restriction} to rent this movie"

                # if not rented and not restricted, rent dvd to customer
                else:
                    this_movie.is_rented = True
                    our_man.rented_dvds.append(this_movie)
                    return f"{our_man.name} has successfully rented {this_movie.name}"

    def return_dvd(self, customer_id, dvd_id):
        our_man = self.find_customer(customer_id)
        for this_movie in self.dvds:
            if dvd_id == this_movie.id:
                if this_movie not in our_man.rented_dvds:
                    return f"{our_man.name} does not have that DVD"
                else:
                    this_movie.is_rented = False
                    our_man.rented_dvds.remove(this_movie)
                    return f"{our_man.name} has successfully returned {this_movie.name}"


    def __repr__(self):
        data_to_print = ""
        for customer in self.customers:
            data_to_print += customer.__repr__() + "\n"
        for dvd in self.dvds:
            data_to_print += dvd.__repr__() + "\n"
        return data_to_print.strip()
