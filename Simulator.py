from Player import Player
import copy

class Simulator(Player):
	def __init__(self, grid):
		#super(Simulator, self).__init__()
		self._original_grid = grid
		self._grid = copy.deepcopy(grid)

	def play(self):
		pass

	def execute(self, command):
		if command == "move/0": # Move Up
			for i in range(1, 4):
				for j in range(0, 4):
					value = self._grid[i][j]
					for k in range(i, 0, -1):
						if self._grid[k - 1][j] == 0:
							self._grid[k - 1][j] = self._grid[k][j]
							self._grid[k][j] = 0
						elif self._grid[k - 1][j] == self._grid[k][j] and self._grid[k][j] == value:
							self._grid[k - 1][j] += self._grid[k][j]
							self._grid[k][j] = 0
						else:
							break
		elif command == "move/1": # Move Right
			for i in range(0, 4):
				for j in range(2, -1, -1):
					value = self._grid[i][j]
					for l in range(j, 3):
						if self._grid[i][l + 1] == 0:
							self._grid[i][l + 1] = self._grid[i][l]
							self._grid[i][l] = 0
						elif self._grid[i][l + 1] == self._grid[i][l] and self._grid[i][l] == value:
							self._grid[i][l + 1] += self._grid[i][l]
							self._grid[i][l] = 0
						else:
							break;
		elif command == "move/2": # Move Down
			for i in range(2, -1, -1):
				for j in range(0, 4):
					value = self._grid[i][j]
					for k in range(i, 3):
						if self._grid[k + 1][j] == 0:
							self._grid[k + 1][j] = self._grid[k][j]
							self._grid[k][j] = 0
						elif self._grid[k + 1][j] == self._grid[k][j] and self._grid[k][j] == value:
							self._grid[k + 1][j] += self._grid[k][j]
							self._grid[k][j] = 0
						else:
							break;
		elif command == "move/3": # Move Left
			for i in range(0, 4):
				for j in range(1, 4):
					value = self._grid[i][j]
					for l in range(j, 0, -1):
						if self._grid[i][l - 1] == 0:
							self._grid[i][l - 1] = self._grid[i][l]
							self._grid[i][l] = 0
						elif self._grid[i][l - 1] == self._grid[i][l] and self._grid[i][l] == value:
							self._grid[i][l - 1] += self._grid[i][l]
							self._grid[i][l] = 0
						else:
							break
	def reset(self):
		self._grid = copy.deepcopy(self._original_grid)
