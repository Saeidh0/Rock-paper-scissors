import random
import sys
import pygame


# add transparancy
# GUI improvment
pygame.init()

screen_size = pygame.display.set_mode((800,500))
#transparency
transparency = pygame.Surface((300,38), pygame.SRCALPHA)#surface(width,height) of the area we want transperent

pygame.display.set_caption('Rock, Paper, Scissors')
icon = pygame.image.load('paw.png')
pygame.display.set_icon(icon)



background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background,(800,500))

#upload rock, paper, scissors image
rock = pygame.image.load('rock.png')
paper = pygame.image.load('paper.png')
scissors = pygame.image.load('scissors.png')

rockflip = pygame.image.load('rockflip.png')
paperflip = pygame.image.load('paperflip.png')
scissorsflip = pygame.image.load('scissorsflip.png')

font = pygame.font.Font(None, 30)

option=['rock', 'paper', 'scissors']

def logic(users_input):
   

    computer_pick = random.choice(option)

    if users_input == computer_pick:
        result = 'Tie'
    else:
        if users_input == 'rock' and computer_pick == 'scissors':
            result = 'You win'
        elif users_input == 'scissors' and computer_pick == 'paper':
            result = 'You win'
        elif users_input == 'paper' and computer_pick == 'rock':
            result = 'You win'
        else:
            result = 'Computer win'
    return computer_pick, result
        

def main():
    

    running = True
    user_input = ''
    computer_pick =''
    result = ''
    user_pick = ''

    player_wins = 0
    computer_wins = 0
    tie =0

    input_box = pygame.Rect(245,100,300,40)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    #keboard input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    choice = user_input.lower().strip()
                    if choice in option:
                        user_pick = choice

                        computer_pick, result = logic(choice)                
                        if result == 'You win':
                            player_wins +=1
                        elif result == 'Computer win':
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

# input box
        pygame.draw.rect(screen_size,(255,255,255), input_box, border_radius=15)
        
# user input
        text = font.render(user_input,True, (101,50,25))
        screen_size.blit(text,(input_box.x +10 , input_box.y +10))
# show picture based on input
        if user_pick == 'rock':
            screen_size.blit(rock,(-5,170))
        elif user_pick == 'paper':
            screen_size.blit(paper,(-5,170))
        elif user_pick == 'scissors':
            screen_size.blit(scissors,(-5,170))
# user input choice 
        user_ch_rect = pygame.Rect(50,400,300,38)
        pygame.draw.rect(transparency,(95,158,190,180), transparency.get_rect(),border_radius=15)#for transparency
        screen_size.blit(transparency,user_ch_rect)
        user_text = font.render(f'You choose: {user_pick}', True, (250,250,250))
        screen_size.blit(user_text,(user_ch_rect.x +10, user_ch_rect.y +10))

#instruction 
        instruction = font.render('Type rock, paper, or scissors and press enter: ',
        True, (101,50,25))
        screen_size.blit (instruction,(180,70))

# computer chice
        com_ch_rect = pygame.Rect(445,400,300,38)
        pygame.draw.rect(transparency,(240,128,128,180), transparency.get_rect(), border_radius = 15)
        screen_size.blit(transparency,com_ch_rect)
        computer_text = font.render(f'Computer choose: {computer_pick}', True, (250,250,250))
        screen_size.blit(computer_text,(com_ch_rect.x +10, com_ch_rect.y +10))

#show picture based on computer choice
        if computer_pick == 'rock':
            screen_size.blit(rockflip,(420,170))
        elif computer_pick == 'paper':
            screen_size.blit(paperflip,(420,170))
        elif computer_pick == 'scissors':
            screen_size.blit(scissorsflip,(420,170))
# result background
        result_background = pygame.Rect(250,450,300,38)
        pygame.draw.rect(transparency,(107,142,50,180), transparency.get_rect(), border_radius = 15)
        screen_size.blit(transparency,result_background)
#Result text
        result_text = font.render(result,True,(250,250,250),None)
        text_rect = result_text.get_rect(center = result_background.center)
        screen_size.blit(result_text,text_rect)

#score

        score_text = font.render(
            f'You: {player_wins}   Computer: {computer_wins}   Ties: {tie}',
            True,
            (101,50,25))

        screen_size.blit(score_text,(252,150))


        pygame.display.flip()

    pygame.quit()
    sys.exit()
main()