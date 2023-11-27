from unittest import TestCase, main

from testing_lab.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car_manager = Car("Dacia", "Duster", 7, 55)

    def test_init(self):
        self.assertEqual(self.car_manager.make, "Dacia")
        self.assertEqual(self.car_manager.model, "Duster")
        self.assertEqual(self.car_manager.fuel_consumption, 7)
        self.assertEqual(self.car_manager.fuel_capacity, 55)
        self.assertEqual(self.car_manager.fuel_amount, 0)

    def test_make_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager = Car("", "Duster", 7, 55)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager = Car("Dacia", "", 7, 55)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager = Car("Dacia", "Duster", 0, 55)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager = Car("Dacia", "Duster", 7, -1)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_raise_exception_negative_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_fuel_amount(self):
        self.car_manager.refuel(90)
        self.assertEqual(self.car_manager.fuel_capacity, self.car_manager.fuel_amount)

    def test_drive(self):
        self.car_manager.refuel(90)
        self.car_manager.drive(10)

        self.assertEqual(self.car_manager.fuel_amount, 54.3)

    def test_drive_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.drive(10)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()


