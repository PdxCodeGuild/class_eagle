



import random
import math


# average

def average(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    return total / len(x)
print(average([34, 56, 73, 21]))


# variance

def variance(x):
    mu = average(x)
    total = 0
    for i in range(len(x)):
        total += (x[i] - mu)**2
    return total / len(x)
print(variance([34, 56, 73, 21])) # 46.0

import math
def standard_deviation(x):
    v = variance(x)
    return math.sqrt(v)
print(standard_deviation([34, 56, 73, 21]))

# nums = []
# for i in range(100):
#     nums.append(random.randint(0, 99))


# mean = average(nums)
# print(f'Average: {mean}')
# var = variance(nums, mean)
# print(f'Variance: {var}')
# std = math.sqrt(var)
# print(f'Standard Deviation: {std}')

