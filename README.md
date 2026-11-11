# Лабораторные работы по Python

Репозиторий с лабораторными работами. Исходный код находится в [src/](src/), скриншоты выполнения программ — в [images/](images/).

---

## [Лабораторная работа №1](src/lab01/)  `ВЫПОЛНЕНА`

### 1. Приветствие — [01_greeting.py](src/lab01/01_greeting.py)

Программа запрашивает имя и возраст пользователя, после чего выводит приветствие и сообщает, сколько лет ему исполнится через год.

**Как работает код:** имя читается через `input()` как строка, возраст приводится к целому числу с помощью `int()`. Результат выводится f-строкой, в которой прямо в выражении вычисляется `age+1`.

![Приветствие](images/lab01/01_greeting.png)

---

### 2. Сумма и среднее — [02_sum_avg.py](src/lab01/02_sum_avg.py)

Программа считывает два вещественных числа и выводит их сумму и среднее арифметическое.

**Как работает код:** оба числа читаются через `input()` и преобразуются в `float`, чтобы работать с дробными значениями. В f-строке вычисляются сумма `a+b` и среднее `(a+b)/2`.

![Сумма и среднее](images/lab01/02_sum_avg.png)

---

### 3. Скидка и НДС — [03_discount_vat.py](src/lab01/03_discount_vat.py)

Программа рассчитывает итоговую стоимость товара: сначала применяется скидка, затем на полученную базу начисляется НДС.

**Как работает код:** на вход подаются цена, процент скидки и процент НДС. База считается как `price*(1-discount/100)`, сумма НДС — как `base*vat/100`, итог — их сумма. Все три значения выводятся с округлением до двух знаков через спецификатор формата `:.2f`.

![Скидка и НДС](images/lab01/03_discount_vat.png)

---

### 4. Минуты в часы:минуты — [04_minutes_to_hhmm.py](src/lab01/04_minutes_to_hhmm.py)

Программа переводит количество минут в формат `ЧЧ:ММ`.

**Как работает код:** целочисленное деление `min//60` даёт часы, остаток от деления `min%60` — минуты. Спецификатор `:02d` применяется к обеим частям и дополняет их ведущим нулём, поэтому и часы, и минуты всегда выводятся двузначными.

![Минуты в часы](images/lab01/04_minutes_to_hhmm.png)

---

### 5. Инициалы и длина ФИО — [05_initials_and_len.py](src/lab01/05_initials_and_len.py)

Программа принимает ФИО и выводит инициалы, а также суммарное количество букв.

**Как работает код:** строка разбивается по пробелам методом `split()` на три части, которые распаковываются в переменные `n1, n2, n3`. Из каждой берётся первый символ и переводится в верхний регистр через `upper()`. Длина считается как сумма `len()` трёх частей — пробелы при этом не учитываются.

![Инициалы и длина](images/lab01/05_initials_and_len.png)

---

### 6. Список регистраций — [06_registration_list.py](src/lab01/06_registration_list.py)

Программа считывает `n` корректных записей о регистрации и подсчитывает, сколько из них со статусом `True`, а сколько — с `False`.

**Как работает код:** цикл `while` работает, пока не набрано `n` валидных записей. Каждая строка проверяется на соответствие формату: первые два поля должны быть буквенными (`isalpha()`), третье — числом (`isdigit()`). Счётчик `i` увеличивается только при успешной проверке, поэтому некорректная запись не засчитывается и запрашивается заново. Приглашение ко вводу нумеруется (`in_1:`, `in_2:`, ...), а в конце выводятся счётчики `t` и `f` с префиксом `out:`.

![Список регистраций](/images/lab01/06_registration_list.png)

---

### 7. Расшифровка сообщения — [07_decryption.py](src/lab01/07_decryption.py)

Программа извлекает скрытое сообщение из зашумлённой строки.

**Как работает код:** сначала два цикла находят позицию первой заглавной буквы (`n1`) и позицию первой цифры (`n2`). Разница `m = n2 - n1` задаёт шаг выборки символов. Далее строка обходится начиная с `n1`, и каждый символ, индекс которого кратен `m+1`, добавляется к результату. Обход прерывается при встрече точки — она отмечает конец сообщения.

![Расшифровка](images/lab01/07_decryption.png)

---

## [Лабораторная работа №2](src/lab02/) `ВЫПОЛНЕНА`

### 1 - arrays.py

