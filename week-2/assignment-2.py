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
    q_sort(nums, 0, len(nums))
    product_1 = nums[-1] * nums[-2]
    product_2 = nums[0] * nums[1]
    return max(product_1, product_2)


print(maxProduct([5, 20, 2, 6]))
print(maxProduct([10, -20, 0, 3]))
print(maxProduct([-1, 2]))
print(maxProduct([-1, 0, 2]))
print(maxProduct([-1, -2, 0]))


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
