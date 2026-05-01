class MyIterable:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        # Метод __iter__ делает объект итерируемым
        # создаём генератор
        for i in range(self.n):
            # yield возвращает значение
            yield i


# Создаём объект
obj = MyIterable(5)

# Перебираем объект в цикле
for x in obj:
    print(x)  # Выводим значения от 0 до 4