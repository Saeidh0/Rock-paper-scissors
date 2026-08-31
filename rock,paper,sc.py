import random

user_wins = 0
computer_wins = 0

option=['rock', 'paper', 'scissors']

while True:
    users_input= input('Type Rock/Paper/Scissors or Q to quit.').lower()
    
    if users_input =='q':
        break
    if users_input not in ['rock', 'paper', 'scissors']:
        print ("Invalid input")
        continue

    random_number = random.randint(0, 2)
    #rock:0, paper:1, scissors:2

    computer_pick = option[random_number]
    print('computer pick', computer_pick + '.')

    if users_input == 'rock' and computer_pick == 'scissors':
        print('YOU win!')
        user_wins +=1
        continue
    elif users_input == 'scissors' and computer_pick == 'paper':
        print('YOU win!')
        user_wins +=1
        continue
    elif users_input == 'paper' and computer_pick == 'rock':
        print('YOU win!')
        user_wins +=1
        continue

    else:
        print('YOU lost')
        computer_wins +=1

print("you won", user_wins,'times')
print('computer won', computer_wins, 'times')
