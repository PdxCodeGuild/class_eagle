# Lab 3: Grading

# Part 1 - Convert a number grade to a letter grade, using if and elif 
# statements and comparisons. First have the user enter a number representing 
# the grade (0-100). Then convert the number grade to a letter grade.


# Part 2 - Find the specific letter grade (A+, B-, etc). You can check for 
# more specific ranges using if statements, or use modulus % to get the 
# ones-digit to set another string to '+', '-', or ' '. Then you can 
# concatenate that string with your grade string.

def num_to_letter_grade(num):
    grades = {
        'A': list(range(90, 100)), 
        'B': list(range(80, 90)), 
        'C': list(range(70, 80)),
        'D': list(range(60, 70)),
        'F': list(range(0, 60))
    }
    for grade in grades:
        if num in grades[grade]:
            letter = grade
    if num % 10 >= 5 or num >= 100:
        moddifier = '+'
    else:
        moddifier = '-'
    letter_grade = letter + moddifier
    return letter_grade

# def num_to_letter_grade(num):
#     letter_grade = ''
#     if num < 60:
#         letter_grade ='F'
#     elif num >= 60 and num < 65:
#         letter_grade = 'D-'
#     elif num >= 65 and num < 70:
#         letter_grade = 'D+'
#     elif num >= 70 and num < 75:
#         letter_grade = 'C-'
#     elif num >= 75 and num < 80:
#         letter_grade = 'C+'
#     elif num >= 80 and num < 85:
#         letter_grade = 'B-'
#     elif num >= 85 and num < 90:
#         letter_grade = 'B+'
#     elif num >= 90 and num < 95:
#         letter_grade = 'A-'
#     else:
#         letter_grade = 'A+'
#     return letter_grade

while True:
    num = input('Enter the number grade: ')
    num = int(num)

    print(num_to_letter_grade(num))

