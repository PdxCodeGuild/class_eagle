



# fruits1 = ['apples', 'bananas']
# fruits2 = ['pears', 'cherries']
# print(fruits1 == fruits2) # False
# print(fruits1 != fruits2) # True


# s1 = 'ab'
# s2 = 'ab'
# print(id(s1))
# print(id(s2))
# print(s1 == s2)



# identity vs equality
# identity - two variables refer to the same object
# equality - two objects have the same value

# letters1 = ['a', 'b']
# letters2 = ['a', 'b']

# print(id(letters1))
# print(id(letters2))

# print(letters1 == letters2)
# print(letters1 != letters2)


# r1 = range(10)
# r2 = range(10)
# print(id(r1))
# print(id(r2))
# print(r1 == r2)




# letters = 'abc'
# letters = letters + 'd'
# letters += 'd'
# print(letters)



# fruits = ['apple', 'banana', 'peach', 'pear']
## fruits = fruits.append('pineapple') # BAD
# fruits.append('pineapple')
# print(fruits) # ['apple', 'banana', 'peach', 'pear', 'pineapple']


# import random
# fruits = random.shuffle(fruits) # ALSO BAD
# print(fruits)



# fruits = ['apples', 'pears', 'bananas', 'pears']
# while 'pears' in fruits:
#     fruits.remove('pears')
# print(fruits) # ['apples', 'bananas']



fruits = ['apples', 'bananas', 'pears']
fruits2 = fruits.copy()
fruits2.pop()
print(fruits)
print(fruits2)



