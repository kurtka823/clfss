import time


def measure_time(func, *args, **kwargs):
    start = time.time()          
    result = func(*args, **kwargs)   # запуск функции
    end = time.time()     
    
    work_time = end - start          # считаем время выполнения
    return result, work_time 


# Пример функции для теста
def slow_function():
    time.sleep(1)
    return "Готово"


# Тест
def test_measure_time():
    result, t = measure_time(slow_function)
    
    assert result == "Готово"   # проверяем результат
    assert t >= 1     
    
    print("Тест пройден!")


# Запуск программы
if __name__ == "__main__":
    test_measure_time()