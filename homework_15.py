# homework_15
# написати клас автомобіль
# має мати атрибути
# рік випуску (за замовчуванням 2020, в ініт ПЕРЕДАЄТЬСЯ)
# виробник
# марка
# пробіг (за замовчуванням 0, в ініт не передається)
# витрата палива (флоатове значення)
# перевизначити метод __str__ (значення на ваш вибір)
# створити метод для подачі сигналу
# створити кілька екземплярів автомобілів

year = 2020
class Car:
    def __init__(self, manufacturer, model, year: int = 2020, mileage=0, fuel_consumption: float = 0.0):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_consumption = fuel_consumption
    def __str__(self) -> str:
        return f'Я купила машину: {self.year} {self.manufacturer} {self.model}'

    def honk(self):
        return f'Beep! {self.manufacturer} {self.model}'


car_1 = Car(manufacturer='Volkswagen', model='Golf', mileage=70000, fuel_consumption=8.5)
car_2 = Car(manufacturer='Seat', model='Leon', fuel_consumption=6.2)
car_3 = Car(manufacturer='Ford', model='Focus', mileage=12000)

print(car_2)
print(car_1.honk())
