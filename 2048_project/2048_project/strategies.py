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

# TODO: Obviously, the connection management here is terrible.
class InteractiveStrategy(Strategy):
    """
    This class provides a "strategy" in the sense that the player provides the strategy by
    playing the game interactively. This is primarily used to create a history of "good"
    gameplay for the computer to mimic.
    """

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

             self.analyzeGame()
        except:
            if cn:
                cn.rollback()
            raise
        finally:
            if cn:
                cn.close()

    def analyzeGame(self):
        # This is eventually be more complex than this.
        cn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db="game")
        cr = cn.cursor()
        cr.execute("INSERT INTO rubrics (hash, move) SELECT hash, move FROM history WHERE game_id = %s ON DUPLICATE KEY UPDATE move = VALUES(move)", (self.id,))

    def _hash_grid(self, grid):
        """
        This function is the key to this approach to the system. By employing a modified z-order hash
        for a primary key in a table "rubrics", I can encode each configuration of the grid such that
        grids with similar hashes are "substantially similar", similar enough that the moves used in
        the nearby boards are probably good moves for the board the AI is facing currently.

        Future improvements may be found in changing the ordering from z-order to a serpentine one
        more consitent with the game's strategy. Abstracting this into a utility class would aid in
        running comparative experiments with different hashing functions.
        """
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

# This inherits from RubricStrategy just to get the _hash_grid function. That should be 
#   abstracted away into a utility class
class RubricStrategy(InteractiveStrategy):
    """
    This strategy uses a modified z-order so be able to search for boards in its knowledge base that
    are "substantially similar" to the board it is currently facing, allowing the computer to learn to
    play through experience. It seems to me that this is a more reliable way for the computer to
    understand the game the attempting to create a fitness function.

    With suitable additions, this approach can lead to the computer self-learning by adjusting how the
    rubrics are built through the method analyzeGame and how to weight nearby boards (how many of the
    nearest boards to use, how to weight the results based on their distance from the current board,
    etc.)
    """

    host = ''
    user = ''
    password = ''
    _old_grid = None
    _move_index = 0

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def getMove(self, grid):
        if grid == self._old_grid:
            self._move_index += 1
        else:
            self._move_index = 0
        self._old_grid = copy.deepcopy(grid)
        for row in grid:
            line = '|'
            for cell in row:
                line += "{:4d}|".format(cell)
            print line

        hash = self._hash_grid(grid)

        cn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db="game")
        cr = cn.cursor()
        cr.execute("SELECT move, COUNT(move), SUM(diff)/COUNT(move) AS avg_diff FROM (SELECT move, CASE WHEN hash > %(hash)s THEN hash - %(hash)s ELSE %(hash)s - hash END AS diff FROM rubrics ORDER BY diff ASC LIMIT 10) closest_moves GROUP BY move ORDER BY avg_diff ASC" % {"hash": hash })
        move_counts = cr.fetchall()
	print move_counts
        move_list = []
        #for (move, count, diffs) in move_counts:
        #    move_list += [move] * count
        #move_list += ['random']
        #move = random.choice(move_list)
        if len(move_counts) <= self._move_index:
            move = 'random'
            self._move_index = 0
        else:
	    move = move_counts[self._move_index][0]
        print move
        if move == 'random':
            rand_moves = ['up', 'left', 'down', 'right']
            move = random.choice(rand_moves)
        if move == 'left':
            return_value = moves.MoveLeft(self.player)
        elif move == 'up':
            return_value = moves.MoveUp(self.player)
        elif move == 'down':
            return_value = moves.MoveDown(self.player)
        elif move == 'right':
            return_value = moves.MoveRight(self.player)
        return return_value

    def reportResults(self, grid, score):
        pass
 
    def reportFinalResults(self, grid, score):
        pass

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
