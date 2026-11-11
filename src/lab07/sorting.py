def bubble_sort(nums):
    """Возвращает список отсортированный пузырьком, с ранним выходом"""
    nums = list(nums)
    n = len(nums)
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        if not swapped:
            break
    return nums


def insertion_sort(nums):
    """Сортировка вставками. Возвращает новый список, а исходный не меняет"""
    nums = list(nums)
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = current
    return nums


def selection_sort(nums):
    """Сортировка выбором. Возвращает новый список, а исходный не меняет"""
    nums = list(nums)
    n = len(nums)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if nums[j] < nums[smallest]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums


def merge_sort(nums):
    """Разделяй и властвуй: разделяет на отрезки длиной 1, 2, 4, ..."""
    nums = list(nums)
    n = len(nums)
    width = 1
    while width < n:
        merged = []
        for start in range(0, n, 2 * width):
            left = nums[start:start + width]
            right = nums[start + width:start + 2 * width]
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
        nums = merged
        width *= 2
    return nums


def counting_sort(nums, lo, hi):
    """Подсчётом для целых чисел из диапазона [lo, hi]"""
    counts = [0] * (hi - lo + 1)
    for value in nums:
        if value < lo or value > hi:
            raise ValueError(f"Число {value} вне диапазона [{lo}, {hi}]")
        counts[value - lo] += 1
    result = []
    for offset in range(len(counts)):
        result.extend([lo + offset] * counts[offset])
    return result
