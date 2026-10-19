from src.lib.text import normalize, tokenize, count_freq, top_n

text = input()

words = tokenize(normalize(text))
freq = count_freq(words)
width = len(max(words, key=len) if words else exit("Без слов в предложении таблицы не будет"))
print(f"Всего слов: {len(words)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")
for word, count in top_n(freq, 5):
    print(f"{word}:{count}")