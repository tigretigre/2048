__author__ = 'cardj'

import random

import moves
from Simulator import Simulator


class Strategy(object):
    def registerPlayer(self, player):
        self.player = player


class LowerRightStrategy(Strategy):

    def getMove(self, grid):
        return moves.MoveUp(self.player)



class RandomStrategy(Strategy):

    def getMove(self, grid):
        move = random.randint(0, 3)
        arr = [moves.MoveUp(self.player), moves.MoveDown(self.player), moves.MoveLeft(self.player), moves.MoveRight(self.player)]
        return arr[move]

class PatsStrategy(Strategy):
    def getMove(self, grid):
        arr = [moves.MoveUp(self.player), moves.MoveDown(self.player), moves.MoveLeft(self.player), moves.MoveRight(self.player)]
        move = 0
        while(move == 0):
            move = random.randint(0, 3)
        print "poop!"
        return arr[move]

#class SammysStrategy(Strategy):

#    def getMove(self, grid):
#        arr = [moves.MoveUp(self.player), moves.MoveDown(self.player), moves.MoveLeft(self.player), moves.MoveRight(self.player)]
#        for move in arr:
            # What would happen?
            # Has this changed?
#            pass

#    def is_valid(self, grid, move):

#       for x in range(1, 4): # 1 - 4 for moving right, 0 - 3 for moving left, 0 - 4 for moving up or down
#           for y in range(1, 4): # 1 - 4 for moving up, 0 - 3 fo rmoving down, 0 - 4 for moving left or right
#               if(grid[y][x] == 0 or grid_next_cell_depending_on_move == grid[y][x]):
#                   return True
#
#        return False

class GeneticStrategy(Strategy):
	score = 0
	gene_code = ""

	def __init__(self, gene_code):
		self.gene_code = gene_code
		self.weights = []
		for i in range(0, 4):
			self.weights.append([])
		for i in range(0, 16):
			gene = gene_code[i*16:i*16+16]
			weight = int(gene, 2)
			self.weights[int(i/4)].append(weight)

	def getMove(self, grid):
		# Create simulator
		simulator = Simulator(grid)
		highest_score = 0
		best_move = None

		# Do a depth-first search of the  movement space, 1 moves ahead
		move_options = [moves.MoveUp(simulator), moves.MoveRight(simulator), moves.MoveLeft(simulator), moves.MoveDown(simulator)]
		for move in move_options:
			move.execute()
			if grid != simulator._grid:
				score = self._score_grid(simulator._grid)
				if score > highest_score:
					highest_score = score
					best_move = move
				#else:
				#	print "Score too low: %s and %s" % (highest_score, score)
			#else:
			#	print "No affect on the grid"
			simulator.reset()

		best_move.player = self.player
		return best_move

	def _score_grid(self, grid):
		score = 0
		for y in range(0, len(grid)):
			for x in range(0, len(grid[y])):
				cell = grid[x][y]
				score += cell * self.weights[y][x]
		return score
