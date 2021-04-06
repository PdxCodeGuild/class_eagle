
user_score = input('What is your score?')

user_score = int(user_score)

if user_score > 90:
    grade = "A"

elif user_score > 80:
    grade = "B" 

elif user_score > 70:
    grade = "C" 

elif user_score > 60: 
    grade = "D" 

elif user_score <= 59:
    grade = "F"

modifier = user_score % 10 

if modifier >= 7:
    mod = "+"

elif modifier <= 3:
    mod = "-"

    
print(f"You got an {grade}{mod}")




