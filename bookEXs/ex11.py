#Упражнение 11, ввод данных
"""
#метод который вызывает печать на экран, вместо перевода строки добавляем пробел
print("Сколько тебе лет?", end=' ')
#переменная лет
age = input()
#метод который вызывает печать на экран, вместо перевода строки добавляем пробел
print("Каков твой рост?", end=' ')
#переменная высота
height = input()
#метод который вызывает печать на экран, вместо перевода строки добавляем пробел
print("Сколько ты весишь?", end=' ')
#переменная вес
weight = input()
#Форматированно выводим на экран эти значения
print(f"Итак, тебе {age} лет, в тебе {height} см роста и {weight} кг веса.")
"""

#1. расставить комментарии
#2. проверить код - проверяем то что ввели , лучше не ждать пока компелятор тебе это скажет (мое мнение)
#3. ошибок не было
#4. Ломаем код . убрали знак форматирования.
"""
Вторая часть задания
функция для ввода данных с клавиатуры
input(promt)
promt - подсказка
Возращает строковую значение, даже если ввели цифры
Записывается без управляющей последовательности \n
"""

#1. задать другие вопросы пользователю
#2. использовать по другому команду input
"""

print(f"Вас зовут {you_name_is}, вы планируете попасть в{you_place_live}, в году {2023+you_date_move}")

"""
"""
#Изначально запоминается как строка
txt = input("Введите ваше имя для сохранения ее в переменуую:")
#Вывод значения
print(f"Это то, что вы только что ввели {txt}")

"""
#Можно форматировать под число сразу через функцию int() float(). Но если пользователь ввел не правильные данные появится ошибка и выполнение скрипта остановится.
#Итого есть отдельный блок https://docs.python.org/3/tutorial/errors.html работы с ошибками. - пока не входит в рамки обучения python
"""
import sys
txt = input("Тестовый ввод текста:")
#Вывод значения
sys.stderr.write(txt)
#Обработчик ошибки если пользователь вел строку а не int()
try:
    #print(txt)
    sys.stderr.flush()
except "test:":
    print("Выловили ответ из потока вывода ошибок")
"""
