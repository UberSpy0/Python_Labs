import argparse
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir


def print_table(header, rows):
    table = [header] + [tuple(str(v) for v in row) for row in rows]
    widths = [max(len(row[i]) for row in table) for i in range(len(header))]

    def fmt(row):
        cells = []
        for value, width in zip(row, widths):
            cells.append(value.rjust(width) if value.isdigit() else value.ljust(width))
        return " | ".join(cells)

    print(fmt(header))
    print("-+-".join("-" * w for w in widths))
    for row in table[1:]:
        print(fmt(row))


def read_or_exit(path, encoding):   #обработка ошибок
    try:
        return read_text(path, encoding=encoding)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {path}")
        raise SystemExit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: не удалось прочитать {path} в кодировке {encoding}. "
              f"Попробуйте --encoding cp1251")
        raise SystemExit(1)


def main():
    parser = argparse.ArgumentParser(description="Частотный отчёт по текстам")
    parser.add_argument("--in", dest="inputs", nargs="+", default=["data/input.txt"],
                        help="один или несколько входных файлов")
    parser.add_argument("--out", default="data/report.csv",
                        help="отчёт для одного файла")
    parser.add_argument("--per-file", default="data/report_per_file.csv",
                        help="отчёт по каждому файлу (если файлов несколько)")
    parser.add_argument("--total", default="data/report_total.csv",
                        help="сводный отчёт (если файлов несколько)")
    parser.add_argument("--encoding", default="utf-8")
    args = parser.parse_args()

    per_file_rows = []
    total_freq = {}
    total_words = 0

    for path in sorted(args.inputs, key=lambda p: Path(p).name):
        text = read_or_exit(path, args.encoding)
        words = tokenize(normalize(text))
        freq = count_freq(words)
        total_words += len(words)
        for word, count in top_n(freq, len(freq)):
            per_file_rows.append((Path(path).name, word, count))
        for word, count in freq.items():
            total_freq[word] = total_freq.get(word, 0) + count

    total_rows = top_n(total_freq, len(total_freq))

    if len(args.inputs) == 1:
        ensure_parent_dir(args.out)
        write_csv(total_rows, args.out, header=("word", "count"))
    else:
        ensure_parent_dir(args.per_file)
        ensure_parent_dir(args.total)
        write_csv(per_file_rows, args.per_file, header=("file", "word", "count"))
        write_csv(total_rows, args.total, header=("word", "count"))

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {len(total_freq)}")
    print("Топ-5:")
    for word, count in top_n(total_freq, 5):
        print(f"{word}:{count}")

    print()
    if len(args.inputs) > 1:
        print("По файлам:")
        print_table(("file", "word", "count"), per_file_rows)
        print()
    print_table(("word", "count"), top_n(total_freq, 5))


if __name__ == "__main__":
    main()