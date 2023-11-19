import mymodule as mm

print("Here we are show text from module")
mm.testing_module("Running test module")


print("get acces to module objects")
print(dir(mm))

#Перечисляем красиво список обьектов в модуле.
for list in dir(mm):
    print(list)

print("Тип обьякта из модуля:",type(mm.person1) )
