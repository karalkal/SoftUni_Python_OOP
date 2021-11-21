from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: Customer = []
        self.trainers: Trainer = []
        self.equipment: Equipment = []
        self.plans: ExercisePlan = []
        self.subscriptions: Subscription = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        for this_subscription in self.subscriptions:
            if this_subscription.id == subscription_id:
                break
        str_to_display = str(this_subscription) + "\n"

        customer_to_display_id = this_subscription.customer_id
        trainer_to_display_id = this_subscription.trainer_id

        for customer in self.customers:
            if customer_to_display_id == customer.id:
                str_to_display += str(customer) + "\n"
                break

        for trainer in self.trainers:
            if trainer_to_display_id == trainer.id:
                str_to_display += str(trainer) + "\n"
                break

        for this_plan in self.plans:
            if trainer_to_display_id == this_plan.trainer_id:
                plan_of_interest = this_plan
                to_add_plan_str_at_the_end = str(this_plan)
                break

        for this_eq in self.equipment:
            if plan_of_interest.equipment_id == this_eq.id:
                str_to_display += str(this_eq) + "\n"
                break

        return str_to_display + to_add_plan_str_at_the_end

# ivan = Customer("ivan", "hg", "kjkjk@kur.com")
# my_gym = Gym()
# ivan = my_gym.add_customer(ivan)


# Customer <1> John; Address: Maple Street; Email: john.smith@gmail.com
# Trainer <1> Peter
# Equipment <1> Treadmill
# Plan <1> with duration 20 minutes
