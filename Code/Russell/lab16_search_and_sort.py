
test_list = [1, 2, 3, 4, 5, 6, 7, 8, ]

# def linear_search(nums, value):
#     for i in range(len(nums)):
#         if nums[i] == value:
#             return i
#     else:
#         return 'not there'


# print(linear_search(test_list, 7))

# nums = [8, 6, 7, 4, 5, 2, 1, 3]


def binary_search(list_a, value):
    length = len(list_a)
    low = 0
    high = length -1
    while low <= high:
        mid = (low + high) // 2
        if list_a[mid] < value:
            low = mid + 1
        elif list_a[mid] > value:
            high = mid - 1
        else:
            return mid
    return 'unsuccessful' 
# #REMEMBER (PEMDAS) line 21. 

index = binary_search(test_list, 3)

print(f'binary search: {index}')
# test_list = [2, 1, 5, 6]


# the swapped variable should be True initially, and any time you swap two variables in your list
# the first line of the loop, we set swapped to False
# inside the conditional (where we find a pair out of order) we set swapped to True (meaning we did find a pair that was out of order)


def bubble_sort(a_list):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(1,len(a_list)):
            if a_list[i-1] > a_list[i]:
                a_list[i-1] , a_list[i] = a_list[i] , a_list[i-1]
                swapped = True
    return a_list
        


# print(bubble_sort(nums))



# procedure bubbleSort(A : list of sortable items)
#     n := length(A)
#     repeat
#         swapped = false
#         for i := 1 to n - 1 inclusive do
#             /* if this pair is out of order */
#             if A[i - 1] > A[i] then
#                 /* swap them and remember something changed */
#                 swap(A[i - 1], A[i])
#                 swapped := true
#             end if
#         end for
#     until not swapped
# end procedure