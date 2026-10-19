def min_max(nums):
    if len(nums)==0:
        return "ValueError"
    minv = maxv= nums[0]
    for num in nums:
        if num < minv:
            minv = num
        elif num > maxv:
            maxv = num
    return tuple([minv, maxv])

def unique_sorted(nums):
    if not isinstance(nums, list):
        raise TypeError("TypeError")
    return sorted(set(nums))

def flatten(nums):
    result = []
    for n in nums:
        if isinstance(n, (list, tuple)):
            for i in n:
                result.append(i)
        else:
            return "TypeError"
    return result

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
