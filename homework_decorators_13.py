# homework
# написати декоратор, який по імені функції створює текстовий файл (чи csv), в який записуються логи роботи задекорованої функції (функцій) - час, результат роботи
#
import time
from functools import wraps

def log_time_alt(path_to_logfile, interval):
    def log(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            start_time = time.time()
            fun_result = func(*args, **kwargs)
            end_time = time.time()
            passed_time = end_time - start_time

            with open(path_to_logfile, 'a') as log_file:
                log_file.write(f"Execution time: {passed_time:.2f} seconds\n")
                log_file.write(f"Your result: {fun_result}\n")

            return fun_result

        return wrapped

    return log

@log_time_alt('working_log.txt', 30)
def mult_function(a, b) -> int:
    return a * b
def power_function(a, b) -> int:
    return a ** b

result = mult_function(3, 2)
result_power = power_function(4,2)

print(f"Your result: {result}, power result: {result_power}")
