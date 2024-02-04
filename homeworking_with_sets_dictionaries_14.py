# homework homeworking_with_sets_dictionaries_14
# написати програму, яка просить в користувача ввести через пробіл міста, в яких він був за минулі 10 років
# потім окремо запросити у користувача міста, куди він хоче поїхати внаступні 10 років
# вивести на екран повідомлення з текстом про те, що користувачу, мабуть, дуже сподобалося в містах, які він повторив в двох циклах вводу,
# якщо повтору не було - вивести повідомлення, що користувач відкритий до чогось нового
# врахувати випадки, що користувач нічого не вводить не потрібно, в даному випадку вам явно зазначено, що ці перевірки не потрібні.
# не потрібно перевіряти введення цифр
# ми виходим із того, що користувач введе щось на зразок "Київ Тернопіль париЖ акапулько"
# В той же час врахуйте, що користувач може вводити дані в різних регістрах
# використати сети

past_cities = input('Enter the cities you have been to in the past 10 years separated by a space ->')
# Kyiv Lviv Odesa London cardiff bath Vena Berlin Warsaw Oslo
# print(past_cities)
cities_list_past = past_cities.title().split()
cities_set_past = set(cities_list_past)
# print(cities_set_past)

future_cities = input('Enter through the space of the city where you want to go in the next 10 years ->')
# Kyiv Lviv London Paris madrid rome barcelona dublin valencia krakiv
cities_list_future = future_cities.title().split()
cities_set_future = set(cities_list_future)
# print(cities_set_future)
common_ = cities_set_past & cities_set_future
print(common_)
if not cities_set_past | cities_set_future:
    print('Nothing entered.')
    exit()

if not common_:
    print('The user is open to something new.')
else:
    print(f'The user must have really liked the cities: {', '.join(common_)}.')
