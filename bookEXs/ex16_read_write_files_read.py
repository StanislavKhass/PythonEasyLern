#страница 83
#импортируем из модуля sys функуию argv которая возращает список параметром с которыми запустили программа
from sys import argv

#делаем паспаковку параметров по номерам 0 - имя программы, 1 - второй переданный параметр
script, filename = argv

#выводим сообщения
print(f"Будем считывать файл {filename}.")
print("Для выхода из программы нажмите CTRL+C (^C).")
print("Для продолжения чтения нажмите Enter.")

#просит сделать выбор пользователю
input("?")

#открываем файл
print("Открытие файла...")
target = open(filename, "r")

#очистка файла
print("Очистка файла. До свидания!")
txt = target.read()

print(f"Данные которые хранятся в файле{script}: \n{txt}")

print("И наконец, я закрою файл.")
target.close()
