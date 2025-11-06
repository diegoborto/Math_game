import termcolor
from termcolor import colored
import time
import random
import math

game_numbers = ('1', '2', '3', '4', '5')
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

    result = float(num1 + num2)

    print(f'{num1} + {num2} ?')

    return

def subtraction():
    global result
    num1 = get_number()
    num2 = get_number()

    result = float(num1 - num2)

    print(f'{num1} - {num2} ?')

    return

def product():
    global result
    num1 = get_number()
    num2 = get_number()

    result = float(num1 * num2)

    print(f'{num1} * {num2} ?')

    return

def division():
    global result
    num1 = get_number()
    num2 = get_number()

    result = float(round(num1 / num2, 2))

    print(f'{num1} / {num2} ?')

    return

def percentages():
    global result
    num = get_number()
    perc = random.randint(1,99)

    result = float(perc/100 * num)

    print(f'{perc} % of {num} ?')

    return

def get_answer():
    answer = float(input())
    if answer == result:
        print(colored('Correct!', 'green'))
    else:
        print(colored('Wrong!', 'red'))
        print('Correct answer was:', result)
        remove_life()

def remove_life():
    global lives
    
    if lives > 1:
        lives=lives -1
        print('Lives remaining:', lives)
        print(colored('-------------------------------------------------------','red'))
    else:
        #game over
        lives = 0
        print(colored('Game over :(', 'red'))
        
    return 

#----------------------------------------------------------------------------------------
print(colored('-------------------------------------------------------','blue'))
print(colored('Welcome to the math game!','blue'))
print(colored('What game do you want to play?','blue'))
print(f'1. Additions\n2. Subtractions\n3. Products\n4. Divisions\n5. Percentages\n')

while game_sel not in game_numbers:
    game_sel = input('Type a number from 1 to 5: ')

print(colored('Select the difficulty:','blue'))
print(f'e. Easy\nm. Medium\nh. Hard\n')

while game_difficulty not in game_difficulties:
    game_difficulty = input('Type e, m or h to select the difficulty: ')

match game_sel:
    #additions
    case '1':
        print(colored('-------------------------------------------------------','blue'))
        print(colored('Addictions game! Get ready!','blue'))
        print(f'You have {lenght_game} exercises')
        time.sleep(2)
        for i in range(lenght_game):
            if lives == 0 : break
            print('')
            addiction()
            get_answer()
            
    case '2':
        #subtractions
        print(colored('-------------------------------------------------------','blue'))
        print(colored('Subtractions game! Get ready!','blue'))
        print(f'You have {lenght_game} exercises')
        time.sleep(2)
        for i in range(lenght_game):
            if lives == 0 : break
            print('')
            subtraction()
            get_answer()

    case '3':
        #products
        print(colored('-------------------------------------------------------','blue'))
        print(colored('Products game! Get ready!','blue'))
        print(f'You have {lenght_game} exercises')
        time.sleep(2)
        for i in range(lenght_game):
            if lives == 0 : break
            print('')
            product()
            get_answer()

    case '4':
        #divisions
        print(colored('-------------------------------------------------------','blue'))
        print(colored('Divisions game! Get ready! (2 decimals)','blue'))
        print(f'You have {lenght_game} exercises')
        time.sleep(2)
        for i in range(lenght_game):
            if lives == 0 : break
            print('')
            division()
            get_answer()        

    case '5':
        #Percentages
        print(colored('-------------------------------------------------------','blue'))
        print(colored('Percentages game! Get ready!','blue'))
        print(f'You have {lenght_game} exercises')
        time.sleep(2)
        for i in range(lenght_game):
            if lives == 0 : break
            print('')
            percentages()
            get_answer() 
