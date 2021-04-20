





# for i in range(10): # 0 1 2 ... 9
# for i in range(5, 10) # 5 6 ... 9
# for i in range(5, 10, 2) # 5 7 9
# for i in range(10, 4, -2): # 10 8 6


# Practice 5: More Practice


# Pretty Numbers
# Convert an integer into a pretty string with commas `12345678` to `12,345,678`

def pretty_number(num):

    # go from the back to the front
    # insert a comma every third character

    # convert our int into a list of single-character strings
    num = str(num)
    num = list(num)
    pretty_number = []
    counter = 0
    # loop in reverse (i will go 8, 7, 6, 5, ... 2, 1, 0)
    for i in range(len(num)-1, -1, -1):
        # append the number to our output
        pretty_number.append(num[i])
        # increment our counter
        counter += 1
        # if we've gone over 3 numbers and we're not on the last iteration
        if counter == 3 and i != 0:
            # append a comma
            pretty_number.append(',')
            # reset our counter
            counter = 0
    # reverse it
    pretty_number.reverse()
    # join it
    pretty_number = ''.join(pretty_number)

    # KLUGE
    # if pretty_number[0] == ',':
    #     pretty_number = pretty_number[1:]

    return pretty_number

# https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
# def pretty_number(num):
#     return f'{num:,}'

# print(pretty_number(1))
# print(pretty_number(12))
# print(pretty_number(123))
# print(pretty_number(1234))
# print(pretty_number(12345))
# print(pretty_number(123456))
# print(pretty_number(1234567))
# print(pretty_number(1234593874509238475203489)) # 12,345,678
# print(pretty_number(12345678)) # 12,345,678
# print(pretty_number(5721)) # 5,721
# print(pretty_number(10)) # 10




# Pretty Bytes
# Convert a number of bytes `1567123` into a pretty form `1.5 mb`. The `round` function can take two parameters, the number and the number of decimal places to round to `print(round(1.2345, 2))` will print `1.23`.

def pretty_bytes(bytes):
    ...
# print(pretty_bytes(200)) # 200 b
# print(pretty_bytes(1567123)) # 1.5 mb
# print(pretty_bytes(7321000000)) # 7.32 gb 


# Palindrome
# A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse. Write a function `check_palindrome(word)` which takes a string, and returns True if the string's a palindrome, or False if it's not.


def check_palindrome(word):
    return word == word[::-1]

    word = list(word)
    reverse_word = word.copy()
    reverse_word.reverse()
    if word == reverse_word:
        return True
    else:
        return False
    
print(check_palindrome('racecar')) # True
print(check_palindrome('palindrome')) # False
print(check_palindrome('tacocat')) # True
print(check_palindrome('noon')) # True

# Anagram
# Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. `anagram` and `nag a ram`. Write another function `check_anagram(word1, word2)` that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:
# 1. Convert each word to lower case (`lower`)
# 2. Remove all the spaces from each word (`replace`)
# 3. Sort the letters of each word (`sorted`)
# 4. Check if the two are equal

def check_anagram(word1, word2):
    ...
# print(check_anagram('anagram', 'nag a ram')) # True
# print(check_anagram('sheep', 'goat')) # False


