from car_manager import Car

import unittest


class test_car_manager(unittest.TestCase):
    def test_init__with_valid_values(self):
        best_car = Car("Alfa", "GT", 6, 80)
        self.assertEqual("Alfa", best_car.make)
        self.assertEqual("GT", best_car.model)
        self.assertEqual(6, best_car.fuel_consumption)
        self.assertEqual(80, best_car.fuel_capacity)
        self.assertEqual(0, best_car.fuel_amount)

    def test_change_make_setter__with_valid_values__expect_changed_make(self):
        best_car = Car("Alfa", "GT", 6, 80)
        self.assertEqual("Alfa", best_car.make)
        best_car.make = "Porsche"
        self.assertEqual("Porsche", best_car.make)

    def test_change_model_setter__with_valid_values__expect_changed_model(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        self.assertEqual("Giulia", best_car.model)
        best_car.model = "GT"
        self.assertEqual("GT", best_car.model)

    def test_fuel_cons_setter__with_valid_values__expect_changed_fuel_cons(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        self.assertEqual(6, best_car.fuel_consumption)
        best_car.fuel_consumption = 8888
        self.assertEqual(8888, best_car.fuel_consumption)

    def test_fuel_capacity_setter__with_valid_values__expect_changed_fuel_capacity(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        self.assertEqual(80, best_car.fuel_capacity)
        best_car.fuel_capacity = 8888
        self.assertEqual(8888, best_car.fuel_capacity)

    def test_fuel_amount_setter__with_valid_values__expect_changed_fuel_amount(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        self.assertEqual(0, best_car.fuel_amount)
        best_car.fuel_amount = 8888
        self.assertEqual(8888, best_car.fuel_amount)

    def test_change_make_setter__with_empty_string__expect_exception(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        with self.assertRaises(Exception) as scenario:
            best_car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(scenario.exception))

    def test_change_model_setter__with_empty_string__expect_exception(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        with self.assertRaises(Exception) as scenario:
            best_car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(scenario.exception))

    def test_fuel_cons_setter__with_zero_or_negative__expect_exception(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        with self.assertRaises(Exception) as scenario:
            best_car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(scenario.exception))
        with self.assertRaises(Exception) as scenario:
            best_car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(scenario.exception))

    def test_fuel_capacity_setter__with_zero_or_negative__expect_exception(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        with self.assertRaises(Exception) as scenario:
            best_car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(scenario.exception))
        with self.assertRaises(Exception) as scenario:
            best_car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(scenario.exception))

    def test_fuel_amount_setter__with_zero__expect_exception(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        with self.assertRaises(Exception) as scenario:
            best_car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(scenario.exception))

    def test_refuel_meth__when_capacity_not_exceeded__expect_new_value(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        best_car.fuel_amount = 70
        best_car.refuel(10)
        self.assertEqual(80, best_car.fuel_amount)

    def test_refuel_meth__when_capacity_is_exceeded__expect_new_value(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        best_car.fuel_amount = 70
        best_car.refuel(11)
        self.assertEqual(80, best_car.fuel_amount)

    def test_refuel_meth__with_zero_or_negative__expect_exception(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        with self.assertRaises(Exception) as scenario:
            best_car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(scenario.exception))
        with self.assertRaises(Exception) as scenario:
            best_car.refuel(-2)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(scenario.exception))

    def test_drive__when_enough_fuel__expect_fuel_decrease(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        best_car.fuel_amount = 6
        best_car.drive(100)
        self.assertEqual(0, best_car.fuel_amount)

    def test_drive__when_not_enough_fuel__expect_exception(self):
        best_car = Car("Alfa", "Giulia", 6, 80)
        best_car.fuel_amount = 6
        with self.assertRaises(Exception) as scenario:
            best_car.drive(101)
        self.assertEqual("You don't have enough fuel to drive!", str(scenario.exception))


if __name__ == "__main__":
    unittest.main()
