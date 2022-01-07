def q_sort(data, left, right):
    if left < right:
        pivot = data[left]
        i, j = left, right

        while i < j:
            i += 1
            while i < right and data[i] < pivot: i += 1
            j -= 1
            while j >= left and data[j] > pivot: j -= 1

            if i < j:
                data[i], data[j] = data[j], data[i]
            
        data[j], data[left] = data[left], data[j] 
        q_sort(data, left, j)
        q_sort(data, j+1, right)


def maxProduct(nums):
    '''
    Time Complexity:
        O(maxProduct(nums)): 
            O(1) + O(1) + O(nlogn) + O(1) + O(n) => O(nlogn) in best-case and average-case.
            O(1) + O(1) +  O(n^2)  + O(1) + O(n) => O(n^2) in worst-case.

    reference: https://wiki.python.org/moin/TimeComplexity
    '''
    # one statement: O(1) in average-case.
    left = 0
    # len(): O(1) in average-case.
    right = len(nums)

    # quick sort algorithm:
    #    O(nlogn) in best-case and average-case.
    #    O(n^2) in worst-case.
    q_sort(nums, left, right) 

    # two statements: O(1) in average-case.
    product_1 = nums[-1] * nums[-2]
    product_2 = nums[0] * nums[1]

    # max(): O(n) in average-case.
    return max(product_1, product_2)


print(maxProduct([5, 20, 2, 6]))
print(maxProduct([10, -20, 0, 3]))
print(maxProduct([-1, 2]))
print(maxProduct([-1, 0, 2]))
print(maxProduct([-1, -2, 0]))
