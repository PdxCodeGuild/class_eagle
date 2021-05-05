


# cases =============================

# this_is_snake_case - all lowercase with underscores for spaces, use for variables and functions in Python
# ThisIsTitleCaseOrPascalCase - each word starts with a capital, used for Python classes
# thisIsCamelCase - each word starts with a capital except the first one, used in JavaScript/Java/C#/etc
# this-is-kebab-case - all lowercase with hyphens for spaces, used for classes in CSS




# objects =============================
# assignment


# x: variable
# 1: int literal (literally writing the value in the source code)
# =: assignment
x = 1
y = 'hello'
print(id(x))
print(id(y))


# mutable vs immutable
# immutable types: None, boolean, int, float, string
# mutable types: list, dictionary

# one object but two variables referring to it
x = 1
y = x
print(id(x))
print(id(y))

# ints are immutable, doing x+1 creates a new object
x = 1
print(id(x))
x = x + 1
print(id(x))


# ints and strings are IMMUTABLE
x = 1
y = x
y += 1
print(x)
print(id(x))
print(y)
print(id(y))

x = 'hello'
y = x
y += 'world'
print(x)
print(id(x))
print(y)
print(id(y))

# lists are MUTABLE
x = ['a', 'b', 'c']
y = x
y.append('d') # when we modify y we're modifying x as well
print(x)
print(id(x))
print(y)
print(id(y))


# types =============================

# None, boolean, int, float, string, list

x = 1
print(type(x)) # <class 'int'>


class MyList:
    ...
my_list = MyList()
print(type(my_list))


# modules =============================

print(__name__)

import math
print(math.sqrt(4))

import random
print(random.randint(1, 10))

from random import randint
print(randint(1, 10))

from random import randint as random_integer
print(random_integer(1, 10))

import lab03_grading
print(lab03_grading.number_grade_to_letter_grade(87))

from lab03_grading import number_grade_to_letter_grade
print(number_grade_to_letter_grade(87))

# __name__ is a special variable you can access inside a module
# if the user ran the module, the value of __name__ will be __main__
# if the user imported the module, the value of __name__ will be the name of the module
# this allows you to only run certain code when the module itself is being run and not when it's imported


# comparisons =============================

x = 1
print(x == 1)
print(x != 1)


# conditionals =============================

import random
temperature = random.randint(50, 100)
if temperature > 80:
    print(f'{temperature} is hot')
elif temperature > 60:
    print(f'{temperature} is warm')
elif temperature > 40:
    print(f'{temperature} is cold')
else:
    print(f'{temperature} is freezing')


# conditionals can be used with any boolean
name = 'Bob'
is_bob = name == 'Bob'
if is_bob:
    print('its Bob')
else:
    print('its not Bob')

# while True


# functions =============================
# parameters / arguments - input, get renamed
# return - output (assigned to a variable or passed to another function)

# calling a function

print('hello world!')
print('hello world!', end='!!\n') # optional parameter

p = print
p('hello world!')


# defining a function

def increment(v):
    return v + 1

def add(a, b):
    a = increment(a)
    return a + b

print(add(5, 7))
print(add(5, add(5, 2)))


# specifying a default value for the second parameter makes it optional
def add(a, b=1):
    return a + b
print(add(5, 7)) # 12
print(add(5)) # 6


# if a function doesn't return anything, it implicitly returns None

def add(a, b):
    return a + b
c = add(5, 7)
print(c)

def add(a, b):
    a + b # not returning anything
c = add(5, 7)
print(c)

x = print('hello!') # print does not return anything either
print(x)



# strings =============================

# s1 = 'hello world!'
# s2 = "also hello world!"

age = 67
print('Bob is ' + age) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print('Bob is ' + str(age)) # concatenation
print(f'Bob is {age}') # f-string


name = 'Bob'
print(name.upper()) # the 'upper' method returns a new string, upper case


# lists =============================

nums = [1, 2, 3]
print(nums)
nums.append(4)
print(nums)

# loops =============================

x = 1
while x <= 10:
    print(x)
    x += 1

# iterate over the characters in a string
name = 'Jeremiah'
for char in name:
    print(char)

# iterate over the elements in a list
nums = [1, 2, 3, 4]
for num in nums:
    print(num)

# iterate over a range of numbers
for i in range(10):
    print(i)



# dictionaries =============================
# a collection of key-value pairs
# you can access the values using a key

d = {'name': 'Bob', 'age': 67}
print(d['name']) # Bob



