#Страница 85
from sys import argv
from os.path import exists
#модуль можно импортировать весь как import и название модуля
#в модуле могут быть не только функции но и переменные к которым можно обращаться
#модуль можно переименовать как import mymodul as mx
#import sys #Можно посмотреть функции которын входят в модуль
#print(dir(sys))
# можно импортироват только часть модуля from modul import name_of_par_modul
from ex17_modul import open_file

script, from_file, to_file = argv

print(f"Копирование данных из файла {from_file} в файл {to_file} ")
print(f"Целевой файл существует == {exists(to_file)}")
print(f"Нажмите клавишу Enter для продолжения или CTRL+C для отмены.")
input()

#ОТкрываем файлы через with
#with open(from_file) as in_file:
#    indata = in_file.read()
#    with open(to_file, "w") as out_file:
#        out_file.write(indata)
#        print(f"Отлично, скопированно {len(indata)} байт.")

indata = open_file(from_file)
count_bytes_writes = open(to_file,"w").write(indata)
print(f"Отлично, скопированно {len(indata)} байт.")
