from Player import Player
import strategies
import sys

# Init player
player = Player()

# Init strategy
player.strategy = strategies.RandomStrategy()

skip = False
# Loop
while(player.play()):
	print '\n'.join(map(repr, player._grid))
	print player._score
	print '\n'
	if not skip:
		moves = raw_input("Move?")
		if(moves == 'y'):
			skip = True