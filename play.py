#!/usr/bin/env python

from Player import Player
import strategies
import sys

# Init player
player = Player()

# Init strategy
player.strategy = strategies.RandomStrategy()

def print_status(player):
	print '\n'.join(map(repr, player._grid))
	print player._score
	print '\n'


playing = True
skip = False
# Loop
while(playing):
	if not skip:
		print_status(player)
		moves = raw_input("Move?")
		if(moves == 'y'):
			skip = True
	playing = player.play()

print_status(player)
