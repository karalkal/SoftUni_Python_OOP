from project.factory.paint_factory import PaintFactory
from unittest import TestCase, main


class TestPaitFactory(TestCase):

    def test_correct_initialisation(self):
        factory = PaintFactory("Kaput", 1000)
        self.assertEqual("Kaput", factory.name)
        self.assertEqual(1000, factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], factory.valid_ingredients)
        self.assertEqual({}, factory.ingredients)

    def test_add_ingredient_if_product_type_in_valid_ingredients_and_can_add(self):
        factory = PaintFactory("Kaput", 1000)
        factory.add_ingredient("white", 44)
        self.assertEqual({"white": 44}, factory.ingredients)
        factory.add_ingredient("red", 22)
        self.assertEqual({"white": 44, "red": 22}, factory.ingredients)
        # adding extra quantity
        factory.add_ingredient("red", 22)
        self.assertEqual({"white": 44, "red": 44}, factory.ingredients)

    def test_add_ingredient_if_product_type_in_valid_ingredients_but_cannot_add_raises(self):
        factory = PaintFactory("Kaput", 66)
        factory.add_ingredient("white", 44)
        factory.add_ingredient("red", 22)
        with self.assertRaises(ValueError) as context:
            factory.add_ingredient("red", 1)
        self.assertEqual("Not enough space in factory", str(context.exception))
        with self.assertRaises(ValueError) as context:
            factory.add_ingredient("blue", 1)
        self.assertEqual("Not enough space in factory", str(context.exception))


    def test_add_ingredient_with_invalid_colour_raises(self):
        factory = PaintFactory("Kaput", 66)
        factory.add_ingredient("white", 44)
        factory.add_ingredient("red", 22)
        with self.assertRaises(TypeError) as context:
            factory.add_ingredient("gyz", 22)
        self.assertEqual("Ingredient of type gyz not allowed in PaintFactory", str(context.exception))


    def test_remove_ingredient_if_product_type_in_ingredients_and_enough_quantity(self):
        factory = PaintFactory("Kaput", 66)
        factory.add_ingredient("white", 44)
        factory.add_ingredient("red", 22)
        factory.remove_ingredient("white", 44)
        self.assertEqual({"white": 0, "red": 22}, factory.ingredients)
        factory.remove_ingredient("red", 22)
        self.assertEqual({"white": 0, "red": 0}, factory.ingredients)

    def test_remove_ingredient_if_product_type_in_ingredients_and_not_enough_quantity_raises(self):
        factory = PaintFactory("Kaput", 66)
        factory.add_ingredient("white", 44)
        with self.assertRaises(ValueError) as context:
            factory.remove_ingredient("white", 45)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))


    def test_remove_ingredient_if_product_type_not_in_ingredients_raiese(self):
        factory = PaintFactory("Kaput", 66)
        factory.add_ingredient("white", 44)
        with self.assertRaises(KeyError) as context:
            factory.remove_ingredient("red", 22)
        self.assertEqual("'No such ingredient in the factory'", str(context.exception))

    def test_property_products(self):
        factory = PaintFactory("Kaput", 88)
        factory.add_ingredient("white", 44)
        factory.add_ingredient("red", 44)
        self.assertEqual({"white": 44, "red": 44}, factory.products)


if __name__ == "__main__":
    main()
