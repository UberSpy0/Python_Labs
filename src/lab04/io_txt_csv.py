import csv
from pathlib import Path


def read_text(path, encoding="utf-8"):
    """
    Читает текстовый файл целиком и возвращает строку.

    Сначала пробует UTF-8. Если файл в UTF-8, кодировка из параметра
    не применяется. Только если UTF-8 не подошёл, файл читается в указанной кодировке.
    """
    p = Path(path)
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        if encoding.lower().replace("-", "") == "utf8":
            raise
        return p.read_text(encoding=encoding)


def write_csv(rows, path, header=None):
    """
    Создаёт или перезаписывает CSV (через разделитель ",", с кодировкой UTF-8).
    Если передан header, он пишется первой строкой.
    Если строки (и заголовок) разной длины - ValueError.
    """
    rows = [tuple(row) for row in rows]
    lengths = {len(row) for row in rows}
    if header is not None:
        header = tuple(header)
        lengths.add(len(header))
    if len(lengths) > 1:
        raise ValueError("Все строки должны быть одинаковой длины")

    with Path(path).open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)


def ensure_parent_dir(path):
    """Создаёт родительские папки для path"""
    Path(path).parent.mkdir(parents=True, exist_ok=True)