- `min_max` — проходит по списку циклом и сравнивает каждое число, параллельно заменяя актуальное максимальное и минимальное число. Возвращает котедж `(минимум, максимум)`. Если дан пустой список — `ValueError`.
- `unique_sorted` — превращает список в `set`, чтобы убрать повторы, и сортирует через `sorted()`.
- `flatten` — проходит циклом по значениям всех списков и котеджей в общем списке и складывает все их элементы в один список. Если строка не список и не кортеж — `TypeError`.

**Тесты:**

![Тесты arrays.py](images/lab02/arrays.png)

---

### B - matrix.py

- `transpose(mat)` — для каждого столбца собирает его элементы в новую строку, так строки и столбцы меняются местами.
- `row_sums(mat)` — складывает числа в каждой строке.
- `col_sums(mat)` — складывает числа в каждом столбце.

Все три функции сначала проверяют, что строки одной длины, то есть прямоугольность матрицы. Если нет — `ValueError`.

**Тесты:**

![Тесты matrix.py](images/lab02/matrix.png)

---

### C - tuples.py

- `format_record(rec)` — принимает запись студента формата `(ФИО, группа, GPA)`, убирает лишние пробелы в начале и в конце строки используя `strip()`, записывает инициалы и возвращает строку вида `Иванов И.И., гр. BIVT-25, GPA 4.60`. Неверный тип данных — `TypeError`, пустые или неверные значения — `ValueError`.

**Тесты:**

![Тесты tuples.py](images/lab02/tuples.png)

---

## [Лабораторная работа №3](src/lab03/) `ВЫПОЛНЕНА`

### A - text.py — [src/lib/text.py](src/lib/text.py)

- `normalize` — приводит текст к нижнему регистру через `casefold()` (или `lower()`, если `casefold=False`), заменяет `ё` на `е`, меняет `\t`, `\r` и `\n` на пробелы и убирает лишние пробелы через `split()` и `" ".join()`. Если передана не строка — `TypeError`.
- `tokenize` — находит слова регулярным составленным выражением `\w+(?:-\w+)*`: буквы, цифры и **дефис внутри слова**, например,`по-настоящему`. Эмодзи и знаки препинания пропускаются выражением.
- `count_freq` — проходит по списку слов и считает, сколько раз встречается каждое. Возвращает словарь `слово: количество`.
- `top_n` — сортирует пары `(слово, количество)` по ключу `(количество, слово)`, то есть сначала по убыванию частоты, а при равенстве по алфавиту берёт первые `n`.

**Тесты через `assert`:**

![Цикл проверки](images/lab03/text_tests.png)

![Результат:](images/lab03/text.png)

---

### B - text_stats.py — [src/lab03/text_stats.py](src/lab03/text_stats.py)

Программа читает одну строку из stdin и выводит количество слов, количество уникальных слов и топ-5 самых частых, используя **испортированные функции**: `normalize`, `count_freq`, и `top_n`.

**Запуск** (из корня проекта):

![Запуск](images/lab03/text_stats.png)

---

### ★ - text_table.py — [src/lab03/text_table.py](src/lab03/text_table.py)

Программа делает то же самое, что и `text_stats.py`, но просто выводит топ-5 в виде выровненной таблицы.

**Запуск:**

![Таблица](images/lab03/text_table.png)

---

## [Лабораторная работа №4](src/lab04/) `ВЫПОЛНЕНА`

### A - io_txt_csv.py — [src/lab04/io_txt_csv.py](src/lab04/io_txt_csv.py)

- `read_text` — читает файл целиком в одну строку. Сначала пробует `utf-8`. Если файл в `utf-8`, параметр `encoding` не применяется. Только если `utf-8` не подошёл, файл читается в указанной кодировке: `read_text("file.txt", encoding="cp1251")`. Если файла нет — `FileNotFoundError`, если не подошла ни одна кодировка — `UnicodeDecodeError`.
- `write_csv` — создаёт или перезаписывает CSV (разделитель `,`, кодировка UTF-8). Если передан `header`, он пишется первой строкой. Если строки разной длины — `ValueError`.
- `ensure_parent_dir` — создаёт родительские папки, если их нет.

**Пустые данные:** `write_csv` с пустым `rows` и без `header` создаёт пустой файл, а с `header` — файл только с заголовком.

**Тест (запись и чтение):**

```bash
python3 -c "from src.lab04.io_txt_csv import read_text, write_csv; write_csv([('test', 3)], 'data/check.csv', header=('word', 'count')); print(read_text('data/check.csv'))"
```

![Тест A: Один Файл](images/lab04/At.png)

---

### B - text_report.py — [src/lab04/text_report.py](src/lab04/text_report.py)

