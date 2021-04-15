






# Practice 5: More Practice


# Pretty Numbers
# Convert an integer into a pretty string with commas `12345678` to `12,345,678`

def pretty_number(num):
    ...
print(pretty_number(12345678)) # 12,345,678

# Pretty Bytes
# Convert a number of bytes `1567123` into a pretty form `1.5 mb`. The `round` function can take two parameters, the number and the number of decimal places to round to `print(round(1.2345, 2))` will print `1.23`.

def pretty_bytes(bytes):
    ...
print(pretty_bytes(200)) # 200 b
print(pretty_bytes(1567123)) # 1.5 mb
print(pretty_bytes(7321000000)) # 7.32 gb 

# Palindrome
# A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse. Write a function `check_palindrome(word)` which takes a string, and returns True if the string's a palindrome, or False if it's not.


def check_palindrome(word):
    ...
print(check_palindrome('racecar')) # True
print(check_palindrome('palindrome')) # False

# Anagram
# Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. `anagram` and `nag a ram`. Write another function `check_anagram(word1, word2)` that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:
# 1. Convert each word to lower case (`lower`)
# 2. Remove all the spaces from each word (`replace`)
# 3. Sort the letters of each word (`sorted`)
# 4. Check if the two are equal

def check_anagram(word1, word2):
    ...
print(check_anagram('anagram', 'nag a ram')) # True
print(check_anagram('sheep', 'goat')) # False


# Scramble Letters
# Write a function `scramble_letters` to scramble the internals letters of words, but keep first and last letter the same.

def scramble_letters(text):
    ...
print(scramble_letters('hello world!')) # hlelo wlrod!

