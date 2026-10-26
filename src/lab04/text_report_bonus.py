import argparse
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir


def main():
    parser = argparse.ArgumentParser(description="Отчёт по нескольким файлам")
    parser.add_argument("--in", dest="inputs", nargs="+", required=True,
                        help="входные файлы, например data/a.txt data/b.txt")
    parser.add_argument("--per-file", default="data/report_per_file.csv")
    parser.add_argument("--total", default="data/report_total.csv")
    parser.add_argument("--encoding", default="utf-8")
    args = parser.parse_args()

    per_file_rows = []
    total_freq = {}

    for path in sorted(args.inputs, key=lambda p: Path(p).name):
        try:
            text = read_text(path, encoding=args.encoding)
        except FileNotFoundError:
            print(f"FileNotFoundError: {path}")
            raise SystemExit(1)
        except UnicodeDecodeError:
            print(f"UnicodeDecodeError"
                  f"{args.encoding}. Попробуйте --encoding cp1251")
            raise SystemExit(1)

        freq = count_freq(tokenize(normalize(text)))
        for word, count in top_n(freq, len(freq)):
            per_file_rows.append((Path(path).name, word, count))
        for word, count in freq.items():
            total_freq[word] = total_freq.get(word, 0) + count

    ensure_parent_dir(args.per_file)
    ensure_parent_dir(args.total)
    write_csv(per_file_rows, args.per_file, header=("file", "word", "count"))
    write_csv(top_n(total_freq, len(total_freq)), args.total,
              header=("word", "count"))

    print(f"Файлов: {len(args.inputs)}")
    print(f"Уникальных слов во всех файлах: {len(total_freq)}")


if __name__ == "__main__":
    main()