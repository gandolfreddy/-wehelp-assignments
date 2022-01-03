def maxZeros(nums):
    nums_lt = ''.join(map(str, nums)).split('1')
    nums_len = map(lambda elem: len(elem), nums_lt)
    return max(nums_len)


print(maxZeros([0, 1, 0, 0]))
print(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]))
print(maxZeros([1, 1, 1, 1, 1]))
print(maxZeros([0, 0, 0, 1, 1]))
