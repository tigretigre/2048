__author__ = 'cardj'

import random

from moves import (
    MoveDown,
    MoveLeft,
    MoveRight,
    MoveUp,
)


MOVE_LIST = [MoveUp, MoveDown, MoveLeft, MoveRight]

ROTATIONS = {
    MoveUp: lambda x, y: (y, 3 - x),
    MoveDown: lambda x, y: (y, x),
    MoveLeft: lambda x, y: (3 - x, y),
    MoveRight: lambda x, y: (x, y),
}


def is_move_valid(grid, move):
    rot = ROTATIONS[move]
    for y in range(0, 4):
        for x in range(1, 4):
            a, b = rot(x, y)
            a2, b2 = rot(x - 1, y)
            if grid[b][a] > 0 and grid[b2][a2] in [0, grid[b][a]]:
                return True
    return False    


class Strategy(object):
    def registerPlayer(self, player):
        self.player = player


class LowerRightStrategy(Strategy):

    def getMove(self, grid):
        mv = next(move for move in [MoveDown, MoveRight, MoveLeft] if is_move_valid(grid, move))
        return mv(self.player)


class RandomStrategy(Strategy):

    def getMove(self, grid):
        move = random.randint(0, 3)
        return MOVE_LIST[move](self.player)


class PatsStrategy(Strategy):
    def getMove(self, grid):
        move = 0
        while(move == 0):
            move = random.randint(0, 3)
        print "poop!"
        return MOVE_LIST[move](self.player)

#class SammysStrategy(Strategy):

#    def getMove(self, grid):
#        for move in arr:
            # What would happen?
            # Has this changed?
#            pass



