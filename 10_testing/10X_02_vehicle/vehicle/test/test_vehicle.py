from project.vehicle import Vehicle
import unittest


class TestVehicle(unittest.TestCase):
    def test_constant__must_be_1_25(self):
        my_car = Vehicle(2.2, 190)
        self.assertEqual(1.25, my_car.DEFAULT_FUEL_CONSUMPTION)

        alfa = Vehicle(1, 1)
        alfa.DEFAULT_FUEL_CONSUMPTION = 8888
        self.assertEqual(1.25, alfa.fuel_consumption)
        self.assertEqual(8888, alfa.DEFAULT_FUEL_CONSUMPTION)

    def test_all_values_in_constructor_are_floats(self):
        my_car = Vehicle(2.2, 190.1)
        self.assertIsInstance(my_car.DEFAULT_FUEL_CONSUMPTION, float)
        self.assertIsInstance(my_car.fuel_consumption, float)
        self.assertIsInstance(my_car.fuel, float)
        self.assertIsInstance(my_car.capacity, float)
        self.assertIsInstance(my_car.horse_power, float)

    def test_constructor__with_float_values(self):
        my_car = Vehicle(2.2, 1.90)
        self.assertEqual(2.2, my_car.fuel)
        self.assertEqual(2.2, my_car.capacity)
        self.assertEqual(1.90, my_car.horse_power)
        self.assertEqual(1.25, my_car.fuel_consumption)

    def test_drive_meth__when_enough_fuel__expect_fuel_to_decrease(self):
        my_car = Vehicle(81.25, 190)
        self.assertEqual(81.25, my_car.fuel)
        my_car.drive(65)
        self.assertEqual(0, my_car.fuel)

    def test_drive_meth__when_not_enough_fuel__expect_exception(self):
        my_car = Vehicle(80, 190)
        self.assertEqual(80, my_car.fuel)
        with self.assertRaises(Exception) as scenario:
            my_car.drive(66)
        self.assertEqual("Not enough fuel", str(scenario.exception))

    def test_refuel_when_enough_capacity__expect_fuel_to_increase(self):
        my_car = Vehicle(70, 190)
        my_car.capacity = 80
        my_car.refuel(10)
        self.assertEqual(80, my_car.fuel)

    def test_refuel_when_not_enough_capacity__expect_exception(self):
        my_car = Vehicle(70, 190)
        my_car.capacity = 80
        with self.assertRaises(Exception) as scenario:
            my_car.refuel(12)
        self.assertEqual("Too much fuel", str(scenario.exception))

    def test_str_method(self):
        my_car = Vehicle(70, 190)
        expected = "The vehicle has 190 horse power with 70 fuel left and 1.25 fuel consumption"
        actual = str(my_car)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
