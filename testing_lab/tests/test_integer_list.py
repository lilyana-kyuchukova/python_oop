import unittest

from testing_lab.extended_list import IntegerList


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1, 2, 3, 4, False, "30", 3.4)

    def test_init_and_get_data(self):
        self.assertEqual([1, 2, 3, 4], self.integer_list.get_data())

    def test_add_element(self):
        actual = self.integer_list.get_data()
        expected = self.integer_list.get_data() + [2]
        self.integer_list.add(2)
        self.assertEqual(actual, expected)

    def test_add_element_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add("2")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_index(self):
        actual = self.integer_list.get_data()
        expected = [2, 3, 4]
        deleted = 1
        actual_deleted = self.integer_list.remove_index(0)

        self.assertEqual(actual, expected)
        self.assertEqual(deleted, actual_deleted)

    def test_remove_index_raise_exception(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(20)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get(self):
        expected = 2
        actual = self.integer_list.get_data()[1]

        self.integer_list.get(1)

        self.assertEqual(expected, actual)

    def test_get_raise_exception(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert(self):
        expected = [0, 1, 2, 3, 4]
        self.integer_list.insert(len(self.integer_list.get_data()) - 10, 0)

        self.assertEqual(self.integer_list.get_data(), expected)

    def test_inset_raise_exception_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(len(self.integer_list.get_data()) + 1, 1)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_raise_exception_invalid_type(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, "1")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_biggest(self):
        expected = max(self.integer_list.get_data())
        actual = self.integer_list.get_biggest()

        self.assertEqual(expected, actual)

    def test_get_index(self):
        expected = 0
        actual = self.integer_list.get_index(1)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()