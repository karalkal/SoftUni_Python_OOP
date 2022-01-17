from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory
from project.factory.paint_factory import Factory


class TestPaintFactory(TestCase):
    def test_initialization(self):
        factory = PaintFactory("name", 88)
        self.assertEqual("name", factory.name)
        self.assertEqual(88, factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], factory.valid_ingredients)
        self.assertEqual({}, factory.ingredients)

    def test_add_ingredient_with_valid_ingredient_and_can_add_expect_to_add_if_new_and_increase_value(self):
        factory = PaintFactory("name", 88)
        factory.add_ingredient("white", 22)
        self.assertEqual({"white": 22}, factory.ingredients)
        factory.add_ingredient("blue", 22)
        self.assertEqual({"white": 22, "blue": 22}, factory.ingredients)
        factory.add_ingredient("white", 22)
        self.assertEqual({"white": 44, "blue": 22}, factory.ingredients)
        factory.add_ingredient("blue", 22)
        self.assertEqual({"white": 44, "blue": 44}, factory.ingredients)

    def test_add_ingredient_with_valid_ingredient_cannot_add_raises_value_error(self):
        factory = PaintFactory("name", 44)
        factory.add_ingredient("white", 22)
        self.assertEqual({"white": 22}, factory.ingredients)
        factory.add_ingredient("blue", 22)
        self.assertEqual({"white": 22, "blue": 22}, factory.ingredients)
        with self.assertRaises(ValueError) as context:
            factory.add_ingredient("white", 22)
        self.assertEqual("Not enough space in factory", str(context.exception))

    def test_add_ingredient_with_invalid_ingredient_cannot_add_raises_type_error(self):
        factory = PaintFactory("name", 88)
        factory.add_ingredient("white", 22)
        self.assertEqual({"white": 22}, factory.ingredients)
        factory.add_ingredient("blue", 22)
        self.assertEqual({"white": 22, "blue": 22}, factory.ingredients)
        with self.assertRaises(TypeError) as context:
            factory.add_ingredient("pink", 22)
        self.assertEqual("Ingredient of type pink not allowed in PaintFactory", str(context.exception))

    def test_remove_ingredient_with_valid_values_expect_to_reduce_value(self):
        factory = PaintFactory("name", 88)
        factory.add_ingredient("white", 22)
        self.assertEqual({"white": 22}, factory.ingredients)
        factory.add_ingredient("blue", 22)
        self.assertEqual({"white": 22, "blue": 22}, factory.ingredients)
        factory.remove_ingredient("white", 11)
        self.assertEqual({"white": 11, "blue": 22}, factory.ingredients)
        factory.remove_ingredient("blue", 22)
        self.assertEqual({"white": 11, "blue": 0}, factory.ingredients)

    def test_remove_ingredient_with_valid_value_but_more_than_available_raises_value_error(self):
        factory = PaintFactory("name", 88)
        factory.add_ingredient("white", 22)
        self.assertEqual({"white": 22}, factory.ingredients)
        factory.add_ingredient("blue", 22)
        self.assertEqual({"white": 22, "blue": 22}, factory.ingredients)
        factory.remove_ingredient("white", 11)
        self.assertEqual({"white": 11, "blue": 22}, factory.ingredients)
        with self.assertRaises(ValueError) as context:
            factory.remove_ingredient("white", 12)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))

    def test_remove_ingredient_with_valid_value_but_more_than_available_raises_value_error(self):
        factory = PaintFactory("name", 88)
        factory.add_ingredient("white", 22)
        self.assertEqual({"white": 22}, factory.ingredients)
        factory.add_ingredient("blue", 22)
        self.assertEqual({"white": 22, "blue": 22}, factory.ingredients)
        factory.remove_ingredient("white", 11)
        self.assertEqual({"white": 11, "blue": 22}, factory.ingredients)
        with self.assertRaises(KeyError) as context:
            factory.remove_ingredient("red", 11)
        self.assertEqual("'No such ingredient in the factory'", str(context.exception))

    def test_property(self):
        factory = PaintFactory("name", 88)
        factory.add_ingredient("white", 22)
        self.assertEqual({"white": 22}, factory.ingredients)
        factory.add_ingredient("blue", 22)
        self.assertEqual({"white": 22, "blue": 22}, factory.ingredients)
        self.assertEqual({"white": 22, "blue": 22}, factory.products)

    def test_factory_base_class_try_to_instantiate_raise_error(self):  # not required
        expected_message = "Can't instantiate abstract class Factory with abstract methods __init__, add_ingredient, remove_ingredient"
        with self.assertRaises(TypeError) as context:
            factory = Factory("somename", 22)
        self.assertEqual(expected_message, str(context.exception))


if __name__ == "__main__":
    main()
