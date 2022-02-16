#!/usr/bin/python3
#This is a guess the number game
import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1, 20)
guess = ''
print('Well, ' + name + ' , I am thinking of a number between 1 and 20')

#Ask the player to guess 6 times.

print(secretNumber)

for guessTaken in range(1, 7):
    try:
        print('Take a guess.')
        print('')
        
        guess = int(input())
        if guess < secretNumber:
            print('Your guess is too low. ' + str(6 - guessTaken) + ' guess remaining')
        elif guess > secretNumber:
            print('Your guess is too high. '+ str(6 - guessTaken) + ' guess remaining')
        else:
            break #This condition is the correct guess
    except ValueError:
        print('')
        print('Opps! Sorry you did not input a number, Try again! ' + str(6 - guessTaken) + ' guess remaining')
        print('')
try:
    if guess == secretNumber:
        if guessTaken == 1:
            print('Hawda sa buang oy! Tagnaan mn dayon')
        else:
            print('Good job, ' + name + '! You guessed my number in ' + str(guessTaken) + ' guesses!')
    elif guess != int:
        print('Sorry, You did not put a valid guess')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))
except ValueError:
    print('Sorry, You did not put a valid guess')