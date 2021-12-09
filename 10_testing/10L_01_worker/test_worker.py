from worker import Worker

import unittest

'''
    • Test if the worker is initialized with the correct name, salary, and energy
    • Test if the worker's energy is incremented after the rest method is called
    • Test if an error is raised if the worker tries to work with negative energy or equal to 0
    • Test if the worker's money is increased by his salary correctly after the work method is called
    • Test if the worker's energy is decreased after the work method is called	
    • Test if the get_info method returns the proper string with correct values
'''


class WorkerTests(unittest.TestCase):
    name = "Ivan"
    salary = 350
    energy = 200

    def test_init__when_correct_name_salary_energy__expect_correct_initilaization(self):
        # arrange + act
        worker = Worker(self.name, self.salary, self.energy)
        # assert
        self.assertEqual(self.name, worker.name)
        self.assertEqual(self.salary, worker.salary)
        self.assertEqual(self.energy, worker.energy)
        self.assertEqual(0, worker.money)

    def test_increment_energy__when_rested__expect_plus_one(self):
        # arrange
        worker = Worker(self.name, self.salary, self.energy)
        self.assertEqual(self.energy, worker.energy)
        self.assertEqual(200, worker.energy)

        # act
        worker.rest()
        # assert
        self.assertEqual(self.energy + 1, worker.energy)
        self.assertEqual(201, worker.energy)

    def test_work__when_energy_zero__expect_exception(self):
        # arrange
        worker = Worker(self.name, self.salary, 0)
        # act
        with self.assertRaises(Exception) as context:
            worker.work()
        # assert
        self.assertEqual('Not enough energy.', str(context.exception))

    def test_work__when_energy_negative__expect_exception(self):
        # arrange
        worker = Worker(self.name, self.salary, -88)
        # act
        with self.assertRaises(Exception) as context:
            worker.work()
        # assert
        self.assertEqual('Not enough energy.', str(context.exception))

    def test_raise_money_by_salary__when_work_method_called__expect_money_plus_salary(self):
        worker = Worker(self.name, self.salary, self.energy)
        self.assertEqual(0, worker.money)
        worker.work()
        # self.assertEqual(self.salary, worker.money)
        self.assertEqual(350, worker.money)
        worker.work()
        # self.assertEqual(self.salary * 2, worker.money)
        self.assertEqual(700, worker.money)

    def test_decrease_energy__when_work_method_called__expect_energy_minus_one(self):
        worker = Worker(self.name, self.salary, self.energy)
        self.assertEqual(self.energy, worker.energy)
        worker.work()
        self.assertEqual(self.energy - 1, worker.energy)
        worker.work()
        self.assertEqual(self.energy - 2, worker.energy)

    def test_get_info__when_called_with__expect_correct_string(self):
        worker = Worker(self.name, self.salary, self.energy)
        # worker.get_info()
        # expected = f'Ivan has saved 0 money.'
        # actual = f'{worker.name} has saved {worker.money} money.'
        expected = f'Ivan has saved 0 money.'
        actual = worker.get_info()

        self.assertEqual(expected, actual)

        worker.work()
        worker.work()
        worker.work()
        worker.work()
        worker.get_info()
        expected = f'Ivan has saved {4 * 350} money.'
        actual = worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
