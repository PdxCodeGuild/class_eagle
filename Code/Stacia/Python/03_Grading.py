# asks the user to input their score.
score = input int("What did you score on your test?")
# result is a list that a grade and modifier will be stored in later. 
result = []

#a series of if elif logic gates that terminate with an else. 
#these logic gates find the range of the score.
if score >= 90:#the score is filtered into a range. 
    grade = ("an A") #a value is assigned to a grade.
    #result.append(grade)#the result list is appended. This step is unnessisary but remains.  
        
elif score >=80
    grade = ("a B")
    #result.append(grade)
    
elif score >=70#each elif statement isproceduarly evaluated. It will not trigger if a prior statement was triggered.
    grade = ("a C")
    #result.append(grade)

elif score  >= 60 
    grade = ("a D")
    #result.append(grade)
        
else:
    grade = ("a F") #when none of the statements trigger an f is  assigned. 
    result.append(grade)

# z = (score) #this step is unnessisary I could have taken y from the modulous of score. 

y = score %10 #score is an integer from int(input) and dose not need to be changed to a new value. mod 10 of score finds out what remains once the score is divided by 10
if score >= 7: #when the ones didget is greater than or equal to  7 it is a plus. 
    x = "+"
elif y <= 3:#when its less than or equal to three its a minus. 
    x = "-"
else:
    x = "" #other wise x is asigned a blank string

#the results are printed in an fstring
print (f"you scored {grade}{x}.") 