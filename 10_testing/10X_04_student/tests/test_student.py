from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def test_initialization(self):
        student = Student("Ivanushka")
        self.assertEqual("Ivanushka", student.name)
        self.assertEqual({}, student.courses)

        student = Student("Ivanushka", {"Bio": [1, 2, 3], "Sport": [7, 8, 9]})
        self.assertEqual("Ivanushka", student.name)
        self.assertTrue(any([x for x in student.courses if x == "Bio"]))
        self.assertTrue(any([x for x in student.courses if x == "Sport"]))
        self.assertEqual([1, 2, 3], student.courses["Bio"])
        self.assertEqual([7, 8, 9], student.courses["Sport"])

    def test_enrol__if_already_in_course__expect_appended_values_list_and_string_output(self):
        student = Student("Ivanushka", {"Bio": [1, 2, 3], "Sport": [7, 8, 9]})
        expected_output = "Course already added. Notes have been updated."
        actual_output = student.enroll("Bio", [44, 66, 88], "whatever")
        self.assertEqual(expected_output, actual_output)

        expected_list_values = [1, 2, 3, 44, 66, 88]
        actual_list_values = student.courses["Bio"]
        self.assertEqual(expected_list_values, actual_list_values)

    def test_enrol__if_new_course_and_add_notes_blank__expect_new_kvpair_in_course_dict_and_output(self):
        student = Student("Ivanushka", {"Bio": [1, 2, 3]})
        expected_output = "Course and course notes have been added."
	actual_output = student.enroll("Sport", [44, 66, 88])
        self.assertEqual(expected_output, actual_output)

        expected_student_courses = {"Bio": [1, 2, 3], "Sport": [44, 66, 88]}
        actual_student_courses = student.courses
        self.assertEqual(expected_student_courses, actual_student_courses)

    def test_enrol__if_new_course_and_add_notes_Y__expect_new_kvpair_in_course_dict_and_output(self):
        student = Student("Ivanushka", {"Bio": [1, 2, 3]})
        expected_output = "Course and course notes have been added."
        actual_output = student.enroll("Sport", [44, 66, 88], "Y")
        self.assertEqual(expected_output, actual_output)

        expected_student_courses = {"Bio": [1, 2, 3], "Sport": [44, 66, 88]}
        actual_student_courses = student.courses
        self.assertEqual(expected_student_courses, actual_student_courses)

    def test_enrol__if_just_enrolling_on_a_new_course__expect_empty_list_as_value(self):
        student = Student("Ivanushka", {"Bio": [1, 2, 3]})
        expected_output = "Course has been added."
        actual_output = student.enroll("Sport", [44, 66, 88], "ХУЙ")
        self.assertEqual(expected_output, actual_output)

        expected_student_courses = {"Bio": [1, 2, 3], "Sport": []}
        actual_student_courses = student.courses
        self.assertEqual(expected_student_courses, actual_student_courses)

    def test_add_notes__if_course_is_in_dict__expect_extended_list_and_str_output(self):
        student = Student("Ivanushka", {"Bio": [1, 2, 3], "Sport": [7, 8, 9]})
        expected_output = "Notes have been updated"
        actual_output = student.add_notes("Bio", 8888)
        self.assertEqual(expected_output, actual_output)

        expected_bio_values = [1, 2, 3, 8888]
        actual_bio_values = student.courses["Bio"]
        self.assertEqual(expected_bio_values, actual_bio_values)

    def test_add_notes__if_course_is_not_in_dict__raise_error(self):
        student = Student("Ivanushka", {"Bio": [1, 2, 3], "Sport": [7, 8, 9]})
        with self.assertRaises(Exception) as context:
            student.add_notes("Geo", 8888)
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_leave_course_if_course_is_in_dict__expect_not_in_list_and_str_output(self):
        student = Student("Ivanushka", {"Bio": [1, 2, 3], "Sport": [7, 8, 9]})
        expected_output = "Course has been removed"
        actual_output = student.leave_course("Bio")
        self.assertEqual(expected_output, actual_output)

        expected_student_courses = {"Sport": [7, 8, 9]}
        actual_student_courses = student.courses
        self.assertEqual(expected_student_courses, actual_student_courses)

    def test_leave_course__if_course_is_not_in_dict__raise_error(self):
        student = Student("Ivanushka", {"Bio": [1, 2, 3], "Sport": [7, 8, 9]})
        with self.assertRaises(Exception) as context:
            student.leave_course("Geo")
        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))


if __name__ == "__main__":
    main()
