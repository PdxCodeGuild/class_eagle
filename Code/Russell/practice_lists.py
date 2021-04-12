import random

# Average
# Write a function to find the average of a list of numbers


def average(nums):
    #     x = sum(nums)
    #     y = x / len(nums)
    #     return y
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
# print(average([1, 2, 3, 4, 5])) # 3




# Remove Empty
# Write a function to remove all empty strings from a list.


def remove_empty(mylist):
    while '' in mylist:
        mylist.remove('')
    return mylist
    
# print(remove_empty(['a', 'b', '', 'c', '', 'd'])) # ['a', 'b', 'c', 'd']





# Thanos
# Given a list, return a new list with every other element removed
# Leave the original list unchanged
def thanos(values):
    #use slicing
    return values[::2]

    #start with a blank list
    new_list = []
    #iterate over the indices of our list
    starting_index = random.randint(0, 1)
    for avenger_index in range(starting_index, len(values), 2):
        print(avenger_index)
        #access the element at the given index and add it to our new list
        new_list.append(values[avenger_index])
    return new_list
        
    

print(thanos(['Thor', 'Iron Man', 'Black Widow', 'Hulk', 'Captain America', 'Bucky', 'Spiderman', 'Scarlet Witch'])) # [2, 4]




# Half-Double
# Given a list of mumbers, halve the numbers in the first half, and double the numbers in the second half
# if there's an odd number of elements, leave the middle element unchanged
def half_double(mylist):
    ...

# print(half_double([5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # [2.5, 3, 3.5, 4.5, 22, 24, 26, 28]
# print(half_double([1, 2, 3])) # [0.5, 2, 6]




# Common Elements
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):
  ...
# print(common_elements([1, 2, 3], [2, 3, 4])) # [2, 3]