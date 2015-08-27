__author__ = 'cardj'

import random

import moves
import math
import copy
import MySQLdb
from Simulator import Simulator


class Strategy(object):
    def registerPlayer(self, player):
        self.player = player

    def reportResults(self, new_grid, new_score):
        pass

    def reportFinalResults(self, new_grid, new_score):
        pass

class InteractiveStrategy(Strategy):

    host = ''
    user = ''
    password = ''

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        cn = None
        try:
            cn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db="game")
            cr = cn.cursor()
            cr.execute("INSERT INTO games VALUES ();")
            cr.execute("SELECT LAST_INSERT_ID();")
            ((self.id,),) = cr.fetchall()
            cn.commit()
        except:
            if cn:
                cn.rollback()
            raise
        finally:
            if cn:
                cn.close()

    def getMove(self, grid):
        self._old_grid = copy.deepcopy(grid)
        for row in grid:
	    line = '|'
            for cell in row:
                line += "{:4d}|".format(cell)
            print line
        return_value = None
        move_value = None
        repeat = True
        while(repeat):
            move = raw_input("Move?")
            repeat = False
            if move == 'h':
                return_value = moves.MoveLeft(self.player)
                move_value = 'left'
            elif move == 'j':
                return_value = moves.MoveUp(self.player)
                move_value = 'up'
            elif move == 'k':
                return_value = moves.MoveDown(self.player)
                move_value = 'down'
            elif move == 'l':
                return_value = moves.MoveRight(self.player)
                move_value = 'right'
            else:
                repeat = True
        
        self._old_move = move_value
        return return_value

    def reportResults(self, new_grid, new_score):
        if self._old_grid == new_grid:
            return
        
        # TODO: This hash function should be in a utility class somewhere.
        hash = self._hash_grid(self._old_grid)
        cn = None
        try:
            cn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="game")
            cr = cn.cursor()
            cr.execute("INSERT INTO history (game_id, hash, move, score) VALUES (%s, %s, %s, %s)", (self.id, hash, self._old_move, new_score))
            cn.commit()
        except:
            if cn:
                cn.rollback()
            raise
        finally:
            if cn:
                cn.close()

    def reportFinalResults(self, new_grid, new_score):
        cn = None
        try:
             cn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="game")
             cr = cn.cursor()
             cr.execute("UPDATE games SET score=%s WHERE id = %s", (new_score, self.id))
             cn.commit()
        except:
            if cn:
                cn.rollback()
            raise
        finally:
            if cn:
                cn.close()



    def _hash_grid(self, grid):
        hash = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                value = grid[y][x]
                if value == 0:
                    log_value = 0
                else:
                    log_value = int(math.log(value, 2))
                mult = (y & 0b10) << 4 | (x & 0b10) << 3 | (y & 0b01) << 3 | (x & 0b01) << 2
                hash |= log_value << mult
        return hash


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
