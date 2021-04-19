


import random

# Fibonacci
# Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

def fibonacci(n):
    num1 = 0
    num2 = 1
    output = [num1, num2]
    for count in range(n-2):
        total = num1 + num2
        output.append(total)
        num1 = num2
        num2 = total
    return output

    # output = [0, 1]
    # for count in range(n-2):
    #     output.append(output[-1] + output[-2])
    # return output

#                      num1 num2  total
# print(fibonacci(10)) # [0,   1,    1,   2,    3,    5,    8,    13,    21,    34]



# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.

def find_pair(nums, target):
    output = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            # print(nums[i], nums[j])
            # if i == j:
            #     continue
            if i != j and nums[i] + nums[j] == target:
                output.append((nums[i], nums[j]))
    return output
            
# print(find_pair([5, 6, 2, 3, 4], 7)) # [5, 2]
# print(find_pair([5, 6, 2, 3], 10)) # None


# Scramble Letters
# Write a function `scramble_letters` to scramble the internal letters of words, but keep first and last letter the same.
# https://www.douglastwitchell.com/scrambled_words.php
def scramble_letters(text):
    

    # split text into a list of words ['hello', 'world']
    words = text.split(' ')
    # print(words)

    output = []

    # iterate over the words
    for word in words:
        # for i in range(1, len(word)-1):
        # print(word[1:len(word)-1])

        # take the internal letters out
        mixed_list = list(word[1:len(word)-1])
        random.shuffle(mixed_list)
        mixed_list.insert(0, word[0])
        mixed_list.append(word[len(word)-1])

        output.append(''.join(mixed_list))
        # shuffle them
        # put the word back together
    # put the text back together
    return ' '.join(output)
    
print(scramble_letters('hello world kerfuffle embiggened')) # hlelo wlrod
print(scramble_letters('this is hard to read')) # tihs is hrad to raed
print(scramble_letters('droop here most learnedly delivered adr ‘widow dido’ said as midnight fated mated dryden’s version 470 makest a blemish but that no use of milan antonio i myself you speak the king stephano 225 for i 2 scene iii 3 17 prospero master and expenses including obsolete old cock a refund if it can he be relieved by the construction seems to your ways open eyed with the dropsy drown their noses as in the project gutenberg tm license and rotten carcass of noises 130 my child hanmer 96 sir mark me and that would i have bloody thoughts pros'))
