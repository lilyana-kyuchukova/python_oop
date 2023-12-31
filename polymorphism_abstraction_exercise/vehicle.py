import abc


class Vehicle(abc.ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abc.abstractmethod
    def drive(self, distance: float):
        ...

    @abc.abstractmethod
    def refuel(self, fuel: float):
        ...


class Car(Vehicle):
    AC_ON = 0.9

    def drive(self, distance):
        consumption = (self.fuel_consumption + Car.AC_ON) * distance
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_ON = 1.6

    def drive(self, distance):
        consumption = (self.fuel_consumption + Truck.AC_ON) * distance
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)