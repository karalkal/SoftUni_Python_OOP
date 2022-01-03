from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def test_initialisation(self):
        shop = PetShop("SomeName")
        self.assertEqual(shop.name, "SomeName")
        self.assertTrue(type(shop.food) == dict)
        self.assertTrue(type(shop.pets) == list)

    def test_add_food_if_value_zero_or_negative(self):
        shop = PetShop("SomeName")
        with self.assertRaises(ValueError) as context:
            shop.add_food("lajna", 0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(context.exception))

    def test_add_food_if_valid_value_and_increment_if_already_existing_and_output(self):
        shop = PetShop("SomeName")
        shop.add_food("lajna", 20)
        expected = {"lajna": 20}
        actual = shop.food
        self.assertEqual(expected, actual)

        shop.add_food("lajna", 20)
        expected = {"lajna": 40}
        actual = shop.food
        self.assertEqual(expected, actual)

        expected = "Successfully added 20.00 grams of lajna."
        actual = shop.add_food("lajna", 20)
        self.assertEqual(expected, actual)

    def test_add_pet_if_pet_already_in_list(self):
        shop = PetShop("SomeName")
        shop.add_pet("hamster")
        with self.assertRaises(Exception) as context:
            shop.add_pet("hamster")
        self.assertEqual("Cannot add a pet with the same name", str(context.exception))

    def test_add_pet_if_pet_not_in_list(self):
        shop = PetShop("SomeName")
        meth_expected_output = "Successfully added hamster."
        meth_actual_output = shop.add_pet("hamster")
        self.assertEqual(meth_expected_output, meth_actual_output)
        self.assertTrue("hamster" in shop.pets)

    def test_feed_pet_with_no_valid_pet_name(self):
        shop = PetShop("SomeName")
        shop.pets = ["1", "2", "3", "4"]
        shop.add_food("lajna", 20)

        with self.assertRaises(Exception) as context:
            shop.feed_pet("lajna", "8")
        self.assertEqual("Please insert a valid pet name", str(context.exception))

    def test_feed_pet_with_no_valid_food_name(self):
        shop = PetShop("SomeName")
        shop.pets = ["1", "2", "3", "4"]
        shop.food = {"lajna": 20}

        actual = shop.feed_pet("GOVNA", "2")
        self.assertEqual("You do not have GOVNA", actual)

    def test_if_entry_valid_but_food_below_hundred(self):
        shop = PetShop("SomeName")
        shop.pets = ["1", "2", "3", "4"]
        shop.food = {"lajna": 20}
        self.assertEqual(20, shop.food["lajna"])

        actual = shop.feed_pet("lajna", "2")
        self.assertEqual(20 + 1000.00, shop.food["lajna"])
        self.assertEqual("Adding food...", actual)

    def test_everything_is_ok_food_minus_10(self):
        shop = PetShop("SomeName")
        shop.pets = ["1", "2", "3", "4"]
        shop.food = {"lajna": 2000}

        actual = shop.feed_pet("lajna", "2")
        self.assertEqual(1900, shop.food["lajna"])
        self.assertEqual("2 was successfully fed", actual)

    def test_repr(self):
        shop = PetShop("SomeName")
        shop.pets = ["a", "b"]
        shop.food = {"lajna": 2000}
        expected = 'Shop SomeName:\nPets: a, b'
        actual = shop.__repr__()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
