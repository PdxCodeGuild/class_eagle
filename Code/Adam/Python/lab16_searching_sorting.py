'''
Lab 16: Searching and Sorting
'''


import random

# Part 1 - Linear Search

def linear_search(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
        else:
            print('Value not found')


# # index 0  1  2  3  4  5  6  7
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 3)
# print(index) # 2


# Part 2 - Binary Search

def binary_search(nums, value):
    low_i = nums[0]
    high_i = nums[-1]
    while low_i < high_i:
        mid_i = nums.index(high_i)//2
        if mid_i == value:
            return nums.index(mid_i)
        elif value < mid_i:
            high_i = mid_i
            print('Value not found')
        else:
            low_i = mid_i
            print('Value not found')


# #       0  1  2  3  4  5  6  7
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = binary_search(nums, 3)
# print(index) # 2


# Part 3 - Bubble Sort

def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
  

#                      0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(nums)
print(nums)
print(bubble_sort(nums)) # [1, 2, 3, 4, 5, 6, 7, 8]  