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
print(f'My hovercraft is full of {animals!r}.')

4. for debugging
print(f'Debugging {bugs=} {count=} {area=}')
"""

#Упражнение 6 - Продолжение форматирование строки
"""
x = "_test1"
y = f"_test2 {x}"
z = f"_test3 {y}"
print(z)
#Результат: test 3 test2 test1
строе форматирование строк
"Test {1} Test {2} Test {3}".format("T1","T2","T3")
"Test {2} Test {3} Test {1}".format("T1","T2","T3")
"Test {} Test {} Test {}".format("T1","T2","T3")
"Test {} Test {} Test {}".format(x,y,z)
"Test {} Test {} Test {}".format(x="standart1",y="standart2",z="standart3")

# Первый вариант обьявить через print(arg1,"Text", arg2, "Text", arg3)
# Второй вариант обьявить через f"{arg1} , Text , {arg2}, Text {arg3}"
# Третий вариант обьявить через "{arg1} , Text , {arg2}, Text {arg3}".format(arg1="значение",arg2="значение",arg3="значение")
"""

#Упражнение 7 - работа со строками
"""
Строки можно складывать через сложение: "T"+"E"+"S"T"="TEST
Строку можно умножать на число: "TEST"*2 = "TESTTEST"


"""
#Упражнение 8 - практика с работой "{} {} {}".format
"""
интересный пример рекурсивности
text = "{} {} {} {}"
text.format(text,text,text) Результат: {} {} {} {} {} {} {} {} {} {} {} {}
Если задать значения в переменной то придется обьвлять все переменные и подставлять названия переменных в {}
Будет ошибка
"{} {} {}".format(x=1,y,z)
Правильный вариант
"{x} {y} {z}".format(x=1,y=2,z=3)
либо второй вариант выносить пристваивание переменых за функцию и тогда можно использовать будет индексы
x=1
y=2
z=3
"{} {} {}".format(x,y,z)
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
