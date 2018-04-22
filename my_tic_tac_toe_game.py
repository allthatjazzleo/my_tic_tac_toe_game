choices = [[],[],[]]

for numberOfChoices in range (1, 4):
    choices[0].append(str(numberOfChoices))
for numberOfChoices in range (4, 7):
    choices[1].append(str(numberOfChoices))
for numberOfChoices in range (7, 10):
    choices[2].append(str(numberOfChoices))

playerOneTurn = 1
winner = 0

def printBoard() :
    print( '\n -----')
    print( '|' + choices[0][0] + '|' + choices[0][1] + '|' + choices[0][2] + '|')
    print( ' -----')
    print( '|' + choices[1][0] + '|' + choices[1][1] + '|' + choices[1][2] + '|')
    print( ' -----')
    print( '|' + choices[2][0] + '|' + choices[2][1] + '|' + choices[2][2] + '|')
    print( ' -----\n')

while not winner :
    printBoard()

    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")
    
    
    try:
        chosenNumberOfBox = int(input("The number of box you choose to fill>> "))
        x_coordinateOfBox = int((chosenNumberOfBox - 1)%3)
        y_coordinateOfBox = int((chosenNumberOfBox - 1)/3)
    
    except:
        print("please enter a valid field")
        continue
    if choices[y_coordinateOfBox][x_coordinateOfBox] == 'X' or choices[y_coordinateOfBox][x_coordinateOfBox] == 'O':
        print("illegal move, plase try again")
        continue
    
    
    if playerOneTurn :
        choices[y_coordinateOfBox][x_coordinateOfBox] = 'X'
    else :
        choices[y_coordinateOfBox][x_coordinateOfBox] = 'O'

    playerOneTurn = not playerOneTurn

    
    # horizontal
    for y in range(3):
        for x in range(1):
            if (choices[y][x] == choices[y][x+1] and choices[y][x+1] == choices[y][x+2]):
                winner = 1
                printBoard()
    # vertical
    for x in range(3):
        for y in range(1):
            if (choices[y][x] == choices[y+1][x] and choices[y+1][x] == choices[y+2][x]):
                winner = 1
                printBoard()
    # diagonal
    if((choices[0][0] == choices[1][1] and choices[1][1] == choices[2][2]) or (choices[2][0] == choices[1][1] and choices[1][1] == choices[0][2])) :
        winner = 1
        printBoard()   
print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")

