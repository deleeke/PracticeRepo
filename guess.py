# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

lowrange=1
maxrange=20
number = random.randint(int(lowrange), int(maxrange))
print('Well, ' + myName + ', I am thinking of a number between %s and %s.'%(lowrange,maxrange))

while guessesTaken < 6:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
