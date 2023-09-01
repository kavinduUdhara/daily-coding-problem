def sum_test(nums, k):
    for num1 in range(len(nums)-1):
        for num2 in nums[num1+1:]:
            if (nums[num1] + num2 == k):
                return True
    return False
    
print(sum_test([1, 2, 3, 4, 5], 8))  # Output: True
print(sum_test([2, 4, 6, 8, 10], 7))  # Output: False
print(sum_test([7, 12, 15, 20, 25, 30], 27))  # Output: True
print(sum_test([0, 1, -1, 2, -2], 0))  # Output: True
print(sum_test([5, 10, 15, 20, 25], 50))  # Output: True
print(sum_test([10, 20, 30, 40, 50], 75))  # Output: False