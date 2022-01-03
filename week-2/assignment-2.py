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
def maxProduct(nums):
    product = 1
    for _ in range(2):
        product *= nums.pop(nums.index(max(nums)))
    return product


print(maxProduct([5, 20, 2, 6]))
print(maxProduct([10, -20, 0, 3]))
print(maxProduct([-1, 2]))
print(maxProduct([-1, 0, 2]))


## homework 4
def twoSum(nums, target):
    iterator = enumerate(nums)
    for i, num in iterator:
        match_num = target - num
        if match_num in nums:
            return [i, nums.index(match_num)]


result = twoSum([2, 11, 7, 15], 9)
print(result)


## homework 5
def maxZeros(nums):
    nums_lt = ''.join(map(str, nums)).split('1')
    nums_len = map(lambda elem: len(elem), nums_lt)
    return max(nums_len)


print(maxZeros([0, 1, 0, 0]))
print(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]))
print(maxZeros([1, 1, 1, 1, 1]))
print(maxZeros([0, 0, 0, 1, 1]))
