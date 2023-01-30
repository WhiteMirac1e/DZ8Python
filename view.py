def get_op():
    op = int(input(
        " 1 - добавить нового студента \n 2 - добавить предмет \n 3 - добавить оценки ученику по предмету \n 4 - показ списка учеников \n 5 - показ листа оценок конкретного ученика \n 6 - выход \n"))
    return op

def input_student():
    name = input("Введите имя и фамилию: ")
    return name

def input_subject():
    subject = input("Введите название предмета: ")
    return subject

def input_mark():
    name = input("Введите имя: ")
    subject = input("Введите предмет: ")
    mark = input("Введите оценку: ")
    return name, subject, mark

def get_name_to_show():
    name = input("Введи имя для просмотра оценки")
