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
    MoveDown: lambda x, y: (y, 3 - x),
    MoveUp: lambda x, y: (y, x),
    MoveRight: lambda x, y: (3 - x, y),
    MoveLeft: lambda x, y: (x, y),
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


def move_result(grid, move):
    rot = ROTATIONS[move]
    score = 0
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    zeroes = []
    for y in range(0, 4):
        row = []
        for x in range(0, 4):
            a, b = rot(x, y)
            if grid[b][a] > 0:
                row.append(grid[b][a])
        smashed = []
        while row:
            if len(row) > 1 and row[0] == row[1]:
                val = 2 * row[0]
                smashed.append(val)
                score += val
                row.pop(0)
            else:
                smashed.append(row[0])
            row.pop(0)
        for x in range(0, 4):
            a, b = rot(x, y)
            if len(smashed) > x:
                new_grid[b][a] = smashed[x]
            else:
                new_grid[b][a] = 0
                zeroes.append((a, b))
    return (new_grid, score, zeroes)


class Strategy(object):
    def registerPlayer(self, player):
        self.player = player


class LowerRightStrategy(Strategy):

    def getMove(self, grid):
        mv = next(move for move in [MoveDown, MoveRight, MoveLeft, MoveUp] if is_move_valid(grid, move))
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



