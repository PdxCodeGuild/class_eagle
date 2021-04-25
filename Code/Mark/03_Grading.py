while True:

    user_score = int(input('Please, input your score: '))

    plusminus = user_score % 10


    if user_score > 100:
        print(f'That is an incorrect input, please try again!')   
    elif user_score >= 90:
        if plusminus > 7:
            print('A+')
        elif plusminus < 2:
            print('A-')
        else:
            print('A')
    elif user_score >= 80:
        if plusminus > 7:
            print('B+')
        elif plusminus < 2:
            print('B-')
        else:
            print('B')
    elif user_score >= 70:
        if plusminus > 7:
            print('C+')
        elif plusminus < 2:
            print('C-')
        else:
            print('C')
    elif user_score >= 60:
        if plusminus > 7:
            print('D+')
        elif plusminus < 2:
            print('D-')
        else:
            print('D')
    elif user_score <= 59:
        print("F")
    
    answer = input('''
    Would you like to go again?
    [yes/no]
    ''')
    if answer == 'yes':
        continue
    else:
        break

print('Thank you!')