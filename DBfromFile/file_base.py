import os

ADD_RECORD = 1
SHOW_RECORDS = 2
DELETE_RECORD = 3
EDIT_RECORD = 4
EXIT_NUMBER = 0

NAME_OF_DATABASE = "database.txt"
NAME_OF_BACKUP = "database.bkp"
RAW_FIRSTNAME_STUDENT = 1
RAW_LASTNAME_STUDENT = 2
RAW_DOCNUM_STUDENT = 3
RAW_STATUS_STUDENT = 4
RAW_LINE_TOTAL = 4

INFO_FIRSTNAME_STUDENT = "\053 Имя студента"
INFO_LASTNAME_STUDENT = "\053 Фамилия студента"
INFO_DOCNUM_STUDENT = "\053 Номер договора студента"
INFO_STATUS_STUDENT = "\053 Статус студента"
SHOW_TOTAL_NUMBER_STUDENTS_ON_SCREEN = 5

def main_menu_info():
    os.system('cls')
    print(f"Добавление записи \\ {ADD_RECORD}")
    print(f"показать записи \\ {SHOW_RECORDS}" )
    print(f"удлить запись \\ {DELETE_RECORD}")
    print(f"редактировать запись \\ {EDIT_RECORD}")
    user_key_press = int(input(f"Выход из меню \\ {EXIT_NUMBER}"))
    return user_key_press

def add_record():
    os.system('cls')
    firstname_of_student = input(INFO_FIRSTNAME_STUDENT + ":")
    secondname_of_student = input(INFO_LASTNAME_STUDENT + ":")
    docnum_of_student = input(INFO_DOCNUM_STUDENT + ":")
    status_of_student = input(INFO_STATUS_STUDENT +  ":")
    proof = input("Потвердите добавление записи: y\\n:")
    if proof == "y":
        database = open(NAME_OF_DATABASE,"a")
        print(firstname_of_student, file=database)
        print(secondname_of_student, file=database)
        print(docnum_of_student, file=database)
        print(status_of_student, file=database)
        database.close()
        print(f"Студент {firstname_of_student} {secondname_of_student} договор {docnum_of_student} статус {status_of_student} записан в файл {NAME_OF_DATABASE}")
        input("Нажмите любую клавишу для продолжения.")

def show_records():
    os.system('cls')
    database = open(NAME_OF_DATABASE,"r")
    CURRENT_TOTAL_NUMBER_STUDENTS_ON_SCREEN = 0
    RAW_LINE_CURRENT = 0 # Текущие положение строки , Будем сравнивать с константами отображения RAW_
    RAW_NUMBER_ID = 1
    while True:
        #Прочитали строоку из файла и выходим если строка пустая
        txt_line = database.readline()
        if not txt_line: break

        RAW_LINE_CURRENT += 1
        if RAW_LINE_CURRENT == RAW_FIRSTNAME_STUDENT: print(INFO_FIRSTNAME_STUDENT,":", txt_line , end="", sep=" ")
        elif RAW_LINE_CURRENT == RAW_LASTNAME_STUDENT: print(INFO_LASTNAME_STUDENT,":", txt_line ,end="", sep=" ")
        elif RAW_LINE_CURRENT == RAW_DOCNUM_STUDENT: print(INFO_DOCNUM_STUDENT,":", txt_line , end="", sep=" ")
        elif RAW_LINE_CURRENT == RAW_STATUS_STUDENT: print(INFO_STATUS_STUDENT,":", txt_line , end="", sep=" ")

        if RAW_LINE_CURRENT == RAW_LINE_TOTAL:
            print(f"\133 Номер записи: {RAW_NUMBER_ID} \135 \n") #Вывод номера текущий записи
            RAW_LINE_CURRENT = 0 #Сбрасываем счетчик таблицы данных
            CURRENT_TOTAL_NUMBER_STUDENTS_ON_SCREEN +=1 # Считаем количесто записей на экране
            RAW_NUMBER_ID +=1

        if CURRENT_TOTAL_NUMBER_STUDENTS_ON_SCREEN == SHOW_TOTAL_NUMBER_STUDENTS_ON_SCREEN:
            CURRENT_TOTAL_NUMBER_STUDENTS_ON_SCREEN = 0
            input(f"Действия со студентами: \\Показать остальные записи")
            os.system('cls')

    database.close()
    input("Больше нет записей в файле. Нажмите любую клавишу чтобы продолжить.")

def delete_record():
    os.system('cls')
    number_for_delete = int(input("Введите ID записи которую надо удалить:"))
    if number_for_delete <=0:
        print("Число не может меньше или быть равно 0")
        input("Нажмите любую клавишу для продолжения")
        return ""

    list_of_records = []
    database = open(NAME_OF_DATABASE,"r")
    while True:
        txt_line = database.readline()
        if not txt_line: break
        list_of_records.append(txt_line)
    database.close()

    RAW_FIRST_FOR_DELETE = RAW_LINE_TOTAL * number_for_delete - RAW_LINE_TOTAL # Получили первый номер для удаления
    RAW_LINE_CURRENT = 1
    while RAW_LINE_CURRENT != RAW_LINE_TOTAL+1:
        if RAW_LINE_CURRENT == RAW_FIRSTNAME_STUDENT: print(INFO_FIRSTNAME_STUDENT,":", list_of_records[RAW_FIRST_FOR_DELETE] , end="", sep=" ")
        elif RAW_LINE_CURRENT == RAW_LASTNAME_STUDENT: print(INFO_LASTNAME_STUDENT,":", list_of_records[RAW_FIRST_FOR_DELETE+1] ,end="", sep=" ")
        elif RAW_LINE_CURRENT == RAW_DOCNUM_STUDENT: print(INFO_DOCNUM_STUDENT,":", list_of_records[RAW_FIRST_FOR_DELETE+2] , end="", sep=" ")
        elif RAW_LINE_CURRENT == RAW_STATUS_STUDENT: print(INFO_STATUS_STUDENT,":", list_of_records[RAW_FIRST_FOR_DELETE+3] , end="", sep=" ")
        RAW_LINE_CURRENT +=1

    print(f"\133 Номер записи: {number_for_delete} \135 \n")
    proof = input("Действительно хотите удалить данную запись? y\n:")
    if proof == "y":
        make_copy_of_base(NAME_OF_BACKUP,list_of_records) #делаем бэк ап файла

        for i in range(RAW_LINE_TOTAL):
            list_of_records.pop(RAW_FIRST_FOR_DELETE)

        make_copy_of_base(NAME_OF_DATABASE,list_of_records) #Перезаписываем основную базу
    input("Операция выполнена успешно. Нажмите любую клавишу для продолжения")



def make_copy_of_base(NAME_OF_BACKUP, LIST_OF_RECORDS):
    database_backup = open(NAME_OF_BACKUP, "w")
    for RAW_LINE in LIST_OF_RECORDS:
        database_backup.write(RAW_LINE)
    database_backup.close()


#Добавим этот функционал в новой версии
#Проверка будет происходить при каждом изменение Базы данных
#def check_structure_of_database(database):
#    pass

user_key_press = -1
while True:
    key = main_menu_info()
    if key == ADD_RECORD: add_record()
    if key == SHOW_RECORDS: show_records()
    if key == DELETE_RECORD: delete_record()
    if key == 0: break
