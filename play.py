from Player import Player
import strategies
import sys
import random
from Breeder import Breeder

breeder = Breeder()

breeder.start()
# Init player
#player = Player()

# Init strategy
#gene_code = ""
#for i in range(0, 16):
	#weight = random.randint(0, (1 << 16) - 1)
	#gene_code += "{0:0>16b}".format(weight)
#print gene_code
#player.strategy = strategies.GeneticStrategy(gene_code)

#skip = False
# Loop
#while(player.play()):
#	print '\n'.join(map(repr, player._grid))
#	print player._score
#	print '\n'
#	if not skip:
#		moves = raw_input("Move?")
#		if(moves == 'y'):
#			skip = True
