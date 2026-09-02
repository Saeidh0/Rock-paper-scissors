import random

# add functions to game
# add menu
# add differen modes
#side note : remove the while loop to reuse the code 



def logic():
    user_wins = 0
    computer_wins = 0
    tie = 0
    option=['rock', 'paper', 'scissors']
    while True:
        users_input= input('Type Rock/Paper/Scissors\n').lower()
        if users_input not in option:
            print ('Invalid input.')
        else:
            break    

    computer_pick = random.choice(option)
    print('computer pick', computer_pick + '.')

    if users_input == computer_pick:
        tie +=1
        print("tie")
    else:
        if users_input == 'rock' and computer_pick == 'scissors':
            print('YOU win!')
            user_wins +=1
        elif users_input == 'scissors' and computer_pick == 'paper':
            print('YOU win!')
            user_wins +=1
        elif users_input == 'paper' and computer_pick == 'rock':
            print('YOU win!')
            user_wins +=1

        else:
            print('YOU lost')
            computer_wins +=1
    return user_wins, computer_wins, tie

def single_game():
    result = logic()
    return(result)
    

def out_of_three():
    pass

def out_of_five():
    pass


# start using functions :
def menu(single_game, out_of_three, out_of_five):
    while True:
        print('\n ======[ Menu ]======')
        print('1. Single round')
        print('2. Best out of tree')
        print('3. Best out of five')
        print('5. Exit')
        print(' ====================')

        menu_choice = input('Choose an option: ').strip()
        if menu_choice == '1':
            single_game()
        else:
            print('invalid input')

        



def main():
    # this is to print the menu
    menu(single_game, out_of_three, out_of_five)


    # this is for logic
    user_wins,computer_wins,tie = logic()

    
    print('you won', user_wins,'times')
    print('computer won', computer_wins, 'times')
    print('tie', tie , 'times')

main()
