import random
import time

def displayIntro():
    print('You are an oath bound witch. You have sworn to emasculate any jerk that crosses your path')
    print('In front of you you see two caves. In one there is a supreme total jerk waiting to be told what is.')
    print('In the other is a bunny.')
    print()

def chooseCave():
    cave = ''
    while cave!='1' and cave!='2':
        print('Which cave will you go into? (1 or 2)')
        cave=input()

    return cave
def checkCave(chosenCave):
    print('You draw your sword and rush the cave...')
    time.sleep(2)
    print('It is dank and reeks of socks...')
    time.sleep(2)
    print('A pile of still fleshy bones writhes with maggots and....')
    print()
    time.sleep(2)

    friendlyCave=random.randint(1,2)

    if chosenCave==str(friendlyCave):
        print('you find a huge jerk passed out on a case of keystone light and totally tell him WH4T iSSSS')
    else:
        print('in a flash of white, a creature leaps out at you. You have been devoured by an evil BUNNY!')

playAgain='yes'
while playAgain=='yes' or playAgain=='y':
    displayIntro()

    caveNumber=chooseCave()

    checkCave(caveNumber)
    
    print('Do you want to play again? (yes means yes)')
    playAgain=input()
