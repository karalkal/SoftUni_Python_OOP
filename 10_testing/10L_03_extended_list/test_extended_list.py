from extended_list import IntegerList

import unittest


class TestIntegerList(unittest.TestCase):
    def test_constructor__can_contain_only_integers(self):
        # arrange + act
        the_list = IntegerList(1, 2, 3, "a", True, False, [44, 22], 77.22, 365)
        expected = [1, 2, 3, 365]
        self.assertEqual(expected, the_list._IntegerList__data)

    def test_add__with_valid_entry__expect_new_entry_in_list(self):
        the_list = IntegerList(1, 2, 3, 365)
        the_list.add(88)
        expected = [1, 2, 3, 365, 88]
        self.assertEqual(expected, the_list._IntegerList__data)

    def test_add__with_invalid_entry__raise_value_error(self):
        the_list = IntegerList(1, 2, 3, 365)
        with self.assertRaises(ValueError) as context:
            the_list.add("88")
        self.assertEqual("Element is not Integer", str(context.exception))
        with self.assertRaises(ValueError) as context:
            the_list.add(88.88)
        self.assertEqual("Element is not Integer", str(context.exception))
        with self.assertRaises(ValueError) as context:
            the_list.add([88])
        self.assertEqual("Element is not Integer", str(context.exception))
        with self.assertRaises(ValueError) as context:
            the_list.add(None)
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_remove_index__with_valid_entry__expect_entry_not_in_list_anymore(self):
        the_list = IntegerList(1, 2, 3, 88, 4)
        expected = [1, 2, 3, 4]
        removed = the_list.remove_index(3)
        self.assertEqual(88, removed)
        self.assertEqual(expected, the_list._IntegerList__data)

    def test_remove_index__with_invalid_entry__expect_index_error(self):
        the_list = IntegerList(1, 2, 3, 88, 4)
        with self.assertRaises(IndexError) as context:
            the_list.remove_index(5)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_get_meth__with_valid_entry__expect_correct_item(self):
        the_list = IntegerList(1, 2, 3, 88, 4)
        self.assertEqual(1, the_list.get(0))
        self.assertEqual(88, the_list.get(3))

    def test_get_meth__with_invalid_entry__expect_index_error(self):
        the_list = IntegerList(1, 2, 3, 88, 4)
        with self.assertRaises(IndexError) as context:
            the_list.get(5)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_insert_meth__with_valid_entry__expect_to_have_it_at_correct_location(self):
        the_list = IntegerList(1, 2, 3, 88, 4)
        the_list.insert(3, 1001)
        expected = [1, 2, 3, 1001, 88, 4]
        self.assertEqual(expected, the_list._IntegerList__data)

    def test_insert_meth__with_out_of_range_entry__expect_exception(self):
        the_list = IntegerList(1, 2, 3, 88, 4)
        with self.assertRaises(IndexError) as context:
            the_list.insert(5, 1001)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_insert_meth__with_non_integer_entry__expect_exception(self):
        the_list = IntegerList(1, 2, 3, 88, 4)
        with self.assertRaises(ValueError) as context:
            the_list.insert(2, "УЙ")
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_get_biggest__perform_max__expect_max(self):
        the_list = IntegerList(1, 2, 3, 88, 4)
        expected = 88
        actual = max(the_list.get_data())
        self.assertEqual(expected, actual)

    def test_get_index_meth__with_existing_value__expect_index_of_value_in_list(self):
        the_list = IntegerList(1, 2, 3, 88, 4)
        expected = 3
        actual = the_list.get_index(88)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
