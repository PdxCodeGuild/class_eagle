gradesIn = []
gradesOut = []
studentCount = input("How many students are you grading?: ")
studentCount = int(studentCount)

def GradeEnter():
    for i in range(0, studentCount):
        curStudent = input(f'Enter the numerical grade for student {i+1}: ')
        gradesIn.append(curStudent)
        gradesOut.append(curStudent)

def GradeConvert(a):
    curStudent = int(a)
    gO = ''

    if curStudent >= 90:
        gO = 'A'
    elif curStudent >= 80:
        gO = 'B'
    elif curStudent >= 70:
        gO = 'C'
    elif curStudent >= 60:
        gO = 'D'
    else:
        gO = 'F'
        
    curStudent = curStudent % 10
    if curStudent >= 8:
        gO = f'{gO}+'
    elif curStudent < 5:
        gO = f'{gO}-'

    return gO



GradeEnter()
classAvg = 0
line = '---------------------------\n'
print(line)
for i in range(0, studentCount):
    gradesOut[i] = GradeConvert(gradesIn[i])
    print(f'Student {i+1}: {gradesIn[i]} | {gradesOut[i]}')
    classAvg += int(gradesIn[i])
classAvg /= studentCount
print(line + f'Class Avg: {classAvg} | {GradeConvert(classAvg)}')