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


# index 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
value = random.choice(nums)
print(value)
index = linear_search(nums, value)
print(f'{index}\n')


# Part 2 - Binary Search

def binary_search(nums, value):
    low = 0
    high = len(nums) -1
    while low <= high:
        mid = (low + high)//2
        if value < mid:
            high = mid - 1
            print('Value not found')
        elif value > mid:
            low = mid + 1
            print('Value not found')
        else:
            return mid


#       0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
value = random.choice(nums)
print(value)
num = binary_search(nums, value)
print(f'{num}\n')



# Part 3 - Bubble Sort

def bubble_sort(nums):
    n = len(nums)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i - 1]
                swapped = True
    return nums

#       0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(nums)
print(nums)
print(f'{bubble_sort(nums)}\n') # [1, 2, 3, 4, 5, 6, 7, 8]


# Part 4 - Insertion Sort

