__author__ = 'cardj'

import random

import moves


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