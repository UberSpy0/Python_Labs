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
test1=[[3, -1, 5, 5, 0],[42],[-5,-2,-9],[],[1.5,2,2.0,-3.1]]

def unique_sorted(nums):
    if not isinstance(nums, list):
        raise TypeError("TypeError")
    return sorted(set(nums))
test2=[[3, 1, 1, 1, 3],[],[-1,-1,0,2,2],[1.0,1,2.5,2.5,0]]

def flatten(nums):
    result = []
    for n in nums:
        if isinstance(n, (list, tuple)):
            for i in n:
                result.append(i)
        else:
            return "TypeError"
    return result
test3=[[1, 2], [3, 4], [5]],[[1, 2], (3, 4, 5)],[[1], [], [2, 3]],[[1, 2], "ab"]
for i in test1:
    print(i,' --> ',min_max(i))
print("\n")
for i in test2:
    print(i,' --> ',unique_sorted(i))
print("\n")
for i in test3:
    print(i,' --> ',flatten(i))