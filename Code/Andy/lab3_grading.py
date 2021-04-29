
# LAB 3: This code gives a letter grade from a number grade

print('\nGrade Calculator\n')


# Getting user input for numeric grade
grade = input ("Enter your score as an integer ")
grade = int(grade)


# Outputs depending on the inputted grade 
if grade < 0 :
    print("How did you get negative points? ")

elif grade < 60 :
    print("You received an F") 



elif grade >= 60 and grade <= 63:
    print("You received a D-")

elif grade >= 64 and grade <= 66:
    print("You received a D")

elif grade >= 67 and grade <= 69:
    print("You received a D+")



elif grade >= 70 and grade <= 73:
    print("You received a C-")

elif grade >= 74 and grade <= 76:
    print("You received a C")

elif grade >= 77 and grade <= 79:
    print("You received a C+")



elif grade >= 80 and grade <= 83:
    print("You received a B-")

elif grade >= 84 and grade <= 86:
    print("You received a B")

elif grade >= 87 and grade <= 89:
    print("You received a B+")



elif grade >= 90 and grade <= 93 :
    print("You received an A-")     

elif grade >= 94 and grade <= 96 :
    print("You received an A")       

elif grade >= 97 and grade <= 99 :
    print("You received an A+")    

elif grade == 100 :
    print("You got a perfect score! ")

elif grade >= 101 :
    print("An A and extra credit! ")


