import unittest

from testing_lab.cat import Cat


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Tochka")

    def test_init(self):
        expected_fed = self.cat.fed
        expected_sleepy = self.cat.sleepy
        expected_size = self.cat.size

        self.assertFalse(expected_sleepy, False)
        self.assertFalse(expected_fed, False)
        self.assertFalse(expected_size, 0)
        self.assertEqual(self.cat.name, "Tochka")

    def test_eat(self):
        expected_fed = True
        expected_sleepy = True
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertEqual(expected_fed, self.cat.fed)
        self.assertEqual(expected_sleepy, self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_eat_exception(self):
        self.cat.fed = True
        expected = 'Already fed.'

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual(expected, str(ex.exception))

    def test_sleep_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertEqual(self.cat.sleepy, False)


if __name__ == "__main__":
    unittest.main()