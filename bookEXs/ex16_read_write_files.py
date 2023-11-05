#страница 83
#https://docs.python.org/3/library/functions.html#open
"""some info from web site
'r'

open for reading (default)

'w'

open for writing, truncating the file first

'x'

open for exclusive creation, failing if the file already exists

'a'

open for writing, appending to the end of file if it exists

'b'

binary mode

't'

text mode (default)

'+'

open for updating (reading and writing)
"""
#импортируем из модуля sys функуию argv которая возращает список параметром с которыми запустили программа
from sys import argv

#делаем паспаковку параметров по номерам 0 - имя программы, 1 - второй переданный параметр
script, filename = argv

#выводим сообщения
print(f"Я собираюсь стереть файл {filename}.")
print("Если не хотите стирать его, нажмите сочетание клавиш CTRL+C (^C).")
print("Если хотите стереть файл, нажмите клавишу Enter.")

#просит сделать выбор пользователю
input("?")

#открываем файл
print("Открытие файла...")
with open(filename, "w") as target:
    #очистка файла, при открытие через w этот кусок кода не нужен
    #print("Очистка файла. До свидания!")
    #target.truncate()

    print("Теперь я запрашиваю у вас 3 строки.")
    line1 = input("Строка 1: ")
    line2 = input("Строка 2: ")
    line3 = input("Строка 3: ")

    print("Это я запишу в файл.")

    target.write(line1+"\n"+line2+"\n"+line3+"\n")

#print("И наконец, я закрою файл.")
#target.close()

"""Some to remember
<fileObject>.close() закрываем файл
<fileObject>.read() читаем файл и сохраняем в переменную - можно считать определенное количество байт
<fileObject>.readline() считываем только строку
<fileObject>.truncate() очищает файл
<fileObject>.write() записываем  строку в файл
<fileObject>.seek(0) перемещаем каретку в начало
"""
