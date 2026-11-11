import csv
import json
from pathlib import Path


def json_to_csv(json_path, csv_path):
    """
    Конвертация JSON (список словарей) в CSV.
    Колонки: порядок ключей из первого объекта, новые ключи из других
    объектов добавляются в конец. Пропущенные поля = пустая строка.
    """
    src = Path(json_path)
    dst = Path(csv_path)

    if src.suffix.lower() != ".json":
        raise ValueError("Ожидался файл с расширением .json")
    if not src.exists():
        raise FileNotFoundError(f"Файл не найден: {src}")

    with src.open(encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Некорректный JSON")

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("JSON должен быть списком словарей")

    fieldnames = list(data[0].keys())
    for item in data[1:]:
        for key in item:
            if key not in fieldnames:
                fieldnames.append(key)
    if not fieldnames:
        raise ValueError("В JSON нет ни одного поля")

    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path, json_path):
    """
    Конвертирует CSV (с заголовком) в JSON (список словарей). Значения остаются строками.
    """
    src = Path(csv_path)
    dst = Path(json_path)

    if src.suffix.lower() != ".csv":
        raise ValueError("Ожидался файл с расширением .csv")
    if not src.exists():
        raise FileNotFoundError(f"Файл не найден: {src}")

    with src.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV пустой или без заголовка")
        rows = list(reader)

    if not rows:
        raise ValueError("В CSV нет данных")

    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)