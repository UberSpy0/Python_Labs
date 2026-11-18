import csv
import json
from pathlib import Path

from src.lab08.models import student_to_dict, student_from_dict


def students_to_json(students, path):
    """Сохраняет список записей в JSON (массив объектов, UTF-8, отступ 2)"""
    data = [student_to_dict(s) for s in students]
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path, policy="strict"):
    """
    Читает JSON-массив и прогоняет каждую запись через student_from_dict

    Политика обработки битых записей:
      "strict" (по умолчанию), а первая же ошибка вызовет ValueError с номером записи;
      "skip" - битые записи пропускаются, в конце печатается, сколько пропущено и почему
    """
    if policy not in ("strict", "skip"):
        raise ValueError("policy должна быть 'strict' или 'skip'")

    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {p}")
    with p.open(encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Некорректный JSON")
    if not isinstance(data, list):
        raise ValueError("JSON должен быть массивом объектов")

    students = []
    skipped = []
    for number, item in enumerate(data, start=1):
        try:
            students.append(student_from_dict(item))
        except ValueError as error:
            if policy == "strict":
                raise ValueError(f"запись №{number}: {error}")
            skipped.append((number, str(error)))

    if skipped:
        print(f"Пропущено записей: {len(skipped)}")
        for number, reason in skipped:
            print(f"  запись №{number}: {reason}")
    return students


def students_from_csv(path):
    """* Читает записи из CSV (заголовок fio,birthdate,group,gpa). gpa приходит строкой"""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {p}")
    students = []
    with p.open(newline="", encoding="utf-8") as f:
        for number, row in enumerate(csv.DictReader(f), start=1):
            try:
                #здесь строка gpa превращается в float - внутри student_from_dict
                students.append(student_from_dict(row))
            except ValueError as error:
                raise ValueError(f"строка №{number}: {error}")
    return students
