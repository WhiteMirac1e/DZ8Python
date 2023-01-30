import view

# main_dct = {"FI":{"MATH":[6,3,4], "PHISC":[232]},"FI":}
main_dct = {}
student_name = []
lessons = []
def start():
    while True:
        op = view.get_op()
        if op == 1:
            student = view.input_student()
            if student not in student_name:
                main_dct[student] = {}
                student_name.append(student)
                if lessons:
                    for subject in lessons:
                        main_dct[student][subject] = []
        elif op == 2:
            subject = view.input_subject()
            lessons.append(subject)
            for name in student_name:
                main_dct[name][subject]=[]
        elif op == 3:
            name, subject, mark = view.input_mark()
            main_dct[name][subject].append(mark)
        elif op == 4:
            print(main_dct)
        elif op == 5:
            name = view.get_name_to_show()
            print(f"Оценки {name} - {main_dct[name]}")
        elif op == 6:
            break
        print(main_dct)
