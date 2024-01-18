city = "6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$"
change_format_city = city.strip('6..58 74$:?$')
cities = change_format_city.lower().title().split()
for cities_result in cities:
    if cities_result[-1] == 'а':
        cities_result = f"{cities_result.strip('а')}у"
    print(f"Я\U00002764 {cities_result} ")
