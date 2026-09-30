def transpose(m):
    if len(m) == 0:
        return []
    cols = len(m[0])
    for i in m:
        if len(i) != cols:
            return ("ValueError")
    result = []
    for j in range(cols):
        row = []
        for i in m:
            row.append(i[j])
        result.append(row)
    return result


def row_sums(m):
    if len(m) == 0:
        return []
    cols = len(m[0])
    for i in m:
        if len(i) != cols:
            return ("ValueError")
    result = []
    for i in m:
        total = 0
        for n in i:
            total += n
        result.append(total)
    return result


def col_sums(m):
    if len(m) == 0:
        return []
    cols = len(m[0])
    for i in m:
        if len(i) != cols:
            return ("ValueError")
    result = []
    for j in range(cols):
        total = 0
        for i in m:
            total += i[j]
        result.append(total)
    return result
test1=[[[1, 2, 3]],[[1], [2], [3]],[[1, 2], [3, 4]],[],[[1, 2], [3]]]
test2=[[[1, 2, 3], [4, 5, 6]],[[-1, 1], [10, -10]],[[0, 0], [0, 0]],[[1, 2], [3]]]
test3=[[[1, 2, 3], [4, 5, 6]],[[-1, 1], [10, -10]],[[0, 0], [0, 0]],[[1, 2], [3]]]
for i in test1:
    print(i,' --> ',transpose(i))
print("\n")
for i in test2:
    print(i,' --> ',row_sums(i))
print("\n")
for i in test3:
    print(i,' --> ',col_sums(i))