Скрипт читает текстовый файл, считает частоты слов (функции из ЛР3), сохраняет отчёт в CSV и печатает в консоль краткое резюме и таблицу.

**Запуск** (через `-m`, чтобы Python нашёл пакет `src`):

```bash
printf 'Привет, мир! Привет!!!\n' > data/input.txt && python3 -m src.lab04.text_report && cat data/report.csv
```

**Параметры:** `--in` (входной файл, по умолчанию `data/input.txt`), `--out` (по умолчанию `data/report.csv`), `--encoding` (по умолчанию `utf-8`).

**Решения:**
- **Нет файла** или **неверная кодировка:** выводится понятное сообщение и код выхода 1.
- **Пустой файл:** `report.csv` содержит только заголовок `word,count`.
- **Кодировка cp1251:** передаётся через `--encoding cp1251`, расшифровка применяется только если файл не читается как `utf-8`.
- **Большие файлы:** файл читается целиком; в реальных задачах лучше читать построчно.

![Запуск: один файл](images/lab04/Bt.png)

![report.csv](images/lab04/report_image.png)

**Пустой файл:**

```bash
: > data/input.txt && python3 -m src.lab04.text_report && cat data/report.csv
```

![Пустой файл](images/lab04/Bempty.png)

---

### Тест C — параметр `--encoding`

`read_text` сначала пробует прочитать файл как `utf-8`. Если получилось, параметр `--encoding` не используется. Если `utf-8` не подошёл, файл читается в кодировке из `--encoding`. Если не подошла и она, скрипт выводит сообщение с подсказкой `Попробуйте --encoding cp1251` и завершается с кодом 1.

Так расшифровка делается только тогда, когда она нужна, и обычный `utf-8` файл не превращается в кракозябры, даже если указать `--encoding cp1251`.

**C1. Файл действительно в cp1251** (расшифровка нужна и выполняется):

```bash
printf 'Привет' | iconv -f UTF-8 -t CP1251 > data/input.txt && python3 -m src.lab04.text_report --encoding cp1251 && cat data/report.csv
```

Вывод (кратко):

```
Всего слов: 1
Уникальных слов: 1
Топ-5:
привет:1
```

`report.csv`:

```
word,count
привет,1
```

![Тест C1: файл в cp1251](images/lab04/Ct.png)

**C2. Файл в utf-8, но указан `--encoding cp1251`** (расшифровка не нужна и не применяется, результат тот же, без кракозябр):

```bash
printf 'Привет' > data/input.txt && python3 -m src.lab04.text_report --encoding cp1251 && cat data/report.csv
```

![Тест C2: utf-8 с флагом cp1251](images/lab04/Ct2.png)

---

### D* - несколько файлов — [src/lab04/text_report.py](src/lab04/text_report.py)

Если передать несколько файлов, скрипт создаёт два отчёта: `report_per_file.csv` (колонки `file,word,count`) и `report_total.csv` (`word,count`). Таблица в консоль печатается всегда, ширина столбцов по самому длинному значению.

```bash
printf 'Привет мир' > data/a.txt && printf 'Привет, привет!' > data/b.txt && python3 -m src.lab04.text_report --in data/a.txt data/b.txt && cat data/report_per_file.csv data/report_total.csv
```

![Несколько файлов](images/lab04/D_star.png)

---

## Сброс файла ``input.txt`` для повторного запуска тестов:

```bash
: > data/input.txt
```

![Проведение сброса](images/lab04/Treset.png)

---

## [Лабораторная работа №5](src/lab05/) `ВЫПОЛНЕНА`

### Что выполнено
- `src/lab05/json_csv.py` — функции `json_to_csv` и `csv_to_json`
- `src/lab05/csv_xlsx.py` — функция `csv_to_xlsx` (с использованием библиотеки openpyxl)
- примеры в `data/samples/`, результаты в `data/out/`

### Установка нужных библиотек
```
pip3 install -r requirements.txt
```

### Допущения
- JSON должен быть списком словарей.
- Порядок колонок в CSV: как в первом объекте, новые ключи из остальных идут в конец.
- Пропущенные поля заполняются пустой строкой.
- Все значения из CSV в JSON остаются строками.
- Кодировка везде UTF-8.
- Ошибки: неверное расширение или пустой файл — `ValueError`, нет файла — `FileNotFoundError`.

### Задание A: JSON to CSV
```
python3 -c "from src.lab05.json_csv import json_to_csv; json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv')" && cat data/out/people_from_json.csv && wc -l data/out/people_from_json.csv
```
![json_to_csv](images/lab05/json_to_csv.png)

