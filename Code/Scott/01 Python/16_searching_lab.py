import random as rand

in_nums = []
list_size = 10

for i in range(list_size):
    in_nums.append(rand.randint(0, 99)) #Generates numbers between 0 and 99

def bubble_sort(nums):
    swaps = 1

    while swaps > 0: # Keep iterating until there's an iteration where nothing is swapped
        swaps = 0 
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                temp_val = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp_val

                swaps += 1 
    return nums

def linear_search(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            return i
    return None 

def binary_search(nums, val):
    nums = bubble_sort(nums)
    low_ind = 0
    high_ind = len(nums) - 1
    mid_ind = round((high_ind + low_ind) / 2)
    print(f'L: {low_ind} M: {mid_ind} H: {high_ind}')
    print(nums)

    while low_ind < high_ind:
        mid_ind = round((high_ind + low_ind) / 2)
        if nums[mid_ind] == val:
            return mid_ind
        elif val < nums[mid_ind]:
            high_ind = mid_ind
        elif val > nums[mid_ind]:
            low_ind = mid_ind
        
        print(f'L: {low_ind} M: {mid_ind} H: {high_ind}')
        print(nums)

# Linear Search Stuff
# 
# user_val = input("What number are you looking for? ")
# index_found = linear_search(in_nums, int(user_val))
# if index_found == None:
#     print(f'{user_val} is not in the list of numbers')
# else:
#     print(f'{user_val} is in index {index_found}')

# Binary Search Stuff
print(in_nums)
print(bubble_sort(in_nums))
user_val = input("What number are you looking for? ")
index_found = binary_search(in_nums, int(user_val))
print(f'{user_val} is in index {index_found}')