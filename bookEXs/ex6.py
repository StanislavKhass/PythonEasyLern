#страница 49
#тут задаем переменной значение 10
types_of_people = 10
#создаем строкувую переменнную и внутри добавляем через форматирование еще одну переменную x
x = f"Существует {types_of_people} типов людей."
#похоже на сокращенную переменную
binary = "Python"
#сокращенная переменная
do_not = "нет"
#вставляем переменную одну и другую в строку, и снова сохраняем в переменную y
y = f"Те, кто понимает {binary}, и те, кто - {do_not}."

#выводим из переменной x и y на экран
print(x)
print(y)
# Выводим строку а вней еще одна вложенность с x и y
print(f"Я сказал: {x}")
print(f"А еще я сказал: '{y}'")
#задаем переменную со значением False
hilarious = False
# создаем строку
joke_evaluation = "Разве это не смешно?! {}"
#способ форматирование текста через метод (Про это можно почитать) - Не указано форматирование, просто добавилось в конец.
print(joke_evaluation.format(hilarious))
#Задаем в переменные (w,e) строковые значения
w = "Это часть строки слева..."
e = "а это справа."
#склеиваем строки
print( w + e )

#https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html -тут можно почитать про форматирование
#через {} можно подствлять скобки и подставлять значения, можно использовать индексирование
print("Тестовая строка {0},{1},{2}".format('A','B','C'))
print("Тестовая строка2 {2},{1},{0}".format('A','B','C'))
#подставляем переменные
print("Текстовая {name_str} строка 3 , {name_str2}".format(name_str='тестовая',name_str2='будет что то другое'))
#собственно можно вставить без индекса
print("тестовая строка {}, тестовая строка без индекса {}".format('тест1','тест2'))

x = "_test1"
y = f"_test2 {x}"
z = f"_test3 {y}"
print(z)

print("Test {0} Test {1} Test {2}".format("T1","T2","T3"))
print("Test {1} Test {2} Test {0}".format("T1","T2","T3"))
print("Test {} Test {} Test {}".format("T1","T2","T3"))
print("Test {} Test {} Test {}".format(x,y,z))
print("Test {x} Test {y} Test {z}".format(x="standart1",y="standart2",z="standart3"))