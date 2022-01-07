## homework 1
def calculate(min, max):
    return sum(range(min, max+1))


print(calculate(1, 3)) 
print(calculate(4, 8))


## homework 2
def avg(data):
    cnt = data["count"]
    salaries_sum = sum([item["salary"] for item in data["employees"]])

    return salaries_sum/cnt

    
print(avg({
    "count": 3,
    "employees": [
        {
            "name": "John",
            "salary": 30000
        },
        {
            "name": "Bob",
            "salary": 60000
        },
        {
            "name": "Jenny",
            "salary": 50000
        }
    ]
}))


## homework 3
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


## homework 4
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


## homework 5
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
