# This function takes the values from the arrayslots and places it in a viewable way.
def makeGrid(nodesArray):
    for x in range(3):
        rowText = ''
        for y in range(3):
            # Combine all values from a horizontal view and print it.
            rowText = rowText + nodesArray[x][y].value
        print(rowText)


# This function grabs the choice from the player and tries to place it in the grid.
def getLocationChoice(currentMover, nodesArray):
    # Keep trying to input a valid location.
    validLocation = False
    while validLocation == False:

        # Grab the chosen value from the player
        userInput = input('Choose a position: ')

        # Check if the entered value is a digit (INT)
        if (userInput.isdigit()):
            chosenLocation = int(userInput)

            # Is the chosen location a location that exists on the grid?
            if (chosenLocation >= 10 or chosenLocation <= 0):
                print("Not a valid location! Choose a location between 1 and 9.")

            # The value is a valid location, but is it an available move?
            else:
                # This converts the 1-9 value into a value that the grid understands.
                toCalculateWith = (chosenLocation - 1) / 3
                firstKey = int(toCalculateWith)
                secondKey = int(int((toCalculateWith % 1) * 10) / 3)

                # Check if the value is filled or if it contains a free slot.
                if (nodesArray[firstKey][secondKey].value == '-'):
                    nodesArray[firstKey][secondKey].value = currentMover
                    return chosenLocation
                else:
                    print("Locatie al in gebruik!")
        else:
            print("Voer een nummer in!")


# This function is for the computer to decide on what location it wants to make its move
def letComputerDecide(nodesArray, mover):
    maximizing = False
    scores = minimax(nodesArray, mover, 0, maximizing)

    # Extract the values for easier access.
    result = scores[0]
    vertical = scores[1]
    horizontal = scores[2]

    # Show some extra debug information.
    print("Best possible score:" + str(result))
    print("Vertical:" + str(vertical))
    print("Horizontal: " + str(horizontal))

    # Make the move!
    nodesArray[vertical][horizontal].value = mover
    return horizontal, vertical

# This recursive function loops through the possible endings and sees what the minimizing or maximizing player (mover) would choose
def minimax(nodesArray, mover, depth, maximizing):
    # This commented code is some debug-code to show what it is working with at the moment.
    # print("                ")
    # print("Current mover:" + mover)
    # print("Currently, the temporary board looks like this:")
    # makeGrid(nodesArray)

    # Check if there is a winner (on the new board)
    if (checkWinner(nodesArray, False)):
        # There is a winner. # mover is the NEXT mover (AKA the previous mover won)
        if (mover == 'o'):
            return 1  # print("WINNER IS *")
        else:
            return -1  # print("WINNER IS o")
    if (isDraw(nodesArray)):
        return 0  # The game is a draw. Return a 0

    # The game is not over yet. Look at the possible moves and play each of the possibilities in minimax:
    scores = []

    # Loop through the empty slots and check the possible moves.
    for x in range(3):
        for y in range(3):
            if (nodesArray[x][y].value == '-'):

                # Create a new board where one move has been made.
                copiedBoard = nodesArray.copy()
                copiedBoard[x][y].value = mover
                # *************** This is possibly where the depth is being saved (and is extractable) ***************#
                result = [minimax(copiedBoard, swapMover(mover), depth + 1, not maximizing)]

                # Extract (and convert) the result.
                eindResultaat = result
                while type(eindResultaat[0]) is not int:
                    eindResultaat = eindResultaat[0]

                # Add one ending to the array
                result = eindResultaat
                filler = [result, x, y, depth]
                scores.append(filler)

                # Clean the board
                copiedBoard[x][y].value = '-'

    # Loop through the results to grab the best value
    bestScore = []
    if (maximizing):
        highestRating = [-2]
    else:
        highestRating = [2]

    # Loop through the possibilties and see if a new score is better than what is currently stored.
    for x in scores:
        if (maximizing and x[0][0] > highestRating[0]) or (not maximizing and x[0][0] < highestRating[0]):
            # Set the best currently known score.
            highestRating = x[0]
            bestScore = x

    # This is the best possible score.
    return bestScore

# This function check the rows, columns and diagonaly wheter the game is finished.
def checkWinner(nodesArray, showDebug):
    # Rows
    if (nodesArray[0][0].value == nodesArray[0][1].value == nodesArray[0][2].value and (
            nodesArray[0][0].value == "*" or nodesArray[0][0].value == "o")):  # top row
        if (showDebug):
            print("Winner by completing: toprow")
        winner = True
    elif (nodesArray[1][0].value == nodesArray[1][1].value == nodesArray[1][2].value and (
            nodesArray[1][0].value == "*" or nodesArray[1][0].value == "o")):  # middle row
        if (showDebug):
            print("Winner by completing: middle row")
        winner = True
    elif (nodesArray[2][0].value == nodesArray[2][1].value == nodesArray[2][2].value and (
            nodesArray[2][0].value == "*" or nodesArray[2][0].value == "o")):  # bottom row
        if (showDebug):
            print("Winner by completing: bottom row")
        winner = True

    # Columns
    elif (nodesArray[0][0].value == nodesArray[1][0].value == nodesArray[2][0].value and (
            nodesArray[0][0].value == "*" or nodesArray[0][0].value == "o")):  # left column
        if (showDebug):
            print("Winner by completing: left column")
        winner = True
    elif (nodesArray[0][1].value == nodesArray[1][1].value == nodesArray[2][1].value and (
            nodesArray[0][1].value == "*" or nodesArray[0][1].value == "o")):  # middle column
        if (showDebug):
            print("Winner by completing: middle column")
        winner = True
    elif (nodesArray[0][2].value == nodesArray[1][2].value == nodesArray[2][2].value and (
            nodesArray[0][2].value == "*" or nodesArray[0][2].value == "o")):  # right column
        if (showDebug):
            print("Winner by completing: right column")
        winner = True

    # Diagonally
    elif (nodesArray[0][0].value == nodesArray[1][1].value == nodesArray[2][2].value and (
            nodesArray[0][0].value == "*" or nodesArray[0][0].value == "o")):  # diagonal left top
        if (showDebug):
            print("Winner by completing: diagonal left top")
        winner = True
    elif (nodesArray[2][0].value == nodesArray[1][1].value == nodesArray[0][2].value and (
            nodesArray[2][0].value == "*" or nodesArray[2][0].value == "o")):  # diagonal left bottom
        if (showDebug):
            print("Winner by completing: diagonal left bottom")
        winner = True
    else:
        winner = False
    return winner

# This function checks to board if all the slots are filled AND there is no winner.
def isDraw(nodesArray):
    for x in range(3):
        for y in range(3):
            # If any slot is a dash, the game is still going.
            if (nodesArray[x][y].value == '-'):
                return False
    return True

# This function takes the current mover and switches it to the other mover.
def swapMover(mover):
    if (mover == '*'):
        mover = 'o'
    else:
        mover = '*'
    return mover
