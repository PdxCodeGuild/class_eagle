
##################  Lab 16  #######################

numbers = [1,2,3,4,5,6,7,8]


# Linear search iterates through a list and either returns a match or none
def linear_search(nums, value):
    for i in range(len(nums)):
        if nums [i] == value:
            return([i])
    else:
        return None
#test
#print(linear_search(numbers, 3))
# [2]



# Binary search divides range in half until target is found
def binary_search(nums, n, val):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < val:
            low = mid + 1
        elif nums[mid] > val:
            high = mid - 1
        else:
            return mid
#test
#print(binary_search(numbers,len(numbers), 3))
# 2



# Bubble sort compares the current indice to the next one and swaps if needed
def bubble_sort(nums):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                switch = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = switch
                swapped = True
    return nums


numbers2 = [8,7,6,5,4,3,2,1]
print(bubble_sort(numbers2))
# [1,2,3,4,5,6,7,8]

