__author__ = 'cardj'

class Move(object):
    def __init__(self, player):
        self.player = player

class MoveUp(Move):
    def execute(self):
        self.player.execute("move/0")

class MoveDown(Move):
    def execute(self):
        self.player.execute("move/2")

class MoveRight(Move):
    def execute(self):
        self.player.execute("move/1")

class MoveLeft(Move):
    def execute(self):
        self.player.execute("move/3")
