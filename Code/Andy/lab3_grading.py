grade = input ("Enter your score as an integer ")

grade = int(grade)

if grade < 0 :
    print("How did you get negative points? ")

if grade < 60 :
    print ("You received an F") 



if grade >= 60 and grade <= 63:
    print ("You received a D-")

if grade >= 64 and grade <= 66:
    print ("You received a D")

if grade >= 67 and grade <= 69:
    print ("You received a D+")



if grade >= 70 and grade <= 73:
    print ("You received a C-")

if grade >= 74 and grade <= 76:
    print ("You received a C")

if grade >= 77 and grade <= 79:
    print ("You received a C+")



if grade >= 80 and grade <= 83:
    print ("You received a B-")

if grade >= 84 and grade <= 86:
    print ("You received a B")

if grade >= 87 and grade <= 89:
    print ("You received a B+")



if grade >= 90 and grade <= 93 :
    print ("You received an A-")     

if grade >= 94 and grade <= 96 :
    print ("You received an A")       

if grade >= 97 and grade <= 99 :
    print ("You received an A+")    

if grade == 100 :
    print("You got a perfect score! ")

if grade >= 101 :
    print("An A and extra credit! ")


