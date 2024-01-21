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