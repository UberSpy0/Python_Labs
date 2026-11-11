import re
from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def _check_text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name}: нужна непустая строка")


def _check_birthdate(value):
    if not isinstance(value, str):
        raise ValueError("birthdate: нужна строка в формате YYYY-MM-DD")
    # fromisoformat в новых Python принимает и другие записи (20070514), поэтому формат проверяем сами
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError(f"birthdate: '{value}' не в формате YYYY-MM-DD")
    try:
        born = date.fromisoformat(value)
    except ValueError:
        raise ValueError(f"birthdate: '{value}' - такой даты не существует")
    if born > date.today():
        raise ValueError(f"birthdate: дата {value} находится в будущем")


def _check_gpa(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("gpa: нужно число (int или float)")
    if not 0 <= value <= 5:
        raise ValueError(f"gpa: {value} вне диапазона 0..5")


def make_student(fio, birthdate, group, gpa):
    """Собирает запись, проверяя каждое поле"""
    _check_text(fio, "fio")
    _check_birthdate(birthdate)
    _check_text(group, "group")
    _check_gpa(gpa)
    return {
        "fio": fio.strip(),
        "birthdate": birthdate,
        "group": group.strip(),
        "gpa": float(gpa),
    }


def validate_student(rec):
    """Проверяет готовую запись: набор ключей и значения"""
    if not isinstance(rec, dict):
        raise ValueError("запись должна быть словарём")
    missing = [key for key in STUDENT_FIELDS if key not in rec]
    extra = [key for key in rec if key not in STUDENT_FIELDS]
    if missing:
        raise ValueError(f"не хватает полей: {', '.join(missing)}")
    if extra:
        raise ValueError(f"лишние поля: {', '.join(map(str, extra))}")
    _check_text(rec["fio"], "fio")
    _check_birthdate(rec["birthdate"])
    _check_text(rec["group"], "group")
    _check_gpa(rec["gpa"])


def student_age(rec, today=None):
    """Сколько полных лет студенту на дату today (по умолчанию сегодня)"""
    born = date.fromisoformat(rec["birthdate"])
    if today is None:
        today = date.today()
    years = today.year - born.year
    if (today.month, today.day) < (born.month, born.day):
        years -= 1          #день рождения в этом году ещё не наступил
    return years


def _years_word(n):
    if 11 <= n % 100 <= 14:
        return "лет"
    if n % 10 == 1:
        return "год"
    if 2 <= n % 10 <= 4:
        return "года"
    return "лет"


def format_student(rec):
    """Красивый вывод: Иванов И.И. (БИВТ-26-6-1), 19 лет, GPA 4.30"""
    parts = rec["fio"].split()
    initials = "".join(part[0].upper() + "." for part in parts[1:])
    name = f"{parts[0]} {initials}".strip()
    age = student_age(rec)
    return f"{name} ({rec['group']}), {age} {_years_word(age)}, GPA {rec['gpa']:.2f}"


def student_to_dict(rec):
    """Копия записи (не та же самая) для сериализации"""
    validate_student(rec)
    return {key: rec[key] for key in STUDENT_FIELDS}


def student_from_dict(d):
    """
    Десериализация: берём ровно нужные ключи (лишние игнорируются),
    строку gpa (из CSV) приводим к float, затем валидируем
    """
    if not isinstance(d, dict):
        raise ValueError("запись должна быть объектом (словарём)")
    missing = [key for key in STUDENT_FIELDS if key not in d]
    if missing:
        raise ValueError(f"не хватает полей: {', '.join(missing)}")

    rec = {key: d[key] for key in STUDENT_FIELDS}
    if isinstance(rec["gpa"], str):
        try:
            rec["gpa"] = float(rec["gpa"])
        except ValueError:
            raise ValueError(f"gpa: '{rec['gpa']}' не число")
    elif isinstance(rec["gpa"], int) and not isinstance(rec["gpa"], bool):
        rec["gpa"] = float(rec["gpa"])

    validate_student(rec)
    return rec


def update_student(rec, **fields):
    """
    * Возвращает НОВУЮ запись с изменёнными полями, исходная не меняется
    """
    for key in fields:
        if key not in STUDENT_FIELDS:
            raise KeyError(f"неизвестное поле: {key}")
    new_rec = dict(rec)
    new_rec.update(fields)
    if isinstance(new_rec["gpa"], int) and not isinstance(new_rec["gpa"], bool):
        new_rec["gpa"] = float(new_rec["gpa"])
    validate_student(new_rec)
    return new_rec
