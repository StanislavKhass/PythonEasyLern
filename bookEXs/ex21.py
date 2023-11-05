#Страница 102
def add(a, b):
    print(f"Сложение {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Вычитание {a} - {b}")
    return a - b

def myltiply(a, b):
    print(f"Умножение {a} * {b}")
    return a * b

def devide(a, b):
    print(f"Деление {a} / {b}")
    return a / b


print("Давайте выполним несколько вычислений с помощью функций")

age = add(30,5)
height = subtract(190,4)
weight =  myltiply(35, 2)
iq = devide(250 , 2)

print(f"Возрастс: {age} ,Рость {height}, Вес: {weight}, IQ {iq}")

print("Это головоломка")
what = add( age , subtract(height , myltiply(weight, devide(iq,2))))
#            (35 +       (186-     (70  *   (125\2)=62.5)=4375)=-4189)=-4154
#            (A + (B - (C * (D/2))))
formula = (age + (height - (weight * (iq/2))))
print(what)
print(formula)
# a = age , B = height , C = weight , iq = D
#обратная формула
#formula2 = (B * (D / C) + (A - 5))
formula_in_func = add(myltiply(height, devide(iq , weight)),subtract(age,5))
print(formula_in_func)
