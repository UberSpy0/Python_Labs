import argparse

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

COMMANDS = {
    "json2csv": (json_to_csv, "конвертировать JSON в CSV"),
    "csv2json": (csv_to_json, "конвертировать CSV в JSON"),
    "csv2xlsx": (csv_to_xlsx, "конвертировать CSV в XLSX"),
}

def main():
    parser = argparse.ArgumentParser(description="Конвертер JSON / CSV / XLSX")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for name, (_, help_text) in COMMANDS.items():
        sub = subparsers.add_parser(name, help=help_text)
        sub.add_argument("--in", dest="input", required=True, help="входной файл")
        sub.add_argument("--out", dest="output", required=True, help="выходной файл")

    args = parser.parse_args()
    convert = COMMANDS[args.command][0]

    try:
        convert(args.input, args.output)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {args.input}")
        raise SystemExit(1)
    except ValueError as error:
        print(f"Ошибка: {error}")
        raise SystemExit(1)

    print(f"Готово: {args.input} -> {args.output}")


if __name__ == "__main__":
    main()
