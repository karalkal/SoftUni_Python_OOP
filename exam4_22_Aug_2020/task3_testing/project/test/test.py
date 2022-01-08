from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def test_initialisation(self):
        student = StudentReportCard("Ivan", 4)

        self.assertEqual("Ivan", student.student_name)
        self.assertEqual(4, student.school_year)

    def test_name_setter_if_blank_raises(self):
        with self.assertRaises(ValueError) as context:
            student = StudentReportCard("df", 4)
        self.assertEqual("Student Name cannot be an empty string!", str(context.exception))

    def test_year_setter_if_not_in_range(self):
        student = StudentReportCard("Ivan", 4)
        with self.assertRaises(ValueError) as context:
            student.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))

        student = StudentReportCard("Ivan", 4)
        with self.assertRaises(ValueError) as context:
            student.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))

    def test_add_grade_adding_grades_by_subject(self):
        student = StudentReportCard("Ivan", 4)
        self.assertEqual({}, student.grades_by_subject)
        student.add_grade("Biology", 5.5)
        self.assertEqual({"Biology": [5.5]}, student.grades_by_subject)
        student.add_grade("Biology", 3.5)
        self.assertEqual({"Biology": [5.5, 3.5]}, student.grades_by_subject)
        student.add_grade("English", 2)
        self.assertEqual({"Biology": [5.5, 3.5], "English": [2]}, student.grades_by_subject)
        student.add_grade("English", 6)
        self.assertEqual({"Biology": [5.5, 3.5], "English": [2, 6]}, student.grades_by_subject)
        student.add_grade("BullShit", "nishto")
        self.assertEqual({"Biology": [5.5, 3.5], "English": [2, 6], "BullShit": ["nishto"]}, student.grades_by_subject)



    def test_average_grade_by_subject(self):
        student = StudentReportCard("Ivan", 4)
        student.add_grade("Biology", 5.5)
        student.add_grade("Biology", 3.5)
        student.add_grade("English", 2)
        student.add_grade("English", 6)
        expected = "Biology: 4.50\nEnglish: 4.00"

        self.assertEqual(expected, student.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        student = StudentReportCard("Ivan", 4)
        student.add_grade("Biology", 5.5)
        student.add_grade("Biology", 3.5)
        student.add_grade("English", 2)
        student.add_grade("English", 6)

        expected = "Average Grade: 4.25"
        self.assertEqual(expected, student.average_grade_for_all_subjects())

    def test_repr(self):
        student = StudentReportCard("Ivan", 4)
        student.add_grade("Biology", 5.5)
        student.add_grade("Biology", 3.5)
        student.add_grade("English", 2)
        student.add_grade("English", 6)

        expected = "Name: Ivan\nYear: 4\n----------\nBiology: 4.50\nEnglish: 4.00\n----------\nAverage Grade: 4.25"
        self.assertEqual(expected, str(student))

        if __name__ == "__main__":
            main()
