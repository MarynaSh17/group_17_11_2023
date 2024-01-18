city = "6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$"
change_format_city = city.strip('6..58 74$:?$')
cities = change_format_city.split()
print(cities)
result = ['київ', 'оДеса', 'Львів', 'житоМИР', 'уЖгОрОд', 'ХарКІВ', 'слАвУтИч']
for cities_result in result:
    lower_cities = cities_result.lower().capitalize()
    print(f"Я\U00002764_{lower_cities}_")
