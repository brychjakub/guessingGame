import random

import sys

sys.argv

def guessing_game(first, last):
    choice = ''
    number = random.randint(first, last)
    print(number)
    number_of_tries = 0

    while choice != 'no':
     try:
         choice = int(input(f'guess a nuber between {first} and {last} '))

         if number == choice:
                 number_of_tries += 1
                 choice = input(f'you win! Number of tries: {number_of_tries} wanna play again? ')
                 number = random.randint(first, last)

         else:
             number_of_tries += 1
             print(f'wrong, number of tries: {number_of_tries} try again or say no')
             continue
     except ValueError:
         print('good bye')
         break


guessing_game(1, 10)


