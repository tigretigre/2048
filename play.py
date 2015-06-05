#!/usr/bin/env python

from Player import Player
import strategies
import sys


player = Player()

# Init strategy
player.strategy = strategies.LowerRightStrategy()

def print_status(player):
	print '\n'.join(map(repr, player._grid))


playing = True
skip = False
# Loop
while(playing):
	if not skip:
		print_status(player)
		moves = raw_input("Move?")
		if(moves == 'y'):
			skip = True
	print player._score
	print '\n'
	playing = player.play()

print_status(player)
