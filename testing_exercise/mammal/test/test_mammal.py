from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("lion", "wild", "ROAR")

    def test_init(self):
        self.assertEqual(self.mammal.name, "lion")
        self.assertEqual(self.mammal.type, "wild")
        self.assertEqual(self.mammal.sound, "ROAR")
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_make_sound(self):
        expected = f"{self.mammal.name} makes {self.mammal.sound}"
        result = self.mammal.make_sound()

        self.assertEqual(expected, result)

    def test_info(self):
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        result = self.mammal.info()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()