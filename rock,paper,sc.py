import random

user_wins = 0
computer_wins = 0
tie = 0
option=['rock', 'paper', 'scissors']

while True:
    users_input= input('Type Rock/Paper/Scissors or Q to quit.').lower()
    
    if users_input =='q':
        break
    if users_input not in ['rock', 'paper', 'scissors']:
        print ('Invalid input. Please Type Rock/Paper/Scissors')
        continue
# fix the bug when there is a tie the win goes to computer.
# add a tie tracker.
    computer_pick = random.choice(option)
    print('computer pick', computer_pick + '.')
    if users_input == computer_pick:
        tie +=1
        print("tie")
        continue
    else:
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

print('you won', user_wins,'times')
print('computer won', computer_wins, 'times')
print('tie', tie , 'times')
