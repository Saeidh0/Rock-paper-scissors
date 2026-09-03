import random

# code rework
# add out of 3 to the game
# add out of 5 to the game
# add a summary function for out of three and out of five functions

def logic():
   
    option=['rock', 'paper', 'scissors']
    while True:
        users_input= input('\nType Rock/Paper/Scissors\n').lower()
        if users_input not in option:
            print ('Invalid input.')
        else:
            break    

    computer_pick = random.choice(option)
    print('computer pick', computer_pick + '.')

    if users_input == computer_pick:
        print('tie')
        return 'tie'
    else:
        if users_input == 'rock' and computer_pick == 'scissors':
            print('YOU win!')
            return 'player'
        elif users_input == 'scissors' and computer_pick == 'paper':
            print('YOU win!')
            return 'player'
        elif users_input == 'paper' and computer_pick == 'rock':
            print('YOU win!')
            return 'player'
        else:
            print('YOU lost')
            return 'computer'
        
    #since the single round is the logic code that run just once
    # there is no need to do :
    # def single round()
        #logic()    ==> instade you can just put logic as argumnet in menu input.

def out_of_three():
    user_wins = 0
    computer_wins = 0
    tie = 0
    for _ in range(3):
        win = logic()

        if win == 'player':
            user_wins +=1
        elif win == 'computer':
            computer_wins +=1
        else:
            tie +=1
    # no need to return anything. just call the funciton.=>summary()
    summary(user_wins,computer_wins,tie)
         
    
def out_of_five():
    user_wins = 0
    computer_wins = 0
    tie = 0
    for _ in range(5):
        win = logic()

        if win == 'player':
            user_wins +=1
        elif win == 'computer':
            computer_wins +=1
        else:
            tie +=1
    # no need to return anything. just call the funciton.=>summary()
    summary(user_wins,computer_wins,tie)


def summary(user_wins,computer_wins, tie):
    print('\n-----------[ summary ]------------')
    print('Your wins:', user_wins,)
    print('computer wins:', computer_wins)
    print('ties:', tie )
    print('------------------------------------')

# start using functions :
def menu (logic, out_of_three, out_of_five):
    while True:
        print('\n ======[ Menu ]======')
        print('1. Single round')
        print('2. Three round')
        print('3. Five round')
        print('4. Exit')
        print(' ====================')

        menu_choice = input('Choose an option: ').strip()
        if menu_choice == '1':
            logic()
        elif menu_choice == '2':
            out_of_three()
        elif menu_choice == '3':
            out_of_five()
        elif menu_choice == '4':
            break
        else:
            print('invalid input')

        



def main():
    # this is to print the menu
    menu(logic, out_of_three, out_of_five)



    

 

main()
