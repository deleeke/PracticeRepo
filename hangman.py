import random
HANGMANPICS = ['''

 +---+
 |   |
     |
     |
     |
     |
========''','''

 +---+
 |   |
 O   |
     |
     |
     |
========''','''

 +---+
 |   |
 O   |
 |   |
     |
     |
========''','''

 +---+
 |   |
 O   |
/|   |
     |
     |
========''','''

 +---+
 |   |
 O   |
/|\  |
     |
     |
========''','''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
========''','''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========''','''
 
+---+
 |   |
 O/  |
/|   |
/ \  |
     |
========''','''

+---+
 |   |
\O/  |
 |   |
/ \  |
     |
========''','''

+---+
 |   |
\O/  |
 |/  |
/    |
     |
========''','''

+---+
 |   |
\O/  |
\|/  |
     |
     |
========''','''

 +---+
 |   |
 X   |
/|\  |
/ \  |
     |
========''']
words ={'Animals':'ant baboon badger bat bear beaver camel cat cattle clam cobra cougar coyote crow deer dog donkey eagle ferret fox frog'.split(),
        'Colors':'blue green indigo yellow orange teal red pink violet white black purple brown'.split(),
        'Shapes':'triangle ellipse rhombus trapezoid octagon pentagon septagon parallelogram square chevron'.split(),
        'Fruits':'watermelon kiwi guava mango strawberry blueberry blackberry cherry apple orange grapefruit grape lemon lime'.split()}

def getRandomWord(wordDict):
    #this function returns a random string from the passed dictionary of lists of strings, and the key also
    #First, randomly select a key from the dictionary:
    wordKey=random.choice(list(wordDict.keys()))
    #Second, randomly select a word from the key's list in the dictionary
    wordIndex = random.randint(0,len(wordDict[wordKey])-1)
    return [wordDict[wordKey][wordIndex],wordKey]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks= '_' * len(secretWord)

    for i in range(len(secretWord)):# replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i]+secretWord[i]+blanks[i+1:]

    for letter in blanks: #show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #Returns the letter the player entered. This funciton makes sure the player entered a single letter, and not something else
    while True:
        print('Guess a letter.')
        guess=input()
        guess=guess.lower()
        if len(guess) !=1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You allready guessed that letter. Guess again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess
def playAgain():
    # This funtion returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters=''
correctLetters=''
secretWord, secretKey=getRandomWord(words)
gameIsDone=False

while True:
    print('The secret word is in the set: '+secretKey)
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    #Let the player type in a letter
    guess=getGuess(missedLetters+correctLetters)

    if guess in secretWord:
        correctLetters=correctLetters+guess

        #Check if the player has won
        foundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False
                break
        if foundAllLetters:
            print('Yes! the secret word is "'+secretWord+'"! YOU HAVE WON!!!')

            gameIsDone=True
    else:
        missedLetters=missedLetters+guess

        #check if player has guessed too many times and lost
        if len(missedLetters)==len(HANGMANPICS)-1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter '+str(len(missedLetters))+' missed guesses and '+str(len(correctLetters))+' correct guesses, the word was"'+secretWord+'"')
            gameIsDone=True

        #Ask the player if they want to play again (but only if the game is done)
    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            gameIsDone=False
            secretWord,secretKey=getRandomWord(words)
        else:
            break
        
