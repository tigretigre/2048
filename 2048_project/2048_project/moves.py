__author__ = 'cardj'

class Move(object):
    name = ''
    def __init__(self, player, name):
        self.player = player
        self.name = name

class MoveUp(Move):
    def __init__(self, player):
        super(MoveUp, self).__init__(player, 'up')

    def execute(self):
        self.player.execute("move/0")

class MoveDown(Move):
    def __init__(self, player):
        super(MoveDown, self).__init__(player, 'down')

    def execute(self):
        self.player.execute("move/2")

class MoveRight(Move):
    def __init__(self, player):
        super(MoveRight, self).__init__(player, 'right')

    def execute(self):
        self.player.execute("move/1")

class MoveLeft(Move):
    def __init__(self, player):
        super(MoveLeft, self).__init__(player, 'left')

    def execute(self):
        self.player.execute("move/3")
