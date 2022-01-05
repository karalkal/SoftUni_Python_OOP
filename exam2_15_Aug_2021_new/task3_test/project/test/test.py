from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPestShop(TestCase):
    def test_correct_initialization(self):
        shop = PetShop("Pesho")
        self.assertEqual("Pesho", shop.name)
        self.assertTrue(type(shop.food) == dict)
        self.assertTrue(type(shop.pets) == list)

    def test_add_food_with_negative_and_zero_value_raises_value_error(self):
        shop = PetShop("Pesho")
        with self.assertRaises(ValueError) as context:
            shop.add_food("rice", -5.388)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))
        with self.assertRaises(ValueError) as context:
            shop.add_food("rice", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food_with_valid_value_expected_to_create_key_with_quantity_first_then_increases_plus_message(self):
        shop = PetShop("Pesho")
        shop.add_food("rice", 8.888)
        self.assertEqual({"rice": 8.888}, shop.food)
        shop.add_food("meat", 6.666)
        self.assertEqual({"rice": 8.888, "meat": 6.666}, shop.food)
        shop.add_food("meat", 2.222)
        self.assertEqual({"rice": 8.888, "meat": 8.888}, shop.food)
        expected_message = "Successfully added 2.22 grams of meat."
        actual_message = shop.add_food("meat", 2.222)
        self.assertEqual(expected_message, actual_message)

    def test_add_pet_if_pet_not_in_list_appends_to_list_and_displays_message(self):
        shop = PetShop("Pesho")
        expected_message = "Successfully added Doggy."
        actual_message = shop.add_pet("Doggy")
        self.assertEqual(expected_message, actual_message)
        self.assertEqual(["Doggy"], shop.pets)

    def test_add_pet_if_pet_in_list_raises_exception(self):
        shop = PetShop("Pesho")
        shop.add_pet("Doggy")
        self.assertEqual(["Doggy"], shop.pets)
        with self.assertRaises(Exception) as context:
            shop.add_pet("Doggy")
        self.assertEqual("Cannot add a pet with the same name", str(context.exception))
        self.assertEqual(["Doggy"], shop.pets)

    def test_feed_pet_if_not_pet_name_in_list_raises_exception(self):
        shop = PetShop("Pesho")
        shop.add_pet("Doggy")
        with self.assertRaises(Exception) as context:
            shop.feed_pet("fish", "Pussy")
        self.assertEqual("Please insert a valid pet name", str(context.exception))

    def test_feed_pet_if_pet_in_list_but_no_such_food_returns_message(self):
        shop = PetShop("Pesho")
        shop.add_food("rice", 8.888)
        self.assertEqual({"rice": 8.888}, shop.food)
        shop.add_food("meat", 6.666)
        shop.add_pet("Doggy")
        shop.add_pet("Pussy")
        expected_returned_str = "You do not have fish"
        actual_returned_str = shop.feed_pet("fish", "Pussy")
        self.assertEqual(expected_returned_str, actual_returned_str)

    def test_feed_pet_if_pet_in_list_but_food_quantity_below_returns_message_and_adds_1000_to_value_in_food_dict(self):
        shop = PetShop("Pesho")
        shop.add_pet("Doggy")
        shop.add_food("meat", 99.99)
        self.assertEqual({"meat": 99.99}, shop.food)
        expected_returned_str = "Adding food..."
        actual_returned_str = shop.feed_pet("meat", "Doggy")
        self.assertEqual(expected_returned_str, actual_returned_str)
        self.assertEqual({"meat": 1099.99}, shop.food)

    def test_feed_pet_if_pet_in_list_food_quantity_enough_returns_message_and_subtracts_100_from_value_in_food_dict(
            self):
        shop = PetShop("Pesho")
        shop.add_pet("Doggy")
        shop.add_food("meat", 200)
        expected_returned_str = "Doggy was successfully fed"
        actual_returned_str = shop.feed_pet("meat", "Doggy")
        self.assertEqual(expected_returned_str, actual_returned_str)
        self.assertEqual({"meat": 100}, shop.food)

    def test_repr(self):
        shop = PetShop("Pesho")
        shop.add_pet("Doggy")
        shop.add_pet("Pussy")
        expected_returned_str = 'Shop Pesho:\nPets: Doggy, Pussy'
        actual_returned_str = str(shop)
        self.assertEqual(expected_returned_str, actual_returned_str)

        expected_returned_str = 'Shop Pesho:\nPets: Doggy, Pussy'
        expected_returned_str = 'Shop Pesho:\nPets: Doggy, Pussy'
        actual_returned_str = shop.__repr__()
        self.assertEqual(expected_returned_str, actual_returned_str)

if __name__ == "__main__":
    main()
