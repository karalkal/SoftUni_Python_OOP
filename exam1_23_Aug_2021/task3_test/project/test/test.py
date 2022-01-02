from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def test_correct_initialisation(self):
        library = Library("new_library")
        self.assertEqual(library.name, "new_library")
        self.assertTrue(type(library.books_by_authors) == dict)
        self.assertTrue(type(library.readers) == dict)

    def test_setter_if_empty_string_raise_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.library = Library("")
        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test_add_book_if_author_not_in_books_by_authors_dict_append_to_dict(self):
        library = Library("New Lib")
        library.add_book("Tolstoy", "war and peace")
        expected_output = {"Tolstoy": ["war and peace"]}
        actual_output = library.books_by_authors

        self.assertEqual(expected_output, actual_output)

    def test_add_book_if_author_in_dict_add_new_book(self):
        library = Library("New Lib")
        library.books_by_authors = {"ivan": [1, 2, 3], "pesho": [7, 8, 9]}
        library.add_book("ivan", 8888)
        expected_output = {"ivan": [1, 2, 3, 8888], "pesho": [7, 8, 9]}
        actual_output = library.books_by_authors

        self.assertEqual(expected_output, actual_output)

    def test_if_new_reader_added(self):
        library = Library("New Lib")
        library.add_reader("Orlin")
        library.add_reader("Kalin")
        expected_output = {"Orlin": [], "Kalin": []}
        actual_output = library.readers

        self.assertEqual(expected_output, actual_output)

    def test_if_user_already_registered_raises(self):
        library = Library("New Lib")
        library.add_reader("Orlin")
        library.add_reader("Kalin")
        expected_output = "Kalin is already registered in the New Lib library."
        actual_output = library.add_reader("Kalin")
        self.assertEqual(expected_output, actual_output)

    def test_rent_book_user_not_reg(self):
        library = Library("New Lib")
        library.add_reader("Orlin")
        expected = "Kalin is not registered in the New Lib Library."
        actual = library.rent_book("Kalin", "nishto", "nishto")

        self.assertEqual(expected, actual)

    def test_rent_book_no_books_by_author(self):
        library = Library("New Lib")
        library.add_reader("Orlin")
        library.books_by_authors = {"ivan": [1, 2, 3], "pesho": [7, 8, 9]}
        expected = "New Lib Library does not have any KURCHO's books."
        actual = library.rent_book("Orlin", "KURCHO", "nishto")

        self.assertEqual(expected, actual)

    def test_rent_book_book_doesnt_exist(self):
        library = Library("New Lib")
        library.add_reader("Orlin")
        library.books_by_authors = {"ivan": [1, 2, 3], "pesho": [7, 8, 9]}
        expected = 'New Lib Library does not have ivan\'s "knigata".'
        actual = library.rent_book("Orlin", "ivan", "knigata")

        self.assertEqual(expected, actual)

    def test_add_book_to_readers_dict(self):
        library = Library("New Lib")
        library.add_reader("Orlin")
        library.books_by_authors = {"ivan": ["knigata"], "pesho": [7, 8, 9]}
        library.rent_book("Orlin", "ivan", "knigata")
        expected = {"Orlin": [{"ivan": "knigata"}]}
        actual = library.readers

        self.assertEqual(expected, actual)

    def test_book_title_index(self):
        library = Library("New Lib")
        library.add_reader("Orlin")
        library.books_by_authors = {"pesho": [7, 8, 9]}
        expected = 1
        actual = library.books_by_authors["pesho"].index(8)

        self.assertEqual(expected, actual)

    def test_book_is_removed(self):
        library = Library("New Lib")
        library.add_reader("Orlin")
        library.books_by_authors = {"ivan": ["knigata"], "pesho": [7, 8, 9]}
        library.rent_book("Orlin", "ivan", "knigata")
        expected = {'ivan': [], 'pesho': [7, 8, 9]}
        actual = library.books_by_authors

        self.assertEqual(expected, actual)


    # del self.books_by_authors[book_author][book_title_index]


if __name__ == "__main__":
    main()
