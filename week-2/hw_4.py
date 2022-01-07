def twoSum(nums, target):
    '''
    Time Complexity:
        O(twoSum(nums, target)): 
            O(n) + O(n)*(O(1))+O(n)) + O(1)+O(n)*O(n) => O(n^2) in average-case.

    reference: https://wiki.python.org/moin/TimeComplexity
    '''
    # enumerate(): For returning an enumeration object, 
    #              its time complexity is going to depend on how it's used.
    #              In this case, it should be O(n) because of returning all the elements.
    iterator = enumerate(nums)

    # for loop iteration: O(n) in this case
    for i, num in iterator:
        # one statement: O(1) in average-case.
        match_num = target - num

        # x in s: O(n) in average-case.
        if match_num in nums:
            # list.index(): O(n) in average-case
            return [i, nums.index(match_num)]


result = twoSum([2, 11, 7, 15], 9)
print(result)
