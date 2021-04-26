while True:
    # getting the users score
    user_score = int(input('Input your score: '))
    
    
    # if's and elif's to evaluate the score
    if user_score > 100:
        # added this to ensure that the user doesn't enter an invalid score
        print('There was no extra credit offered, so that score is impossible! Please re-enter your score.')
        continue
    elif user_score >= 90:
        user_grade = 'A'
    elif user_score >= 80:
        user_grade = 'B'
    elif user_score >= 70:
        user_grade = 'C'
    elif user_score >= 60:
        user_grade = 'D'
    elif user_score <= 59:
        user_grade = 'F'

    # using modulus to determine the grade mod "+" or "-"
    plusminus = user_score % 10
    if plusminus > 7:
            grade_mod = '+'
    elif plusminus < 3:
            grade_mod = '-'
    else:
        grade_mod = ""

    # presenting the user there score with the applicable grade mod
    if user_score != 100 and user_score > 59:
        print(f'Your grade is: {user_grade}{grade_mod}')
    elif user_score == 100:
        print('Your grade is: A+')
    else:
        print('Your grade is: F')
    
    # checking to see if they would like to do another score
    answer = input('Would you like to go again?')
    if answer != 'yes':
        break

print('Thank you!')