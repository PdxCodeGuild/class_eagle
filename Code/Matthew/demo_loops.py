


# from utilities import get_int
# age = get_int('What is your age?')
# print(f'You are {age} years old')



# def find_value(mylist, target_value):
#     i = 0
#     while i < len(mylist):
#         if mylist[i] == target_value:
#             print('found the target value')
#             break
#         i += 1
#     else:
#         print('did not find the target value')

#          0          1         2
# fruits = ['apples', 'bananas', 'pears']
# find_value(fruits, 'kiwi')


# range ==================================================

i = 0
while i < 10:
    print(i)
    i += 1

# 1 number - upper bound
for i in range(10):
    print(i)

# 2 numbers - lower bound, upper bound
for i in range(5, 10):
    print(i)

# 3 numbers - lower bound, upper bound, increment
for i in range(10, 20, 2):
    print(i)


# strings ========================================

#       012345678910
text = 'hello world'
print(text[2]) # l

i = 0
while i < len(text):
    print(i, text[i])
    i += 1

for i in range(len(text)):
    print(i, text[i])

for char in text:
    print(char)



text = 'hello world'
print(text)
for char in text:
    print(char)
    char += '!'
    print(char)
print(text)


# accumulator pattern
text = 'hello world'
output = ''
for char in text:
    print(output)
    output += char + '!'
print(output)


# lists ===============================================================

#           0            1        2        3       4        5
fruits = ['apples', 'bananas', 'pears', 'kiwi', 'mango', 'grapes']

# iterate over the indices using a while loop
i = 0
while i < len(fruits):
    print(i, fruits[i])
    i += 1

# iterate over the indices using a for loop
for i in range(len(fruits)):
    print(i, fruits[i])

# iterate over the elements directly
for fruit in fruits:
    print(fruit)

# we can't modify the element when we iterate over the elements directly
print(fruits)
for fruit in fruits:
    print(fruit)
    fruit += '!'
    print(fruit)
print(fruits)


# we can modify the element if we iterate over the indices
print(fruits)
for i in range(len(fruits)):
    # fruit = fruits[i]
    # fruit += '!'
    print(fruits[i])
    fruits[i] += '!'
    print(fruits[i])
print(fruits)











# for i in range(5, 10, 1): # 5, 6, 7, 8, 9
# for i in range(10, 5, -1): # 10, 9, 8, 7, 6


# for i in range(10, -1, -1):
#     print(i)


# 1 number - upper bound
# starts at 0, goes up to but not including that number
for i in range(10):
    print(i, end=' ') # 0...9
print()

# 2 numbers - lower bound, upper bound
# starts from the lower bound, goes up to but not including upper bound
for i in range(5, 10):
    print(i, end=' ') # 5 6 ... 9
print()

# 3 numbers - lower bound, upper bound, increment
# starts from the lower bound, goes up to but not including upper bound, steps up by the increment
for i in range(5, 20, 2):
    print(i, end=' ') # 5 7 9 ... 19
print()

for i in range(30, 100, 5):
    print(i, end=' ') # 30 35 40 45 ... 95
print()

for i in range(100, 30, -5):
    print(i, end=' ') # 100 95 90 85 ... 35
print()

for i in range(100, 29, -1):
    print(i, end=' ') # 100
print()







