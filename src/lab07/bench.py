import random
import timeit

from src.lab04.io_txt_csv import write_csv, ensure_parent_dir
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort, merge_sort, counting_sort

OUT_PATH = "data/lab07/bench.csv"
SLOW_LIMIT = 10000          #квадратичные сортировки на больших n не производятся
SLOW_MARK = ">60"           #оценка: на n=100000 они работают дольше минуты


def measure(func, n):
    """Среднее время одного вызова. Для маленьких n повторяется, чтобы уменьшить шум"""
    number = max(1, 20000 // n)
    return timeit.timeit(func, number=number) / number


def bench_sorting(data, rows):
    sorters = [
        ("bubble_sort", bubble_sort, True),
        ("insertion_sort", insertion_sort, True),
        ("selection_sort", selection_sort, True),
        ("merge_sort", merge_sort, False),
        ("sorted", sorted, False),
    ]
    for n in (1000, 10000, 100000):
        part = data[:n]
        for name, fn, quadratic in sorters:
            if quadratic and n > SLOW_LIMIT:
                rows.append(("sort", n, name, SLOW_MARK))
            else:
                rows.append(("sort", n, name, f"{measure(lambda: fn(part), n):.6f}"))


def bench_narrow(rows):
    """counting_sort выигрывает у sorted, когда диапазон значений узкий"""
    n = 100000
    narrow = [random.randint(0, 1000) for _ in range(n)]
    rows.append(("sort_narrow", n, "counting_sort", f"{measure(lambda: counting_sort(narrow, 0, 1000), n):.6f}"))
    rows.append(("sort_narrow", n, "sorted", f"{measure(lambda: sorted(narrow), n):.6f}"))


def bench_search(data, rows):
    n = len(data)
    queries = [random.choice(data) for _ in range(10000)]

    start = timeit.default_timer()
    sorted_data = sorted(data)
    sort_time = timeit.default_timer() - start

    start = timeit.default_timer()
    for x in queries:
        linear_search(data, x)
    linear_time = timeit.default_timer() - start

    start = timeit.default_timer()
    for x in queries:
        binary_search(sorted_data, x)
    binary_time = timeit.default_timer() - start

    rows.append(("search", n, "linear_search x10000", f"{linear_time:.6f}"))
    rows.append(("search", n, "sorted (before binary)", f"{sort_time:.6f}"))
    rows.append(("search", n, "binary_search x10000", f"{binary_time:.6f}"))


def bench_two_sum(data, rows):
    for n in (1000, 10000):
        #единственная подходящая пара стоит в самом конце списка, это худший случай
        nums = data[:n - 2] + [10 ** 9, 10 ** 9 + 1]
        target = 2 * 10 ** 9 + 1
        for name, fn in (("two_sum_brute", two_sum_brute), ("two_sum_fast", two_sum_fast)):
            seconds = measure(lambda: fn(nums, target), n)
            rows.append(("two_sum", n, name, f"{seconds:.6f}"))


def print_table(header, rows):
    table = [header] + [tuple(str(v) for v in row) for row in rows]
    widths = [max(len(row[i]) for row in table) for i in range(len(header))]
    for index, row in enumerate(table):
        print(" | ".join(value.ljust(width) for value, width in zip(row, widths)))
        if index == 0:
            print("-+-".join("-" * width for width in widths))


def main():
    random.seed(42)
    data = [random.randint(-1000000, 1000000) for _ in range(100000)]
    rows = []

    bench_sorting(data, rows)
    bench_narrow(rows)
    bench_search(data, rows)
    bench_two_sum(data, rows)

    header = ("task", "n", "impl", "seconds")
    print_table(header, rows)

    ensure_parent_dir(OUT_PATH)
    write_csv(rows, OUT_PATH, header=header)
    print(f"\nСохранено: {OUT_PATH}")


if __name__ == "__main__":
    main()