### Задание A: CSV to JSON
```
python3 -c "from src.lab05.json_csv import csv_to_json; csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json')"
```
![csv_to_json](images/lab05/csv_to_json.png)

### Задание B: CSV to XLSX
```
python3 -c "from src.lab05.csv_xlsx import csv_to_xlsx; csv_to_xlsx('data/samples/people.csv', 'data/out/people.xlsx')"
```
![xlsx](images/lab05/xlsx.png)

---

## [Лабораторная работа №6](src/lab06/) `ВЫПОЛНЕНА`

Консольные утилиты на `argparse`. Запускаются как модули (`python3 -m ...`) из корня репозитория, чтобы Python нашёл пакет `src`.

### A - cli_text.py — [src/lab06/cli_text.py](src/lab06/cli_text.py)

- `cat --input <файл> [-n]` — печатает файл построчно, с `-n` перед строкой добавляется её номер.
- `stats --input <файл> [--top 5]` — считает слова (функции из ЛР3) и печатает всего слов, уникальных слов и топ-N.

**Решения:**
- Нет файла — сообщение `Ошибка: файл не найден: ...` и код выхода 1.
- `--top` меньше 1 — ошибка через `parser.error`.
- `--help` работает для программы и для каждой подкоманды.

```bash
python3 -m src.lab06.cli_text cat --input data/samples/people.csv -n
```

![cat -n](images/lab06/cat.png)

```bash
python3 -m src.lab06.cli_text stats --input data/samples/people.txt --top 5
```

![stats](images/lab06/stats.png)

```bash
python3 -m src.lab06.cli_text --help
```

![help cli_text](images/lab06/help_text.png)

### B - cli_convert.py — [src/lab06/cli_convert.py](src/lab06/cli_convert.py)

Три подкоманды вызывают функции из ЛР5. У всех одинаковые параметры: `--in` (входной файл) и `--out` (выходной файл), оба обязательные.

```bash
python3 -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people.csv
```

![json2csv](images/lab06/json2csv.png)

```bash
python3 -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people.json
```

![csv2json](images/lab06/csv2json.png)

```bash
python3 -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx
```

![csv2xlsx](images/lab06/csv2xlsx.png)

```bash
python3 -m src.lab06.cli_convert --help
```

![help cli_convert](images/lab06/help_convert.png)

**Ошибки** (нет файла и неверное расширение дают понятное сообщение и код выхода 1):

```bash
python3 -m src.lab06.cli_text cat --input nope.txt
python3 -m src.lab06.cli_convert json2csv --in data/samples/people.csv --out data/out/x.csv
```

![errors lab06](images/lab06/errors.png)

---

## [Лабораторная работа №7](src/lab07/) `ВЫПОЛНЕНА`

Поиск, сортировки и замеры времени.

### A - search.py — [src/lab07/search.py](src/lab07/search.py)

- `linear_search(nums, x)` — индекс первого вхождения или `-1`.
- `binary_search(sorted_nums, x)` — индекс или `-1`, список должен быть отсортирован.
- `two_sum_brute(nums, target)` — перебор пар.
- `two_sum_fast(nums, target)` — один проход со словарём.

`two_sum` возвращает `(i, j)` с `i < j` или `None`.

### B - sorting.py — [src/lab07/sorting.py](src/lab07/sorting.py)

`bubble_sort` (с ранним выходом), `insertion_sort`, `selection_sort`. Возвращают новый список, без `sorted`, `.sort()`, `min`, `max`.

Бонусное задание: `merge_sort` и `counting_sort(nums, lo, hi)`.

### C - check.py — [src/lab07/check.py](src/lab07/check.py)

Случайные тесты (`random.seed(42)`) сравнивают функции с эталоном.

```bash
python3 -m src.lab07.check
```

Результат: `OK: 1009 проверок`.

![check](images/lab07/check.png)

### D - bench.py — [src/lab07/bench.py](src/lab07/bench.py)

```bash
python3 -m src.lab07.bench
```

Одни и те же данные (`random.seed(42)`), замеры через `timeit`, результат в [data/lab07/bench.csv](data/lab07/bench.csv).

![bench](images/lab07/bench.png)

Примечания: квадратичные сортировки на `n = 100000` пропущены (`>60`); пара для `two_sum` стоит в конце списка (худший случай); `counting_sort` показан на диапазоне 0–1000.

### Выводы

**Пузырёк и рост n.** Пузырёк делает порядка n² операций, поэтому при росте `n` в 10 раз время растёт примерно в 100 раз (<t при 1000> сек до <t при 10000> сек). `sorted` делает n·log n, рост примерно в 12 раз.

