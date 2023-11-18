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

"""
#Научная нотауия для цифр 5. экспонента = сколько цщнаков после точки
string = 5179
print(f"{string:*^50_.3G}")
#5.18E+03
"""

"""
#Индексирование данных
print("{0},{1},{2}".format('a','b','c'))
print("{},{},{}".format('a','b','c'))
print("{2},{1},{0}".format('a','b','c'))
print("{2},{1},{0}".format(*'abc')) # распаковака
print("{0},{1},{0}".format(*'abc'))
"""
"""
#обращение через переменные
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
coord = ['test1', 'test2']
print('Coordinates: {0}, {0}'.format(*coord))
coord = {'param1':'test1','param2': 'test2'}
print('Coordinates: {param1}, {param2}'.format(**coord))
"""

"""
#доступ через атрибуты
c = 3-5j
print(('The complex number {0} is formed from the real part {0.real} '
 'and the imaginary part {0.imag}.').format(c))


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

print(str(Point(4, 2)))
"""
"""
#доступ через индекс аргумента
coord = [3,4]
print("X: {0[0]};  Y: {0[1]}".format(coord))
"""
