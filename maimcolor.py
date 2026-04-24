import colorama

# запуск библиотеки
colorama.init()

# примеры
print(colorama.Fore.RED + "Красный текст")
print(colorama.Fore.GREEN + "Зелёный текст")
print(colorama.Style.BRIGHT + "Яркий текст")
print(colorama.Style.RESET_ALL + "Обычный текст")

# интроспекция 
print(dir(colorama))
help(colorama)

# Мне понравилась библиотека colorama, потому что с её 
# помощью можно легко делать цветнойтекст в консоли. Это удобно и делает вывод более понятным.
