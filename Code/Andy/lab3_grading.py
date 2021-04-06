grade = input ("Enter your score ")

grade = int(grade)

if grade < 0 :
    print("How did you get negative points? ")

if grade < 60 :
    print ("You received an F") 

if grade >= 60 and grade <= 69:
    print ("You received a D")

if grade >= 70 and grade <= 79:
    print ("You received a C")

if grade >= 80 and grade <= 89:
    print ("You received a B")

if grade >= 90 and grade <= 99 :
    print ("You received an A")       

if grade == 100 :
    print("You got a perfect score! ")

if grade >= 101 :
    print("Extra Credit! ")