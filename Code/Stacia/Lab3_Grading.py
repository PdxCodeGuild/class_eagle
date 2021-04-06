
grade=()
enter_score = input ("What did you score on your test?")
score =int(enter_score)
result =[]

if score >= 90:
    grade = ("an A")
    result.append(grade)
        
elif score >=80 and score  <90:
    grade = ("a B")
    result.append(grade)
    
elif score >=70 and score  <80:
    grade = ("a C")
    result.append(grade)
elif score  >= 60 and score <70:
        result.append(grade)
        
else:
    grade=("a F")
    result.append(grade)

z=(score)

y= z %10
if y>=7:
    x="+"
elif y<3:
    x="-"
else:
    x= " "

print (f"you scored {grade}{x}.")