import termcolor
from termcolor import colored
import time
import random

game_numbers = ('1', '2', '3', '4')
game_sel = 'a'
game_difficulties = ('e', 'm', 'h')
game_difficulty = 'a'
lenght_game = 10
lives = 3
correct_answers = 0
#--------------------------------------------------------------------
def get_number():
    global game_difficulty
    if game_difficulty == 'e':
        number = random.randint(1,9)
    elif game_difficulty == 'm':
        number = random.randint(10,99)
    elif game_difficulty == 'h':
        number = random.randint(100,999)
    
    return number

def addiction():
    global result
    num1 = get_number()
    num2 = get_number()

    result = str(num1 + num2)

    print(f'{num1} + {num2} ?')

    return

def get_answer():
    answer = input()
    if answer == result:
        print(colored('Correct!', 'green'))
    else:
        print(colored('Wrong!', 'red'))
        remove_life()

def remove_life():
    global lives
    
    if lives > 1:
        lives=lives -1
        print('Lives remaining:', lives)
    else:
        #game over
        lives = 0
        print(colored('Game over :(', 'red'))
        
    return 

#----------------------------------------------------------------------------------------

print(colored('Welcome to the math game!','blue'))
print(colored('What game do you want to play?','blue'))
print(f'1. Additions\n2. Subtractions\n3. Products\n4. Divisions\n')

while game_sel not in game_numbers:
    game_sel = input('Type a number from 1 to 4: ')

print(colored('Select the difficulty:','blue'))
print(f'e. Easy\nm. Medium\nh. Hard\n')

while game_difficulty not in game_difficulties:
    game_difficulty = input('Type e, m or h to select the difficulty: ')

match game_sel:
    #additions
    case '1':
        print(colored('Addictions game! Get ready!','blue'))
        time.sleep(2)
        for i in range(lenght_game):
            if lives == 0 : break
            print('')
            addiction()
            get_answer()
            
