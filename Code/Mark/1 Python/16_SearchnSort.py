from random import *


# example of linear search
def linear_search(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index_1 = linear_search(nums, 3)
print(nums)
print(f'Linear Search: {index_1}') # 2

# -----------------------------------------------------------------------

# binary search
def binary_search(list, n, value):
    l = 0
    r = n-1
    while l <= r:
        i = (l+r)//2
        if list[i] < value:
            l = i+1
        elif list[i] > value:
            r = i-1
        else:
            return i


# nums = [1, 2, 3, 4, 5, 6, 7, 8]
index_2 = binary_search(nums,len(nums), 3)
print('------------------------------------------------------------------')
print(nums)
print(f'Binary Search: {index_2}') # 2

# -----------------------------------------------------------------------

def bubble_sort(num_list):
    nums = len(num_list)
    swapped = True
    while swapped:
        swapped = False
        for i in range(nums-1):
            if num_list[i] > num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
                swapped = True
        if not swapped:
            return num_list
                    

nums = []
for i in range(1,10):
    nums.append(randint(1,99))
print('------------------------------------------------------------------')
print(nums)
print(f'Bubble sort: {bubble_sort(nums)}')

# -----------------------------------------------------------------------


def insertion_sort(nums):
    i = 1
    while i < len(nums):
        j=i
        while j > 0 and nums[j-1] < nums[j]:
            nums[j],nums[j-1] = nums[j-1],nums[j]
            j -= 1
        i += 1
    nums.reverse()
    return nums


nums_2 = []
for i in range(1,10):
    nums_2.append(randint(1,99))
print('------------------------------------------------------------------')
print(nums_2)
print(f'Insertion sort: {insertion_sort(nums_2)}')