**Бинарный поиск и сортировка.** Бинарный поиск работает только на отсортированном списке: иначе неясно, в какую половину идти. Сортировка стоит n·log n, поиск после неё log n. На 10 000 запросов: линейный <время> с, сортировка + бинарный <время> с. Сортировка окупается при многих запросах, для одного-двух проще линейный поиск.

---

## [Лабораторная работа №8](src/lab08/) `ВЫПОЛНЕНА`

Модель данных без классов: запись `Student` — обычный словарь с фиксированным набором ключей, валидация и сериализация в JSON.

### Структура записи

```python
STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")

{"fio": "Иванов Иван Иванович", "birthdate": "2007-05-14", "group": "БИВТ-26-6-1", "gpa": 4.3}
```

| Поле | Тип | Правило |
|---|---|---|
| `fio` | str | непустая строка (после `strip()`) |
| `birthdate` | str | формат `YYYY-MM-DD`, дата существует и не в будущем |
| `group` | str | непустая строка |
| `gpa` | float | число от 0 до 5; `int` допустим и приводится к `float`; `bool` не принимается |

### A - models.py — [src/lab08/models.py](src/lab08/models.py)

- `make_student(fio, birthdate, group, gpa)` — функция-конструктор: проверяет каждое поле и возвращает словарь. При плохих данных — `ValueError` с понятным сообщением (какое поле и почему).
- `validate_student(rec)` — проверяет готовый словарь: ровно `STUDENT_FIELDS` (ничего лишнего и ничего пропущенного) и значения полей.
- `student_age(rec, today=None)` — полных лет на дату `today`. Если день рождения в этом году ещё не наступил, из разности годов вычитается 1.
- `format_student(rec)` — строка вида `Иванов И.И. (БИВТ-26-6-1), 19 лет, GPA 4.30`.
- `student_to_dict(rec)` — проверяет запись и возвращает её **копию** (новый словарь).
- `student_from_dict(d)` — десериализация: берёт ровно нужные ключи (лишние игнорируются), приводит `gpa` к `float` (в том числе из строки, так приходит значение из CSV), затем валидирует.
- ★ `update_student(rec, **fields)` — возвращает **новую** запись, исходная не меняется. Неизвестный ключ — `KeyError`, неверное значение — `ValueError`.

**Дата:** формат проверяет регулярка, а существование — `date.fromisoformat` (так `2003-02-30` отклоняется).

### B - serialize.py — [src/lab08/serialize.py](src/lab08/serialize.py)

- `students_to_json(students, path)` — сохраняет массив объектов (`ensure_ascii=False`, `indent=2`).
- `students_from_json(path, policy="strict")` — читает массив, каждую запись прогоняет через `student_from_dict`.
- ★ `students_from_csv(path)` — чтение через `csv.DictReader`. `gpa` из CSV приходит строкой, превращается в `float` внутри `student_from_dict`.

**Политика обработки битых записей.** По умолчанию `strict`: первая же ошибка прерывает чтение и выбрасывает `ValueError` с номером записи и причиной. Так молча не пропускаются плохие данные. Дополнительно есть режим `policy="skip"`: битые записи пропускаются, а в консоль печатается, сколько пропущено и почему.

### Примеры JSON

До (`data/lab08/students_input.json`):

```json
[
  {"fio": "Иванов Иван Иванович", "birthdate": "2007-05-14", "group": "БИВТ-26-6-1", "gpa": 4.3},
  {"fio": "Петрова Анна Сергеевна", "birthdate": "2006-03-21", "group": "БИВТ-26-6-1", "gpa": 4.8},
  {"fio": "Сидоров Пётр Андреевич", "birthdate": "2006-11-02", "group": "БИВТ-26-6-2", "gpa": 4}
]
```

После (`data/lab08/students_output.json`): целый `gpa: 4` превратился в `4.0`.

(ВСТАВЬТЕ СЮДА ТЕКСТ ИЗ ВАШЕГО students_output.json: `cat data/lab08/students_output.json`)

Битый файл `data/lab08/students_bad.json`: у второй записи дата `2003-02-30`, у третьей `gpa = 7`.

### Запуск

```bash
python3 -m src.lab08.demo
```

**Корректные записи туда-обратно:**

![туда-обратно](images/lab08/roundtrip.png)

**Запись с неверной датой:**

![неверная дата](images/lab08/bad_date.png)

**Запись с gpa = 7:**

![gpa 7](images/lab08/bad_gpa.png)

**Битый файл: strict и skip:**

![strict и skip](images/lab08/policy.png)
