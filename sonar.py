# Sonar

import random
import sys

def drawBoard(board):
    # Draw the board data structure.

    hline='    ' #space for the left side of the board
    for i in range(1,6):
        hline+=(' '*9)+str(i)

    #print the numbers across the top
    print(hline)
    print('    '+('0123456789'*6))
    print()

    # print each of the 15 rows
    for i in range(15):
        # single digit numbers need to be padded with extra space
        if i<10:
            extraSpace=' '
        else:
            extraSpace=''
        print("%s%s %s %s" %(extraSpace, i, getRow(board, i),i)) 

    #print the numbers across the bottom
    print()
    print('    '+('0123456789'*6))
    print(hline)

def getRow(board, row):
   #Return a string from the board data structure at a certain row.
    boardRow=''
    for i in range(60):
        boardRow+=board[i][row]
    return boardRow
def getNewBoard():
    #Create a new 60x15 board data structure.
    board=[]
    for x in range(60): # the main list is a list of 60 lists
        board.append([])
        for y in range(15): #each list in the main list has 15 single character strings
            #use different characters for the "ocean" to make it readable
            if random.randint(0,1)==0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board
def getRandomChests(numChests):
    # Create a list of chest data structures (two item lists of (x,y) int coordinates
    chests=[]
    for i in range(numChests):
        chests.append([random.randint(0,59), random.randint(0,14)])
    return chests
def isValidMove(x,y):
    #Return True if the coordinates are on the board, otherwise False
    return x>=0 and x<=59 and y>=0 and y<=14
def makeMove(board,chests,x,y):
    #Change the board data structure with a sonar device character. Remove treasure chests
    #from the chest list as they are found. Return False if invalid move.
    #Otherwise, return string result of the move

    if not isValidMove(x,y):
        return False

    smallestDistance=100 #any chest will be closer than 100
    for cx, cy in chests:
        if abs(cx-x)>abs(cy-y):
            distance=abs(cx-x)
        else:
            distance=abs(cy-y)
        if distance<smallestDistance: #find the closest treasure chest
            smallestDistance=distance
    if smallestDistance==0:
        #Player found the treasure chest
        chests.remove([x,y])
        return 'You found a treasure chest!'
    else:
        if smallestDistance<10:
            board[x][y]=str(smallestDistance)
            return 'Treasure detected at a distance of %s from the sonar device.'%(smallestDistance)
        else:
            board[x][y]='0'
            return 'Sonar did not detect anything in range'
def enterPlayerMove():
    #Let the player input move. Return a two item list of int [x,y] coordinates
    print('Enter coordinates of next sonar device drop (0-59 0-14):')
    while True:
        move=input()
        if move.lower()=='quit':
            print('Game terminating...')
            sys.exit()

        move=move.split()
        if len(move)==2 and move[0].isdigit() and move[1].isdigit() and isValidMove(int(move[0]),int(move[1])):
            return[int(move[0]),int(move[1])]
        print('Enter a number from 0 to 59, a space,then a number from 0 to 14.')

def playAgain():
    #Returns true if player wants to play again
    print('Want to play again? (yes or no)')
    return input().lower().startswith('y')

def showInstructions():
    print('''Instructions:
You are Stikla, the time travelling pirate captain of the Likedelere. You are on the hunt for the treasure
that was thrown overboard when you wrangled your last ship. There are 3 chests lurking in the depths.
Luckily, you have 15 sonar devices you brought with you from the future.

To drop the sonar device, enter the coordinates of the point in the ocean where you wish to drop it.
The sonar devices have a range of 9 spaces.
If there is a treasure chest in range, the distance to the closest treasure chest will be displayed
where you drop the sonar device.

For example, the d below marks where the the device was dropped, and the 2's represent all distances 2 spaces away from the device.
The 4's represent the spaces 4 spaces from the the device.

    444444444
    4       4
    4 22222 4
    4 2   2 4
    4 2 d 2 4
    4 2   2 4
    4 22222 4
    4       4
    444444444

Press enter to continue...''')
    input()
    print('''For example, here is treasure chest (the c) located a distance of 2 away from the sonar device (the d):

    22222
    c   2
    2 d 2
    2   2
    22222

The point where the device was dropped will be marked with a 2.

The treasure chests don't move around. If all chests are out of range, the point will be marked with a 0.

If a device is directly dropped on the treasure chest, you have discovered the location of the chest,
and it will be collected. The sonar device will remain there.

When you collect a chest, all sonar devices will update to locate the next closest sunken treasure chest.

Press enter to continue...''')
    input()
    print()


print('T I M E  T R A V E L  P I R A T E !!!!')
print()
print('Enter "y" to view instructions, "n" to go ahead and play the game.')
if input().lower().startswith('y'):
          showInstructions()
while True:
    #game setup
    sonarDevices=16
    theBoard=getNewBoard()
    theChests=getRandomChests(3)
    drawBoard(theBoard)
    previousMoves=[]

    while sonarDevices>0:
        #start of a turn
        #show sonar device/chest status
        if sonarDevices>1: extraSsonar='s'
        else: extraSsonar=''
        if len(theChests)>1: extraSchest='s'
        else: extraSchest=''
        print('%s sonar device%s remain. %s tresure chest%s remain.'%(sonarDevices,extraSsonar,len(theChests),extraSchest))
        x,y=enterPlayerMove()
        previousMoves.append([x,y]) #append so that all moves continue to be tracked and sonar devices updated

        moveResult=makeMove(theBoard,theChests,x,y)
        if moveResult==False:
            continue
        else:
            if moveResult=='You found a treasure chest!':
            # update all sonar devices on the map.
                for x,y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)
        if len(theChests)==0:
            print('You have found all the sunken treasure!! Onward, pirate!')
            break
        sonarDevices-=1

    if sonarDevices==0:
        print("We've run out of sonar devices, cap'n!!!! About ship!")
        print()
        print('....the remaining chests were here:')
        for x,y in theChests:
            print('    %s,%s'(x,y))
    if not playAgain():
        sys.exit()
            
