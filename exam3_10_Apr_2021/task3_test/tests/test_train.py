from project.train.train import Train
from unittest import TestCase, main


class TestTrain(TestCase):
    def test_constants_class_attributes(self):
        vlak = Train("Name", 88)
        actual = vlak.TRAIN_FULL
        self.assertEqual("Train is full", actual)
        actual = vlak.PASSENGER_EXISTS
        self.assertEqual("Passenger {} Exists", actual)
        actual = vlak.PASSENGER_NOT_FOUND  #
        self.assertEqual("Passenger Not Found", actual)
        actual = vlak.PASSENGER_ADD
        self.assertEqual("Added passenger {}", actual)
        actual = vlak.PASSENGER_REMOVED
        self.assertEqual("Removed {}", actual)
        actual = vlak.ZERO_CAPACITY
        self.assertEqual(0, actual)

    def test_init(self):
        vlak = Train("Name", 88)
        self.assertEqual("Name", vlak.name)
        self.assertEqual(88, vlak.capacity)
        self.assertTrue(type(vlak.passengers) == list)

    def test_add_passenger_if_full(self):
        vlak = Train("Name", 4)
        vlak.passengers = ["a", "b", "c", "d"]
        with self.assertRaises(ValueError) as context:
            vlak.add("8888")
        self.assertEqual("Train is full", str(context.exception))

    def test_add_passenger_if_passenger_already_on_train(self):
        vlak = Train("Name", 4)
        vlak.passengers = ["a", "b"]
        with self.assertRaises(ValueError) as context:
            vlak.add("a")
        self.assertEqual("Passenger a Exists", str(context.exception))

    def test_add_passenger_with_valid_entries(self):
        vlak = Train("Name", 5)
        vlak.passengers = ["a", "b", "c", "d"]
        returned_string = vlak.add("8888")
        self.assertEqual(returned_string, "Added passenger 8888")
        self.assertEqual(["a", "b", "c", "d", "8888"], vlak.passengers)

    def test_remove_passenger_if_not_on_train(self):
        vlak = Train("Name", 5)
        vlak.passengers = ["a", "b", "c", "d"]
        with self.assertRaises(ValueError) as context:
            vlak.remove("8888")
        self.assertEqual("Passenger Not Found", str(context.exception))

    def test_remove_with_valid_entry(self):
        vlak = Train("Name", 5)
        vlak.passengers = ["a", "b", "c", "d"]
        returned_string = vlak.remove("a")
        self.assertEqual(returned_string, "Removed a")
        self.assertEqual(["b", "c", "d"], vlak.passengers)


if __name__ == "__main__":
    main()
