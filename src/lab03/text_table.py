from src.lib.text import normalize, tokenize, count_freq
text = input()

words = tokenize(normalize(text))
freq = count_freq(words)
#ищем максимальное значение аттрибута слова, выбрав ключём Длину(len)
width = len(max(words, key=len) if words else exit("Без слов в предложении таблицы не будет"))
print(f"""{'Слово':<{width}} | Частота
{'-' * (width + 10)}""")
for i in freq:
    print(f"{i:<{width}} | {freq[i]}")