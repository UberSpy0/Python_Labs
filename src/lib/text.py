import re
global casefold
global yo2e
casefold=True
yo2e=True
"е"=="ё"
"Е"=="Ё"
def normalize(t):
    if not isinstance(t, str):
        raise TypeError("TypeError")
    match casefold:
        case True:
            t = t.casefold()
        case False:
            t = t.lower()
    if yo2e:
        t = t.replace("ё", "е").replace("Ё", "Е")
    t=t.replace("\n", " ").replace("\t", " ").strip(" ").replace("  ", " ")
    t=" ".join(t.split())
    return t

def tokenize(t):
    if not isinstance(t, str):
        return "TypeError"
    return re.findall(r"\w+(?:-\w+)*", t)
def count_freq(l):
    a={}
    for i in l:
        a[i]=a.get(i, 0)+1
    return a

def top_n(s,n):
    if not isinstance(s, dict):
        return "TypeError"
    pairs = sorted(s.items())
    pairs.sort(key=lambda pair: pair[1], reverse=True)
    return pairs[:n]

if __name__=="__main__":
    # normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"

    # tokenize
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]

    # count_freq + top_n
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    assert top_n(freq, 2) == [("a",3), ("b",2)]

    # тай-брейк по слову при равной частоте
    freq2 = count_freq(["bb","aa","bb","aa","cc"])
    assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
    print("Все тесты прошли")