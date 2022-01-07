def maxZeros(nums):
    '''
    Time Complexity:
        O(maxZeros(nums)): 
            O(n) + O(n)*O(1) + O(n) + O(n)*O(1) + O(n) => O(n) in average-case.

    reference: https://wiki.python.org/moin/TimeComplexity
    '''
    # str.join(): O(n) in average-case.
    # map(): O(n) in average-case.
    # int to str casting: Normally it should be O(n^2), 
    #                     which is O(n) for division and remainder operations to find n digits, 
    #                     and O(n) for each arithmetic operation.
    #                     However the digits we have here would be whether 1 or 0, 
    #                     The time complexity might be treated as O(1).
    # split(): O(n) in average-case.
    nums_lt = ''.join(map(str, nums)).split('1')

    # map(): O(n) in average-case.
    # len(): O(1) in average-case.
    nums_len = map(lambda elem: len(elem), nums_lt)

    # max(): O(n) in average-case.
    return max(nums_len)


print(maxZeros([0, 1, 0, 0]))
print(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]))
print(maxZeros([1, 1, 1, 1, 1]))
print(maxZeros([0, 0, 0, 1, 1]))
