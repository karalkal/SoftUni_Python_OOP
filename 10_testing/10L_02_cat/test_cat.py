from cat import Cat

"""
• Cat's size is increased after eating
• Cat is fed after eating
• Cat cannot eat if already fed, raises an error
• Cat cannot fall asleep if not fed, raises an error
• Cat is not sleepy after sleeping
"""

import unittest


class CatTest(unittest.TestCase):
    def test_size_increses__when_eating__expect_plus_one(self):
        gosho = Cat("Goshko")
        expected = 0
        actual = gosho.size
        self.assertEqual(expected, actual)

        gosho.eat()
        expected = 1
        actual = gosho.size
        self.assertEqual(expected, actual)

    def test_is_fed__after_eating__fed_true(self):
        gosho = Cat("Goshko")
        self.assertEqual(False, gosho.fed)
        self.assertFalse(gosho.fed)

        gosho.eat()
        self.assertEqual(True, gosho.fed)
        self.assertTrue(gosho.fed)

    def test_cannot_eat__when_fed__raises_exception(self):
        # arrange
        gosho = Cat("Goshko")
        gosho.fed = True
        # act
        with self.assertRaises(Exception) as context:
            gosho.eat()
        # assert
        self.assertEqual('Already fed.', str(context.exception))

    def test_cannot_sleep__when_hungry__raises_exception(self):
        # arrange
        gosho = Cat("Goshko")
        gosho.fed = False
        # act
        with self.assertRaises(Exception) as context:
            gosho.sleep()
        # assert
        self.assertEqual('Cannot sleep while hungry', str(context.exception))

    def test_not_sleepy__after_sleep__expect_sleepy_false(self):
        # arrange
        gosho = Cat("Goshko")
        gosho.sleepy = True
        self.assertEqual(True, gosho.sleepy)
        gosho.fed = True
        gosho.sleep()
        self.assertEqual(False, gosho.sleepy)


if __name__ == "__main__":
    unittest.main()
