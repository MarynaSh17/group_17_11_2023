# в функціях нижче використайте lambda функції:
# створити список з довільними даними, застосувати функцію map для перетворення всіх елементів списку на стрічковий тип даних
# створити список з довільними типами даних, застосувати функцію filter для отримання зі списку тільки цілих чисел

my_list = ['Acura', 'alfa Romeo', 'aston Martin', 'audi', 'bmw', 'chevrolet', 'Chrysler', 'Dodge',
           'Ford', 'GMC', 'Honda', 'Hyundai', 'Jeep', 'Kia', 'Lexus', 'Mazda',
           'Mercedes-Benz', 'Mini', 'Nissan', 'Porsche', 'Subaru']
mapped_my_list = list(map(lambda i: str(i).upper(), my_list))
print(mapped_my_list)

numbers = [10, 15, 21, 33, 42, 55, 100, 32, 45, 11, 53, 14, 50, 76, 'gjdge']
filtered_numbers = list(filter(lambda j: isinstance(j, int), numbers))
filtered_even_numbers = list(filter(lambda x: x % 2 == 0, filtered_numbers))

print(list(filtered_even_numbers))
