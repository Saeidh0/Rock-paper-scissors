import random
import sys
import pygame


#keep the game logic for 2d version
#change the input and print sturacture based on pygame methods and functions

pygame.init()

screen_size = pygame.display.set_mode((800,500))
pygame.display.set_caption('Rock, Paper, Scissors')

icon = pygame.image.load('paw.png')
pygame.display.set_icon(icon)



background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background,(800,500))

font = pygame.font.Font(None, 40)
big_fond = pygame.font.Font(None, 60)

option=['rock', 'paper', 'scissors']

def logic(users_input):
   

    computer_pick = random.choice(option)

    if users_input == computer_pick:
        result = 'tie'
    else:
        if users_input == 'rock' and computer_pick == 'scissors':
            result = 'You WIN'
        elif users_input == 'scissors' and computer_pick == 'paper':
            result = 'You WIN'
        elif users_input == 'paper' and computer_pick == 'rock':
            result = 'You WIN'
        else:
            result = 'computer WIN'
    return computer_pick, result

'''def round(number_of_rounds):
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

    summary(user_wins,computer_wins,tie)'''
        
'''def summary(user_wins,computer_wins, tie):
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
            print('invalid input')'''

def main():
    

    running = True
    user_input = ''
    computer_pick =''
    result = ''

    player_wins = 0
    computer_wins = 0
    tie =0

    input_box = pygame.Rect(250,200,300,50)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    #keboard input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    choice = user_input.lower().strip()
                    if choice in option:

                        computer_pick, result = logic(choice)                
                        if result == 'player':
                            player_wins +=1
                        elif result == 'computer':
                            computer_wins +=1
                        else:
                            tie +=1

                        user_input =''
                    else:
                        result = 'Invalid input'

                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

                else:
                    user_input += event.unicode

#draw background
        screen_size.blit(background,(0,0))

# input boc
        pygame.draw.rect(screen_size,(255,255,255), input_box)
# user input
        text = font.render(user_input,True, (0,0,0))

        screen_size.blit(text,(input_box.x +10, input_box.y + 10))

#instruction 
        instruction = font.render('Type rock, paper, or scissors and press ENTER: ', True, (255,255,255))
        screen_size.blit (instruction,(150,150))
# conputer chice

        computer_text = font.render(f'computer: {computer_pick}', True, (255,255,255))
        screen_size.blit(computer_text,(230,300))
#Result
        result_text = font.render(
            result,
            True,
            (255, 255, 255)
        )
        screen_size.blit(result_text,(250,470))
#score
        score_text = font.render(
            f'You: {player_wins}   Computer: {computer_wins}   Ties: {tie}',
            True,
            (255, 255, 255)
        )

        screen_size.blit(
            score_text,
            (230, 520)
        )


        pygame.display.flip()



    #menu()

    pygame.quit()
    sys.exit()
main()