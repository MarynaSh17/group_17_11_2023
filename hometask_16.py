# hometask_16
# створити абстрактний клас транспортного засобу
#
# створити два класи - авто та мотоцикл - та унаслідувати їх від транспортного засобу
#
# спільними атрибутами для авто та мотоцикла є марка, обєм баку, залишок пального в баку, швидкість, пробіг
#
# унікальними полями для авто є кількість пасажирів, ознака наявності подушок безпеки (тру/фолс)
#
# унікальними полями для мотоцикла є опція наявності люльки (тру/фолс)
#
# спільними методами є
#
# метод заправки (збільшує обсяг пального в баку на задану величину , проте не більше максимального обєму баку);
# метод переливу пального від себе іншому транспортному засобу (з баку в бак, обсяг теж задається як аргумент) - умова - ми не можемо віддати більше, ніж у нас є, не може залишок бути відємним, і ми не можемо перелити більше, ніж це дозволяє ВІЛЬНИЙ залишок пустого місця в баку приймаючої сторони
# абстрактиним методом можете зробити __str__
from abc import ABC, abstractmethod

class Vehicle(ABC):
        def __init__(self, brand, tank_capacity, fuel_remaining, speed, mileage):
            self.brand = brand
            self.tank_capacity = tank_capacity
            self.fuel_remaining = fuel_remaining
            self.speed = speed
            self.mileage = mileage

        @abstractmethod
        def refuel(self, amount):
            pass

        @abstractmethod
        def transfer_fuel(self, other_vehicle, amount):
            pass

        def __str__(self):
            return f"{self.brand} ({self.__class__.__name__}): Fuel remaining: {self.fuel_remaining} liters"

class Car(Vehicle):
        def __init__(self, brand, tank_capacity, fuel_remaining, speed, mileage, passenger_count, airbags):
            super().__init__(brand, tank_capacity, fuel_remaining, speed, mileage)
            self.passenger_count = passenger_count
            self.airbags = airbags

        def refuel(self, amount):
            self.fuel_remaining = min(self.fuel_remaining + amount, self.tank_capacity)

        def transfer_fuel(self, other_vehicle, amount):
            available_space = other_vehicle.tank_capacity - other_vehicle.fuel_remaining
            transfer_amount = min(amount, available_space)
            self.fuel_remaining -= transfer_amount
            other_vehicle.fuel_remaining += transfer_amount

class Motorcycle(Vehicle):
    def __init__(self, brand, tank_capacity, fuel_remaining, speed, mileage, sidecar):
            super().__init__(brand, tank_capacity, fuel_remaining, speed, mileage)
            self.sidecar = sidecar

    def refuel(self, amount):
        self.fuel_remaining = min(self.fuel_remaining + amount, self.tank_capacity)

    def transfer_fuel(self, other_vehicle, amount):
        available_space = other_vehicle.tank_capacity - other_vehicle.fuel_remaining
        transfer_amount = min(amount, available_space)
        self.fuel_remaining -= transfer_amount
        other_vehicle.fuel_remaining += transfer_amount

    # Example usage:
car1 = Car("Toyota", 50, 30, 120, 150000, 4, True)
motorcycle1 = Motorcycle("Harley-Davidson", 20, 15, 180, 50000, False)

print(car1)
print(motorcycle1)
toyota_camry = Car("Toyota Camry", 60, 40, 120, 150000, 4, True)
print(f"Initial fuel level: {toyota_camry.fuel_remaining} liters")
toyota_camry.refuel(20)  # Refuel by 20 liters
print(f"Fuel level after refueling: {toyota_camry.fuel_remaining} liters")