#страница 106
#Встретил дополнительно про модули

#Как пишем код
"""
1.проверяем написанный код
2. пишем комментарии на каждую строку для понимания
3. хорошей практикой считается читать код в слух снизу вверх

Читать в слух код
Читать код в обратном порядке
Оставлять комментариии , т.к через время начинаешь забывать что делает функция
"""


#Вывод информации на экран через функцию print Упражнение 1 \ Ex1
"""
print("текст"," за ней еще один текст", end="", sep="", flush=True, file=)
print(*args, end="", sep="", flush=, file=)
*args - входные аргументы для вывода на экран.
end="" - символ при окончание строки
sep="" - разделитель между аргументами
flush=False - немедленно выводит в поток вывода содержание буфера если стоит значение True
    import time
    print("Test string that not show up before timer finish", end="")
    time.sleep(5)
file=sys.stout - поток вывода.
    Возможные варианты куда можно записывать поток вывода.
    stdout = стандартный поток вывода
    stderr = стандартный поток ошибок
    file_steam = поток работы с файлом
"""



#Упражнение 2 - изучаем про комментарии
"""
#Комментарий помогает отключать части кода
#Два вида комментариев
#Первый вид комментариев через символ решетки
#Второй вид комментария через тройные ковычики
#Комментарии нужны для описания кода
#Комментарии нужны для отключения кода
"""

#Упражнение 3 - порядок арифмитических операций
"""
#Смотрите(Скобки)
#Эти(Экспоненты)
#Умельцы(Умножение)
#Делают(Деление)
#Скачущий(Сложение)
#Велосипед(Вычитание)
#Виды арифметиечских операций
()  - Смотрите
** возведение в степень - Эти
*(умножение) -  умельцы
/(деление) //(целое число от деления) % получение остатка от деления - делают
+(сложение) - Скачущий
-(вычитание) - велосипед
"""

#Упражнение 4 - именна переменных - Как нужно именовать имена переменных
"""
1.НЕ могут начинаться с цифры
2.должны быть латинскими буквами написанны
3.Можно использовать подчеркивание _ в начале и в середине.
4.Не можем занимать системные имена.

5.имена переменых должны быть читабельны
you_name_is =
you_place_live =
you_date_move =

6. Если мы говорим о числовых переменных то они могут быть:
натуральные числа - подсчет чего то конктретного 1.2.3
вещественные числа - число с плавающей точкой- состоит из (знака , экспоненты , мантиса)
"""

#Упражнение 5 - Вывод форматирование через f"Текст {переменная}"
#https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings
"""
0.Formatted string literals / f- string let you include the value of Python expressions inside a strings
by prefixing the string with f of F and writing expressions as {expressions}

print(f"Testing string :{expressions}")
print(""" New way: {expressions1}
to {expressions2} format text""")

1.The following example rounds pi to three places after the demical
print(f'The value of  pi is approximately {math.pi:.3f}')

2.a minimum number of characters wide ":" - this useful for making columns line up
print(f'{name:10} ==> {phone:10d}')


3.other modifires:  '!a' - applies ascii() , '!s' - applies str() , '!r' - applies repr()
# print(f'My hovercraft is full of {animals!r}.')

4. for debugging
print(f'Debugging {bugs=} {count=} {area=}')
"""

#Упражнение 6 - Продолжение форматирование строки
"""
#Можно использовать как рекурсию
x = "_test1"
y = f"_test2 {x}"
z = f"_test3 {y}"
print(z)
#Результат: test 3 test2 test1
строе форматирование строк

Basic usage str.format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
#but we can use numbers, index
print('{0} and {1}'.format('spam', 'eggs'))
Also we can use name of arguments
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
Or it can be mixed
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
Or use from dictionary
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
"""

#Упражнение 7 - работа со строками
#Дополнительное форматирование
"""
Арифметические действия со строками
Строки можно складывать через сложение: "T"+"E"+"S"T"="TEST
Строку можно умножать на число: "TEST"*2 = "TESTTEST"
#Format string syntax
Format string contain "replacement fileds" surraunded by curly braces { }
For using curly braces in literal = use {{ or }}
Grammer
replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
conversion        ::=  "r" | "s" | "a"
format_spec     ::=  [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["." precision][type]



"""
#Упражнение 8 - практика с работой "{} {} {}".format
"""
интересный пример рекурсивности
text = "{} {} {} {}"
text.format(text,text,text) Результат: {} {} {} {} {} {} {} {} {} {} {} {}
Если задать значения в переменной то придется обьвлять все переменные и подставлять названия переменных в {}
Будет ошибка, В формате переменная должна быть обьявленна.
"{} {} {}".format(x=1,y,z)
Правильный вариант
"{x} {y} {z}".format(x=1,y=2,z=3)
"""

#Упражнение 9-10 - управляющие символы.
"""
#Управляющие последовательности
\'	Single Quote
\\	Backslash
\n	New Line
\r	Carriage Return
\t	Tab
\b	Backspace
\f	Form Feed
\ooo	Octal value
\xhh	Hex value
"""

#Упражнение 11 - Работа с вводом текста
"""
result = input(подсказка) - для ввода с клавиатуры
#возразает строковую переменную
"""

#Упражнение 12 - Работа с модулями
"""
#Модули в python
#Получение документации о модуле python -m pydoc <имя модуля>.
# Туже документацию можно найти на сайте python
time - для работы со временем. Например задерка выполнения кода.
sys - для работы с потоком ввода\вывода
os - работа с операционной системой  - работа с путями файлов
#Получить список все функций внутри модуля dir()

#https://www.w3schools.com/python/python_modules.asp
Modules in Python: Creating moduls
a File containing a set of functions you want to include to you application
1. Create a modul with function - save the code in file with file extension .py
2. Use a modul - we can use import statment: import modul_name
3. Call function from modul: module_name.function_name
4. Module can contain functions, arrays , dictionaries, objects module_name.object

Naming a module_name
1. Module can be any name, but have .py file extension
2. Re-name module , using alias as : import name_module as new_name
3. now we can use new_name.object

Build-in modules: time, sys, os
1. Use dir(name_module) to show all variables in modules
2. The dir() function can use on all modules, also the ones you create youself

Import from module
1. Import parts from module , using keywords from module_name import object_name
2. Acess object_name, dont use modele name
"""

#Упражнение 13-14 Получение аргументов из командной строки
#Была практикой на то что узнали
"""
from sys import argv
script , arg1 = argv
"""

#Упражнение 15 - Работа с файлами - основной принцип работы с файлами
"""
file = open(name_of_file) \ return object on file
variable_of_text = file.read() \ save text frome file , using read() function
file.close() \ close file after work
"""

#Упражнение 16 - режимы открытия файлов
"""
file = open(name_of_file, "mode")
'r' - open for reading (default)
'w' -open for writing, truncating the file first
'x' - open for exclusive creation, failing if the file already exists
'a' - open for writing, appending to the end of file if it exists
'b' - binary mode
't' - text mode (default)
'+' - open for updating (reading and writing)

<fileObject>.open()
<fileObject>.read() читаем файл и сохраняем в переменную - можно считать определенное количество байт
<fileObject>.close() закрываем файл
<fileObject>.readline() считываем только строку
<fileObject>.truncate() очищает файл
<fileObject>.write() записываем  строку в файл
<fileObject>.seek(0) перемещаем каретку в начало
"""

#Упражнение 17 модули
