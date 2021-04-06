gradesIn = [] #Define inputs and outputs as lists
gradesOut = []
studentCount = input("How many students are you grading?: ") #get the number of students that are graded
studentCount = int(studentCount) #convert to int

def GradeConvert(a):
    a = int(a) #ensure input is an int
    gO = '' #define this output variable as str type

    if a >= 90: #convert to letter grade
        gO = 'A'
    elif a >= 80:
        gO = 'B'
    elif a >= 70:
        gO = 'C'
    elif a >= 60:
        gO = 'D'
    else:
        gO = 'F'
        
    a = a % 10 #use ones-digit to assign a + or -
    if a >= 8:
        gO = f'{gO}+'
    elif a < 5:
        gO = f'{gO}-'

    return gO


for i in range(0, studentCount): #take input for each students grade
    curStudent = input(f'Enter the numerical grade for student {i+1}: ')
    gradesIn.append(curStudent) #add it to the input list
    gradesOut.append(curStudent) #we also add it to the output lost here to make sure that both lists have the same lengths

classAvg = 0 #define class avg as a float
line = '---------------------------\n' #ease of use ascii line for formatting
print(line)
for i in range(0, studentCount): #print out each student and their number & letter grade
    gradesOut[i] = GradeConvert(gradesIn[i])
    print(f'Student {i+1}: {gradesIn[i]} | {gradesOut[i]}')
    classAvg += int(gradesIn[i]) #add last student to class avg (creates class sum)
classAvg /= studentCount #divides by number of students (creates class avg)
print(line + f'Class Avg: {classAvg} | {GradeConvert(classAvg)}') #output class avg


