from src.lab08.models import make_student, format_student, update_student
from src.lab08.serialize import students_to_json, students_from_json


def main():
    print("1. Корректные записи туда-обратно")
    students = students_from_json("data/lab08/students_input.json")
    students_to_json(students, "data/lab08/students_output.json")
    again = students_from_json("data/lab08/students_output.json")
    print("до == после:", students == again)
    for rec in again:
        print(format_student(rec))

    print("\n2. Запись с неверной датой (2003-02-30)")
    try:
        make_student("Иванов Иван Иванович", "2003-02-30", "БИВТ-26-6-1", 4.0)
    except ValueError as error:
        print("ValueError:", error)

    print("\n3. Запись с gpa = 7")
    try:
        make_student("Иванов Иван Иванович", "2007-05-14", "БИВТ-26-6-1", 7)
    except ValueError as error:
        print("ValueError:", error)

    print("\n4. Битый файл, политика strict")
    try:
        students_from_json("data/lab08/students_bad.json")
    except ValueError as error:
        print("ValueError:", error)

    print("\n5. Битый файл, политика skip")
    good = students_from_json("data/lab08/students_bad.json", policy="skip")
    print("Прочитано корректных записей:", len(good))

    print("\n6. * update_student не меняет исходную запись")
    first = again[0]
    second = update_student(first, gpa=4.8)
    print("было:", first["gpa"], "стало:", second["gpa"])


if __name__ == "__main__":
    main()
