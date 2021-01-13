# This file exists to provide a locationslot for the tic-tac-toe game.
class Node:
	# value is here to provide a value for the current spot.
	value = ''
	index = 0
	
	# We need to find a way to store the previous and next node. That way, we can keep track of where certain values and nodes are. It enables the usage of making loops through the nodes.
	up = '' # Next node
	down = '' # Previous node

	vertical = ''
	horizontal = ''