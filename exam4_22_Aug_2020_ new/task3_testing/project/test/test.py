from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def test_init(self):
        card = StudentReportCard("asd", 5)
        self.assertEqual("asd", card.student_name)
        self.assertEqual(5, card.school_year)
        self.assertEqual({}, card.grades_by_subject)

    def test_setter_blank_name_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            card = StudentReportCard("", 5)
        self.assertEqual("Student Name cannot be an empty string!", str(context.exception))
        card = StudentReportCard("asd", 5)
        card.student_name = "ivan"
        self.assertEqual("ivan", card.student_name)
        with self.assertRaises(ValueError) as context:
            card = StudentReportCard("", 5)
        self.assertEqual("Student Name cannot be an empty string!", str(context.exception))

    def test_setter_invalid_year_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            card = StudentReportCard("ivan", 0)
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))
        with self.assertRaises(ValueError) as context:
            card = StudentReportCard("ivan", 13)
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))

    def test_add_grade_if_not_in_dict_add_key__nand_value_if_in_dict_append_to_values(self):
        card = StudentReportCard("asd", 5)
        self.assertEqual({}, card.grades_by_subject)
        card.add_grade("Bio", 4.5)
        self.assertEqual({"Bio": [4.5]}, card.grades_by_subject)
        card.add_grade("Bio", 8)
        self.assertEqual({"Bio": [4.5, 8]}, card.grades_by_subject)
        card.add_grade("Geo", 2.22)
        self.assertEqual({"Bio": [4.5, 8], "Geo": [2.22]}, card.grades_by_subject)

    def test_average_grade_by_subject_expect_correct_string(self):
        card = StudentReportCard("asd", 5)
        card.add_grade("Bio", 4.501)
        self.assertEqual({"Bio": [4.501]}, card.grades_by_subject)
        card.add_grade("Bio", 2.501)
        self.assertEqual({"Bio": [4.501, 2.501]}, card.grades_by_subject)
        card.add_grade("Geo", 2.22222)
        self.assertEqual({"Bio": [4.501, 2.501], "Geo": [2.22222]}, card.grades_by_subject)
        expected = "Bio: 3.50\nGeo: 2.22"
        actual = card.average_grade_by_subject()
        self.assertEqual(expected, actual)

    def test_average_grade_for_all_expect_correct_value(self):
        card = StudentReportCard("asd", 5)
        card.add_grade("Bio", 4.501)
        self.assertEqual({"Bio": [4.501]}, card.grades_by_subject)
        card.add_grade("Bio", 2.501)
        self.assertEqual({"Bio": [4.501, 2.501]}, card.grades_by_subject)
        card.add_grade("Geo", 2.22222)
        self.assertEqual({"Bio": [4.501, 2.501], "Geo": [2.22222]}, card.grades_by_subject)
        self.assertEqual("Average Grade: 3.07", card.average_grade_for_all_subjects())

    def test_repr(self):
        card = StudentReportCard("asd", 5)
        card.add_grade("Bio", 4.501)
        self.assertEqual({"Bio": [4.501]}, card.grades_by_subject)
        card.add_grade("Bio", 2.501)
        self.assertEqual({"Bio": [4.501, 2.501]}, card.grades_by_subject)
        card.add_grade("Geo", 2.22222)
        expected = f"Name: asd\n" \
                   f"Year: 5\n" \
                   f"----------\n" \
                   f"Bio: 3.50\n" \
                   f"Geo: 2.22\n" \
                   f"----------\n" \
                   f"Average Grade: 3.07"
        self.assertEqual(expected, str(card))
        self.assertEqual(expected, card.__repr__())


if __name__ == '__main__':
    main()
