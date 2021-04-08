

# Part 1 - Convert a number grade to a letter grade, using if and elif 
# statements and comparisons. First have the user enter a number representing 
# the grade (0-100). Then convert the number grade to a letter grade.


# Part 2 - Find the specific letter grade (A+, B-, etc). You can check for 
# more specific ranges using if statements, or use modulus % to get the 
# ones-digit to set another string to '+', '-', or ' '. Then you can 
# concatenate that string with your grade string.

num = input('Enter the number grade: ')
num = int(num)

if num < 60:
    print('F')
elif num >= 60 and num < 65:
    print('D-')
elif num >= 65 and num < 70:
    print('D+')
elif num >= 70 and num < 75:
    print('C-')
elif num >= 75 and num < 80:
    print('C+')
elif num >= 80 and num < 85:
    print('B-')
elif num >= 85 and num < 90:
    print('B+')
else:
    print('A')

# print(num % 10)