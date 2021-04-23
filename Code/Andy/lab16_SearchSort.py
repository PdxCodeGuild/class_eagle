
##################  Lab 16  #######################

numbers = [1,2,3,4,5,6,7,8]

def linear_search(nums, value):
    for i in range(len(nums)):
        if nums [i] == value:
            return([i])
    else:
        return None

#print(linear_search(numbers, 3))
# [2]


def binary_search(nums, val):
    low = nums[0]
    high = nums[-1]
    while low <= high:
        mid = (low + high) // 2
        if mid < val:
            low = mid + 1
        elif mid > val:
            high = mid - 1
        else:
            return mid
            


#print(binary_search(numbers, 3))
# 3


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

#print(bubble_sort(numbers2))
# [1,2,3,4,5,6,7,8]

