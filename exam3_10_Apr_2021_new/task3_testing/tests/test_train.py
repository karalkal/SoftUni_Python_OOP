from project.train.train import Train
from unittest import TestCase, main


class TestTrain(TestCase):
    def test_init(self):
        express = Train("Bullet", 88)
        self.assertEqual("Bullet", express.name)
        self.assertEqual(88, express.capacity)
        self.assertEqual([], express.passengers)
        self.assertEqual("Train is full", express.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", express.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", express.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", express.PASSENGER_ADD)
        self.assertEqual("Removed {}", express.PASSENGER_REMOVED)
        self.assertEqual(0, express.ZERO_CAPACITY)

    def test_add_passenger_when_train_is_full_raises_value_error(self):
        express = Train("Bullet", 8)
        express.passengers = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(len(express.passengers), express.capacity)
        with self.assertRaises(ValueError) as context:
            express.add(88)
        self.assertEqual("Train is full", str(context.exception))

    def test_add_passenger_if_passenger_name_already_in_list_value_error(self):
        express = Train("Bullet", 88)
        express.passengers = [1, 2, 3, 4, 5, 6, 7, 8]
        with self.assertRaises(ValueError) as context:
            express.add(8)
        self.assertEqual("Passenger 8 Exists", str(context.exception))

    def test_add_passenger_if_enough_space_and_name_not_in_list_expect_to_append_and_return_message(self):
        express = Train("Bullet", 88)
        express.passengers = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], express.passengers)
        express.add(88)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 88], express.passengers)
        expected = "Added passenger 8888"
        actual = express.add(8888)
        self.assertEqual(expected, actual)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 88, 8888], express.passengers)

    def test_remove_if_passenger_not_in_list(self):
        express = Train("Bullet", 88)
        express.passengers = [1, 2, 3, 4, 5, 6, 7, 8]
        with self.assertRaises(ValueError) as context:
            express.remove(88)
        self.assertEqual("Passenger Not Found", str(context.exception))

    def test_remove_passenger_if_name_in_list_expect_to_remove_and_return_message(self):
        express = Train("Bullet", 88)
        express.passengers = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], express.passengers)
        expected = "Removed 8"
        actual = express.remove(8)
        self.assertEqual(expected, actual)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], express.passengers)


if __name__ == '__main__':
    main()
