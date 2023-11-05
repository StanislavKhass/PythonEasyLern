#страница 19
#создаем функцию с двумя входными аргументами cheese_count, boxes_of_crackers
#функция выводит на экран значения этих двух аргументов
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"У нас есть {cheese_count} сырков!")
    print(f"У нас есть {boxes_of_crackers} пачек чипсов!")
    print(f"этого достаточно для вечеринки!")
    print(f"Погнали!\n")

def cars(amount_of_cars,cars_broken,cars_in_rent,company_name="Amiro"):
    print(f"Название компании {company_name}")
    print(f"Всего машин в компании {amount_of_cars}")
    print(f"Машин сломанно {cars_broken}")
    print(f"Машин находится в аренде {cars_in_rent}")
    count_free_cars = amount_of_cars - cars_broken - cars_in_rent
    print(f"Доступных машин {count_free_cars}")
    print("Конец отчета.")
    return count_free_cars

amount_of_cars = 100
cars_broken = 10
cars_in_rent = 5

cars(10,2,2)
cars(10+10,5+1,2+1)
cars(amount_of_cars, 10 , 10)
cars(amount_of_cars, cars_broken  , 10)
cars(amount_of_cars, cars_broken  , cars_in_rent)
cars(amount_of_cars + 500 , cars_broken  , cars_in_rent)
cars(amount_of_cars + 500 , cars_broken  +20, cars_in_rent)
cars(amount_of_cars + 500 , cars_broken  +20, cars_in_rent + 100)
cars(600,10,200,"New trance line")
cars(600,10,200,"New trance line"+"01")
"""
#Передаем 20 и 30 внутри функции
print("Вы можете непосредственно передать числа функции:")
cheese_and_crackers(20,30)

#сначала обьявляем переменные перед функцие, потом передаем в функцию
print("Или, мы можем использовать переменные из нашего сценария")
amount_of_cheese = 10
amount_of_crakers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crakers)

#вычисляем аргументы в функции , передаем как =, как присваиваем переменную
print("Мы даже можем выполнять вычисления внутри функции:")
cheese_and_crackers(10 + 20, 5 + 6)

#две переменные были обьявленны ранее, подставляем переменную с сложением
print("И обьединять переменные с вычислениями:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crakers + 1000)
"""
