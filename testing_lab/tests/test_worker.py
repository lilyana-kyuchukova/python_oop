import unittest

from testing_lab.worker import Worker


class WorkerTests(unittest.TestCase):

    def setUp(self):
        self.worker = Worker("Mario", 1000, 4)

    def test_init(self):
        self.assertEqual(self.worker.name, "Mario")
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 4)
        self.assertEqual(self.worker.money, 0)

    def test_rest(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()
        self.assertEqual(self.worker.energy, expected_energy)

    def test_work_enough_energy(self):
        expected_energy = self.worker.energy - 1
        expected_money = self.worker.salary

        self.worker.work()
        self.assertEqual(self.worker.energy, expected_energy)
        self.assertEqual(self.worker.money, expected_money)

    def test_work_low_energy(self):
        self.worker.energy = 0  # arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work()  # act

        self.assertEqual('Not enough energy.', str(ex.exception))  # assert

    def test_get_info(self):
        actual = self.worker.get_info()
        expected = f"{self.worker.name} has saved {self.worker.money} money."

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
