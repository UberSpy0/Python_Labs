import csv
from pathlib import Path


def read_text(path, encoding="utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows, path, header=None):
    p = Path(path)
    rows = list(rows)
    if rows:
        length = len(rows[0])
        for r in rows:
            if len(r) != length:
                raise ValueError("ValueError")
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


def ensure_parent_dir(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)