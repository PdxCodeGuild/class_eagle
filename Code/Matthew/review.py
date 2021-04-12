



# fundamentals ==============================================
# types and return values

# x = [1, 2, 3]
# print(type(x))
# print('x is ' + x)

# import random
# nums = [1, 2, 3, 4]
# random.shuffle(nums) # this function alters the object given as a parameter
# nums.sort() # this method alters the object on which it's called
# nums.reverse() # this method alters the object on which it's called
# print(nums)

# text = 'a, b, c'
# print(id(text))
# text = text.upper() # this method returns a new string
# print(id(text))
# print(text)
# text = text.split(', ') # this method returns a new list
# print(text)


# strings ==============================================

# '''
# comment
# comment
# comment
# '''

# text = 'hello\nworld!'
# text = '''
# hello
# world
# !!!!!
# '''
# print(text)

# print(len(text))

# print('hello world hello'.replace('hello', 'goodbye')) # goodbye world


# cont = input('would you like to continue? ').lower().strip()
# if cont == 'yes':
#     print('continuing')

#       0123456789...
# text = 'hello world!'
# i = 0
# while i < len(text):
#     print(i, text[i])
#     i += 1

# for i in range(len(text)):
#     print(i, text[i])

# for char in text:
#     print(char)


# lists ==============================================

#            0          1         2          3
fruits = ['apples', 'bananas', 'pears', 'cherries']
print(fruits[0]) # apples

for fruit in fruits:
    fruit += '!'
print(fruits)

for i in range(len(fruits)):
    fruits[i] += '!'

print(fruits)


# looping ==============================================


# print(range(10))
# print(type(range(10)))
# print(list(range(10, 100, 10)))


# for llama in range(10):
#     print(llama, end=' ')
# print()

# for llama in range(10, 20):
#     print(llama, end=' ')
# print()

# for llama in range(10, 20, 2):
#     print(llama, end=' ')
# print()

# for llama in range(10, -1, -2):
#     print(llama, end=' ')
# print()






# functions ==============================================


# isolated block of code
# with specific input (parameters/arguments)
# and specific output (return value)
# maximize code re-use
# functions should be self-contained
#   only operating on variables that were passed as parameters
#   use return for output
# side effect - when you alter variables outside a function


def add(a, b):
    c = a + b
    return c

print(add(5, 2))
d = add(5, 2)
print(d)

x = 5
y = 12
z = add(x, y)
print(z)





# data = [1, 2, 3, 4, 3, 4, 5, 4]
# output = []
# def bad_peaks():
#     for i in range(1, len(data)-1):
#         if data[i-1] < data[i] and data[i+1] < data[i]:
#             output.append(i)
#     return output

# print(bad_peaks())
# print(bad_peaks())





def peaks(data):
    output = []
    for i in range(1, len(data)-1):
        if data[i-1] < data[i] and data[i+1] < data[i]:
            output.append(i)
    return output



data = [1, 2, 3, 4, 3, 4, 5, 4]
print(peaks(data))

data2 = [5, 6, 7, 6, 7, 8, 9, 8, 7]
print(peaks(data2))














