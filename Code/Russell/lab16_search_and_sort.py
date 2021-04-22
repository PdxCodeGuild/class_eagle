
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def linear_search(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
    else:
        return 'not there'


print(linear_search(test_list, 7))


def binary_search(list, length, value):
    low = 0
    high = length -1
    while low <= high:
        mid = low + high // 2
        if list[mid] < value:
            low = mid + 1
        elif list[mid] > value:
            high = mid - 1

