#Упражнение 12 - страница 65

"""
#Получается мы выполняем задание из прошлого успраженеия усовершествуя функцию
age = input("Сколько тебе лет?")
height = input("Каков твой рост?")
weight = input("Сколько ты весишь?")
print(f"Итак, тебе {age} лет, в тебе {height} см роста и {weight} кг веса.")

"""

import sys
#пользуемся документацией python -m pydoc input
#print(sys.getprofile())

#системное пространство
# import os - работа с операционной системой
#import sys -
#не очень хорошая возможность использовать input в принте
#print("Сколько тебе лет", input("try"))


#Sys модуль = симтемный модуль с параметрами и фунуциями
#этот модуль дает доступ до некторых переменных испольщуемым или подерживаемым
#интерпритатором

#print(sys.path)

#os - модуль позволянт использовать функции которые зависят от операционной системы
# open - прочитать или записать файл, если хочется маниаулировать путями = path
# работа со строками в командной строке = fileinput
#создание временныйх файлов tmpfile
#высокоуровневая обработка файлов Shutil
