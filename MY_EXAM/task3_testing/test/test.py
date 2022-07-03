from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def test_correct_initialization(self):
        levski = Team("Levski")
        self.assertEqual("Levski", levski.name)
        self.assertEqual({}, levski.members)

    def test_name_setter_can_contain_only_alpha_raises(self):
        with self.assertRaises(ValueError) as context:
            levski = Team("123")
        self.assertEqual("Team Name can contain only letters!", str(context.exception))
        with self.assertRaises(ValueError) as context:
            levski = Team("Levski1")
        self.assertEqual("Team Name can contain only letters!", str(context.exception))
        with self.assertRaises(ValueError) as context:
            levski = Team("Levski+")
        self.assertEqual("Team Name can contain only letters!", str(context.exception))

    def test_add_member_adding_new_member_successfully(self, **name_age):
        levski = Team("Levski")
        expected = "Successfully added: Ronaldo"
        actual = levski.add_member(**{"Ronaldo": 23})
        self.assertEqual(expected, actual)
        self.assertEqual({"Ronaldo": 23}, levski.members)

        expected = "Successfully added: Messi, Kante, Drogba"
        actual = levski.add_member(**{"Messi": 25, "Kante": 22, "Drogba": 24})
        self.assertEqual(expected, actual)
        self.assertEqual({"Ronaldo": 23, "Messi": 25, "Kante": 22, "Drogba": 24}, levski.members)

    def test_remove_member_with_valid_name(self):
        levski = Team("Levski")
        expected = "Member Messi removed"
        levski.add_member(**{"Messi": 25, "Kante": 22, "Drogba": 24})
        actual = levski.remove_member("Messi")
        self.assertEqual(expected, actual)
        self.assertEqual({"Kante": 22, "Drogba": 24}, levski.members)

    def test_remove_member_with_invalid_name_raises(self):
        levski = Team("Levski")
        levski.add_member(**{"Messi": 25, "Kante": 22, "Drogba": 24})
        expected = "Member with name Ivan does not exist"
        actual = levski.remove_member("Ivan")
        self.assertEqual(expected, actual)
        self.assertEqual({"Messi": 25, "Kante": 22, "Drogba": 24}, levski.members)

    def test___gt___method_first_team_len_greater_than_second_expect_true(self):
        levski = Team("Levski")
        levski.add_member(**{"Messi": 25, "Kante": 22, "Drogba": 24})
        cska = Team("CSKA")
        cska.add_member(**{"Ristju": 25})
        self.assertTrue(len(levski) > len(cska))
        expected = True
        actual = levski > cska
        self.assertEqual(expected, actual)

    def test___gt___method_first_team_same_len_as_second_expact_false(self):
        levski = Team("Levski")
        levski.add_member(**{"Messi": 25, "Kante": 22, "Drogba": 24})
        cska = Team("CSKA")
        cska.add_member(**{"Ristju": 65, "Gyz": 55, "Pehso": 44})
        self.assertFalse(len(levski) > len(cska))
        expected = False
        actual = levski > cska
        self.assertEqual(expected, actual)

    def test___len___method(self):
        levski = Team("Levski")
        levski.add_member(**{"Messi": 25, "Kante": 22, "Drogba": 24})
        expected = 3
        actual = len(levski)
        self.assertEqual(expected, actual)

    def test___add___meth(self):
        levski = Team("Levski")
        levski.add_member(**{"Messi": 25, "Kante": 22, "Drogba": 24})
        cska = Team("CSKA")
        cska.add_member(**{"Ristju": 25})
        actual_new_team_name = (levski + cska).name
        expected_name = "LevskiCSKA"
        self.assertEqual(expected_name, actual_new_team_name)

        actual_new_team_members = (levski + cska).members
        expected_members = {"Messi": 25, "Kante": 22, "Drogba": 24, "Ristju": 25}
        self.assertEqual(expected_members, actual_new_team_members)

    def test___str___(self):
        levski = Team("Levski")
        levski.add_member(**{"Messi": 25, "Kante": 22, "Drogba": 24})
        expected = f"Team name: Levski\nMember: Messi - 25-years old\nMember: Drogba - 24-years old\nMember: Kante - 22-years old"
        self.assertEqual(expected, str(levski))


if __name__ == "__main__":
    main()
