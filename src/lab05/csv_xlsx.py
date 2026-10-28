import csv
from pathlib import Path

from openpyxl import Workbook


def csv_to_xlsx(csv_path, xlsx_path):
    """
    Конвертация CSV в XLSX
    """
    src = Path(csv_path)
    dst = Path(xlsx_path)

    if src.suffix.lower() != ".csv":
        raise ValueError("Ожидался файл с расширением .csv")
    if not src.exists():
        raise FileNotFoundError(f"Файл не найден: {src}")

    with src.open(encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))

    if not rows or not any(rows[0]):
        raise ValueError("CSV пустой или без заголовка")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    for column in ws.columns:
        longest = max(len(str(cell.value)) if cell.value is not None else 0
                      for cell in column)
        ws.column_dimensions[column[0].column_letter].width = max(longest, 8)

    dst.parent.mkdir(parents=True, exist_ok=True)
    wb.save(dst)
