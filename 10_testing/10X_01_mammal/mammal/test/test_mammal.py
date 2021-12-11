from project.mammal import Mammal

import unittest


class TestMammal(unittest.TestCase):
    def test_constructor__with_valid_values__expect_correct_instance(self):
        donald = Mammal("Trump", "idiot", "gruh")
        self.assertEqual("Trump", donald.name)
        self.assertEqual("idiot", donald.type)
        self.assertEqual("gruh", donald.sound)
        self.assertEqual("animals", donald._Mammal__kingdom)

    def test_make_sound_meth__with_existing_instance__expect_sting(self):
        boris = Mammal("Johnson", "wanker", "oink")
        self.assertEqual("Johnson makes oink", boris.make_sound())

    def test_display_kingom__with_animals_default__expect_kigdom(self):
        donald = Mammal("Trump", "idiot", "gruh")
        self.assertEqual("animals", donald.get_kingdom())

        # CANNOT AMEND PRIVATE ATTs
        # boris = Mammal("Johnson", "wanker", "oink")
        # boris._Mammal__kingdom = "UK"
        # self.assertEqual("UK", boris.get_kingdom())

    def test_info__with_existing_instance__expect_str_name_and_type(self):
        tikvata = Mammal("Boko", "fat cunt", "bulyu, bulyu")
        self.assertEqual("Boko is of type fat cunt", tikvata.info())


if __name__ == "__main__":
    unittest.main()
