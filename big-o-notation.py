"""Write two Python functions to find the minimum number in a list. 
The first function should compare each number to every other number on the list. 
O(n2). 
The second function should be linear O(n)."""

def find_min_quadratic(nums):
    """
    O(n**2)
    """
    minimum = nums[0]
    for num in nums:
        # set to True
        is_smallest = True
        for num2 in nums:  # compare num to each num2
            if num > num2:
                is_smallest = False  # num is no longer the smallest
        if is_smallest:
            minimum = num  # set minimum to new smallest num
    return minimum

def find_min_linear(nums):
    """
    O(n)
    """
    minimum = nums[0]
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum

nums = [10, 33, 2, 3, 4, 5]

print(find_min_quadratic(nums))
print(find_min_linear(nums))