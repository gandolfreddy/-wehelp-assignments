def twoSum(nums, target):
    iterator = enumerate(nums)
    for i, num in iterator:
        match_num = target - num
        if match_num in nums:
            return [i, nums.index(match_num)]


result = twoSum([2, 11, 7, 15], 9)
print(result)
