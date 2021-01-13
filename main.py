print('Hello world!')

# Importing of extra files
import classes
from functions import makeGrid
from functions import getLocationChoice
from functions import letComputerDecide
from functions import checkWinner
from functions import isDraw

# Starting variables
firstMover = '*'
secondMover = 'o'
player = '*'
computer = 'o'

# Create the 9 nodes
print('Beginnen met het maken van de grid!')

# Create the grid with slots from a multi-dimensional array with accompanied nodes
nodesArray = []
for x in range(9):
    # Nodesarray requires sub-array
    nodesArray.append([])

    # Looping through horizontal
    for y in range(3):
        # Create the node and append values to the node
        myNode = classes.Node()
        myNode.value = '-'
        nodesArray[x].append(myNode)

# This is the grid if easier control of the grid is required.
nodesArray[0][0].value = '-'
nodesArray[0][1].value = '-'
nodesArray[0][2].value = '-'

nodesArray[1][0].value = '-'
nodesArray[1][1].value = '-'
nodesArray[1][2].value = '-'

nodesArray[2][0].value = '-'
nodesArray[2][1].value = '-'
nodesArray[2][2].value = '-'

# Preparations is done, let's play the game!
for x in range(9):
    # Show the current state of the game.
    print("=====================================")
    print("      Turn: " + str(x + 1) + "     ")
    print("Current grid: ")
    makeGrid(nodesArray)

    # Calculate the current Mover
    if (x % 2) == 1:
        currentMover = secondMover
    else:
        currentMover = firstMover

    # Select a node and place (if possible) a value
    if (currentMover == computer):
        # The turn of the computer
        print("Current mover is computer (" + computer + ")")
        x, y = letComputerDecide(nodesArray, computer)
        print("The AI chose location: (X:" + str(x) + ", Y: " + str(y) + ")")

    else:
        # The players turn.
        print("Current mover is player (" + player + ")")
        locationChoice = getLocationChoice(currentMover, nodesArray)
        print("The player chose location: " + str(locationChoice))

    # A move has been made. Check if the game is over.
    if (checkWinner(nodesArray, True)):  # Is there a winner?
        if (currentMover == computer):
            print("AI won.")
        else:
            print("Player won.")
        makeGrid(nodesArray)
        break
    elif (isDraw(nodesArray)):  # Is there a tie?
        print("Gelijkspel!")
        makeGrid(nodesArray)
        break
    else:  # Continue the game!
        makeGrid(nodesArray)

print('Spel is voorbij!')
