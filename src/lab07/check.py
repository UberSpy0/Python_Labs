import random

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort, merge_sort, counting_sort

counter = {"checks": 0}


def random_list(max_len, low, high):
    return [random.randint(low, high) for _ in range(random.randint(0, max_len))]


def check_sorting(fn, trials=100):
    for _ in range(trials):
        nums = random_list(50, -100, 100)
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__}: {original} -> {result}"
        assert nums == original, f"{fn.__name__} изменил исходный список {original}"
        counter["checks"] += 1


def check_search():
    #linear_search vs list.index
    for _ in range(200):
        nums = random_list(30, -20, 20)
        x = random.randint(-25, 25)
        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1
        assert linear_search(nums, x) == expected, f"linear: {nums}, x={x}"
        counter["checks"] += 1

    #бинарный поиск на отсортированных списках
    for _ in range(200):
        nums = sorted(random_list(30, -20, 20))
        x = random.randint(-25, 25)
        index = binary_search(nums, x)
        if x in nums:
            assert index != -1 and nums[index] == x, f"binary: {nums}, x={x}, index={index}"
        else:
            assert index == -1, f"binary: {nums}, x={x}, index={index}"
        counter["checks"] += 1

    #проверка на граничные случаи
    assert binary_search([], 1) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 3) == -1
    assert binary_search([1, 2], 1) == 0
    assert binary_search([1, 2], 2) == 1
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([1, 2, 3, 4, 5], 9) == -1
    assert linear_search([], 1) == -1
    counter["checks"] += 9


def check_two_sum(trials=100):
    for _ in range(trials):
        nums = random_list(30, -20, 20)
        target = random.randint(-40, 40)
        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)
        assert (brute is None) == (fast is None), f"two_sum: {nums}, target={target}"
        for pair in (brute, fast):
            if pair is not None:
                i, j = pair
                assert i < j and nums[i] + nums[j] == target, f"two_sum: {nums}, target={target}, pair={pair}"
        counter["checks"] += 1


def main():
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort, merge_sort):
        check_sorting(fn)
    check_sorting(lambda nums: counting_sort(nums, -100, 100))
    check_search()
    check_two_sum()
    print(f"OK: {counter['checks']} проверок")


if __name__ == "__main__":
    main()
