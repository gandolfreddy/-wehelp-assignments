def maxProduct(nums):
    product = 1
    for _ in range(2):
        product *= nums.pop(nums.index(max(nums)))
    return product


print(maxProduct([5, 20, 2, 6]))
print(maxProduct([10, -20, 0, 3]))
print(maxProduct([-1, 2]))
print(maxProduct([-1, 0, 2]))
