import argparse
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text


def run_cat(path, numbered):
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(path)
    with p.open(encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            line = line.rstrip("\n")
            if numbered:
                print(f"{number}: {line}")
            else:
                print(line)


def run_stats(path, top):
    text = read_text(path)
    words = tokenize(normalize(text))
    freq = count_freq(words)
    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{top}:")
    for word, count in top_n(freq, top):
        print(f"{word}:{count}")


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты для работы с текстом")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="частоты слов в тексте")
    stats_parser.add_argument("--input", required=True, help="путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="сколько слов показать (по умолчанию 5)")

    args = parser.parse_args()

    if args.command == "stats" and args.top < 1:
        parser.error("--top должен быть не меньше 1")

    try:
        if args.command == "cat":
            run_cat(args.input, args.n)
        else:
            run_stats(args.input, args.top)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {args.input}")
        raise SystemExit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: файл {args.input} не читается как UTF-8")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
