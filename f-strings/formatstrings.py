#use documentatin from official web site
#https://docs.python.org/3/library/string.html#formatstrings
#Нужно разобраться как делать форматирование
"""
Выведет по центру слово TEST и экранирует его #
string = "TEST"
print(f"{string:#^100}")
#result for print
################################################TEST################################################
"""
"""
#Данная история зависит в каком месте мы оставляем показывать плавающую точку (z)
string = -0.0001
print(f"{string:#^z50.3f}")
######################0.000#######################
#Покажет +
string = -0.0001
print(f"{string:#^z50.4f}")
#Покажет -в ответе
######################-0.0001#######################
"""
"""
#Можно выводить в разных форматах  через указание #
string = 10
print(f"{string:#^#10o}")

string = 10
print(f"{string:_^#10x}")

string = 10
print(f"{string:_^#10b}")

string = 10
print(f"{string:_^#10.2f}")
"""

"""
#Использование разделителя
string = 1000000
print(f"{string:#^10,}")

string = 1000000
print(f"{string:#^10_}")

string = 1000000
print(f"{string:#^#10_b}")
"""

"""
# Когда явное выравнивание не задано, заполяняем нулями
string = 10010001
print(f"{string:#050_b}")
"""
