


# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"




# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

def is_even(num):
    return num%2 == 0

def even_even(nums):
    counter = 0
    for num in nums:
        if is_even(num):
            counter += 1
    return is_even(counter)
    # if is_even(counter):
    #     return True
    # else:
    #     return False

def test_even_even():
    assert even_even([5, 6, 2]) == True
    assert even_even([5, 5, 2]) == False


# Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse1(nums):
    
    x = nums.copy()
    x.reverse()
    return x

def reverse2(nums):

    # for i in range(len(output)): # 0 1 2 3 ... len(output)-1

    # if len is 3
    # i should go 2, 1, 0

    # if len is 65
    # i should go 64, 63, 62, 61, .., 1, 0
    # for  i in range(64, 64, -1)

    output = []
    # iterate over the indices in reverse order
    for i in range(len(nums)-1, -1, -1):
        # access the element from our list at that index (nums[i])
        # append the element to the end of our output list
        output.append(nums[i])
    return output

def reverse3(nums):
    output = []
    for num in nums:
        output.insert(0, num)
        # print(output)
    return output




# import string
# letters = list(string.ascii_lowercase)
# print(letters)
# print(reverse3(letters))
# print(nums)



def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]



# Factorial
# Write a function that takes `n` as a parameter and returns `n` factorial.

def factorial(n):
  ...
print(factorial(5)) # 120


# Find Unique
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.


def find_unique(nums):
    ...
nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_nums = find_unique(nums) # [12, 24, 35, 88, 120, 155]



# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.


def find_pair(nums, target):
  ...
print(find_pair([5, 6, 2, 3], 7)) # [5, 2]







# Fibonacci
# Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

def fibonacci(n):
    ...
print(fibonacci(8)) # [1, 1, 2, 3, 5, 8, 13, 21]


# Combine
# Write a function to combine two lists of equal length into one, alternating elements.


def combine(nums1, nums2):
    ...
print(combine(['a','b','c'],[1,2,3])) # ['a', 1, 'b', 2, 'c', 3]








# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

def merge(nums1, nums2):
    ...
print(merge([5,2,1], [6,8,2])) # [[5,6],[2,8],[1,2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.


def combine_all(nums):
    ...
print(combine_all([[5,2,3],[4,5,1],[7,6,3]])) # [5,2,3,4,5,1,7,6,3]







## Progressive Tax

# Income Percentage of Income
# Paid in Tax Amount of Tax
# $5,000 10%
# $50,000 25%
# $100,000 28%
# $150,000 33%
# $350,000 35%




