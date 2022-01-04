from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def test_init(self):
        lib = Library("Kingson")
        self.assertEqual("Kingson", lib.name)
        self.assertTrue(type(lib.books_by_authors) == dict)
        self.assertTrue(type(lib.readers) == dict)

    def test_name_setter_with_empty_string_raises(self):
        with self.assertRaises(ValueError) as context:
            lib = Library("")
        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test_add_book_if_author_not_in_authors_dict_add_author_and_book(self):
        lib = Library("Kingston")
        lib.add_book("Ivan", "Pod Igoto")
        self.assertEqual({"Ivan": ["Pod Igoto"]}, lib.books_by_authors)
        lib.add_book("Kalin", "Нищо")
        self.assertEqual({"Ivan": ["Pod Igoto"], "Kalin": ["Нищо"]}, lib.books_by_authors)

    def test_add_book_if_author_in_authors_dict_expect_append_to_auhtors_list(self):
        lib = Library("Kingston")
        lib.add_book("Ivan", "Pod Igoto")
        lib.add_book("Ivan", "Druga Kniga")
        lib.add_book("Ivan", "Pod Igoto")
        self.assertEqual({"Ivan": ["Pod Igoto", "Druga Kniga"]}, lib.books_by_authors)

    def test_add_reader_if_name_not_readers_dict_expect_to_add(self):
        lib = Library("Kingson")
        lib.add_reader("Vasko")
        self.assertEqual({"Vasko": []}, lib.readers)

    def test_add_reader_if_name_in_readers_dict_return_error_message_dict_remains_unchanged(self):
        lib = Library("Kingston")
        lib.add_reader("Vasko")

        expected = "Vasko is already registered in the Kingston library."
        actual = lib.add_reader("Vasko")
        self.assertEqual(expected, actual)

        self.assertEqual({"Vasko": []}, lib.readers)

    def test_rent_book_if_reader_not_in_dict_return_error_message(self):
        lib = Library("Kingston")
        lib.add_reader("Vasko")

        expected = "Kalin is not registered in the Kingston Library."
        actual = lib.rent_book("Kalin", 1, 2)
        self.assertEqual(expected, actual)

        self.assertEqual({"Vasko": []}, lib.readers)

    def test_rent_book_if_author_not_in_dict_return_error_message(self):
        lib = Library("Kingston")
        lib.add_reader("Vasko")
        lib.add_book("Ivan", "Pod Igoto")
        lib.add_book("Ivan", "Druga Kniga")
        expected = "Kingston Library does not have any Pesho's books."
        actual = lib.rent_book("Vasko", "Pesho", 8)
        self.assertEqual(expected, actual)

    def test_rent_book_if_author_in_dict_but_no_such_book_return_error_message(self):
        lib = Library("Kingston")
        lib.add_reader("Vasko")
        lib.add_book("Ivan", "Pod Igoto")
        expected = f"""Kingston Library does not have Ivan's "aa"."""
        actual = lib.rent_book("Vasko", "Ivan", "aa")
        self.assertEqual(expected, actual)

    def test_rent_book_if_all_is_fine_adds_book_to_this_readers_list(self):
        lib = Library("Kingston")
        lib.add_reader("Vasko")
        self.assertEqual({"Vasko": []}, lib.readers)

        lib.add_book("Ivan", "Pod Igoto")
        lib.rent_book("Vasko", "Ivan", "Pod Igoto")
        self.assertEqual({"Vasko": [{"Ivan": "Pod Igoto"}]}, lib.readers)

    def test_rent_book_if_all_is_fine_returns_removes_book_from_authors_dict_values(self):
        lib = Library("Kingston")
        lib.add_reader("Vasko")
        self.assertEqual({"Vasko": []}, lib.readers)

        lib.add_book("Ivan", "1")
        lib.add_book("Ivan", "2")
        lib.add_book("Ivan", "3")
        lib.add_book("Ivan", "Pod Igoto")
        lib.add_book("Ivan", "4")
        lib.add_book("Ivan", "5")
        self.assertEqual({"Ivan": ["1", "2", "3", "Pod Igoto", "4", "5"]}, lib.books_by_authors)
        lib.rent_book("Vasko", "Ivan", "Pod Igoto")
        self.assertEqual({"Ivan": ["1", "2", "3", "4", "5"]}, lib.books_by_authors)


if __name__ == "__main__":
    main()
