import random
import pygame
import sys


pygame.init()

pygame.display.set_caption('Rock, Paper, Scissors')

icon = pygame.image.load('paw.png')
pygame.display.set_icon(icon)


screen_size = pygame.display.set_mode((800,500))
background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background,(800,500))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen_size.blit(background,(0,0))

# other objects should be here i.e. player, enemy. so it be at top of backgornd===========

    pygame.display.flip()

def logic():
   
    option=['rock', 'paper', 'scissors']
    while True:
        users_input= input('\nType Rock/Paper/Scissors\n').lower().strip()
        if users_input not in option:
            print ('Invalid input.')
        else:
            break    

    computer_pick = random.choice(option)
    print('computer pick', computer_pick + '.\n')

    if users_input == computer_pick:
        print('>>>[ tie ]<<<')
        return 'tie'
    else:
        if users_input == 'rock' and computer_pick == 'scissors':
            print('>>>[ YOU win! ]<<<')
            return 'player'
        elif users_input == 'scissors' and computer_pick == 'paper':
            print('>>>[ YOU win! ]<<<')
            return 'player'
        elif users_input == 'paper' and computer_pick == 'rock':
            print('>>>[ YOU win! ]<<<')
            return 'player'
        else:
            print('>>>[ YOU lost ]<<<')
            return 'computer'

def round(number_of_rounds):
    user_wins = 0
    computer_wins = 0
    tie = 0

    for i in range(number_of_rounds):
        print(f'\nRound {i+1}:')
        win = logic()

        if win == 'player':
            user_wins +=1
        elif win == 'computer':
            computer_wins +=1
        else:
            tie +=1

    summary(user_wins,computer_wins,tie)
        
def summary(user_wins,computer_wins, tie):
    print('\n-----------[ summary ]------------')
    print('Your wins:', user_wins,)
    print('computer wins:', computer_wins)
    print('ties:', tie )
    print('------------------------------------')

def menu ():
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
            round(3)
        elif menu_choice == '3':
            round(5)
        elif menu_choice == '4':
            sys.exit()
        else:
            print('invalid input')

def main():

   menu()

main()

#clean up and exit
pygame.quit()
sys.exit()