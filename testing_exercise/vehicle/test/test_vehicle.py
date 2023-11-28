from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(10.0, 100)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 10)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, 100)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(2000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive(self):
        expected = self.vehicle.fuel - self.vehicle.fuel_consumption * 5
        self.vehicle.drive(5)
        self.assertEqual(self.vehicle.fuel, expected)

    def test_refuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(self.vehicle.capacity + 10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel(self):
        expected = self.vehicle.fuel + 2
        self.vehicle.capacity = 20
        self.vehicle.refuel(2)
        self.assertEqual(expected, self.vehicle.fuel)

    def test_str(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        result = str(self.vehicle)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()