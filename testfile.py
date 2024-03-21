import pytest
import homework_12_testing

def test_check_value():
    time_in_seconds = 10
    speed_in_mps = 3
    car_weight_in_kg = 1000

    expected = 'Транспортний засіб вагою 1000 кг рухався 10 секунд зі швидкістю 3 м/сек, і подолав відстань 30 метрів.'
    actual_result = homework_12_testing.cal_distance(time_seconds=time_in_seconds, speed_mps=speed_in_mps, weight_kg=car_weight_in_kg)
    assert expected == actual_result

def test_negative_value():
    time_in_seconds = 10
    speed_in_mps = -5
    car_weight_in_kg = 1000
    with pytest.raises(ValueError):
        homework_12_testing.cal_distance(time_seconds=time_in_seconds, speed_mps=speed_in_mps, weight_kg=car_weight_in_kg)

def test_incorrect_value():
    time_in_seconds = 10
    speed_in_mps = 'tfyf'
    car_weight_in_kg = 1000
    with pytest.raises(TypeError):
        homework_12_testing.cal_distance(time_seconds=time_in_seconds, speed_mps=speed_in_mps, weight_kg=car_weight_in_kg)
