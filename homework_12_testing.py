# homework
# написати функцію, котра приймає час (в секундах), швидкість (метрів за секунду) та вагу автомобіля (кг). за допомогою * забезпечити, щоб всі аргументи можна було передати як keywords аргументи (типу speed=3)
#
# якщо хоч один із аргументів буде менше 0 - рейзимо помилку ValueError, текст помилки - на ваш вибір
#
# функція повертає стрічку, наступного змісту: "Транспортний засіб вагою 1000 кг рухався 10 секунд зі швидкістю 3м/сек, і подолав відстань 30 метрів"
#
# написати тести до даної функції
#
def cal_distance(*, time_seconds, speed_mps, weight_kg):

    if time_seconds < 0 or speed_mps < 0 or weight_kg < 0:
        raise ValueError("All arguments must not be negative.")
    distance_meters = speed_mps * time_seconds

    return f"Транспортний засіб вагою {weight_kg} кг рухався {time_seconds} секунд зі швидкістю {speed_mps} м/сек, і подолав відстань {distance_meters} метрів."


time_in_seconds = 10
speed_in_mps = 3
car_weight_in_kg = 1000

result = cal_distance(time_seconds=time_in_seconds, speed_mps=speed_in_mps, weight_kg=car_weight_in_kg)
print(result)
