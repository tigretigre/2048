import math

class FitnessFunction(object):
	def score(self, grid):
		pass

class WeightedFunction(FitnessFunction):
	_weights = \
		[[ 2,  32,  512,  8192],
		 [ 4,  64, 1028, 16384],
		 [ 8, 128, 2048, 32768],
		 [16, 256, 4096, 65536]]
	def score(self, grid):
		score = 0
		for x in range(0, 4):
			for y in range(0, 4):
				if(grid[y][x] > 0):
					score = score + math.log(grid[y][x], 2) * self._weights[y][x]
		return score


class SerpentinePath(FitnessFunction):
	path_start = None

	def __init__(self, gene_code):
		last_step = None
		for y in range (3, -1, -1):
			last_step = Cell(0, y, last_step)

		for y in range(0, 4):
			last_step = Cell(1, y, last_step)

		for y in range(3, -1, -1):
			last_step = Cell(2, y, last_step)

		for y in range(0, 4):
			last_step = Cell(3, y, last_step)

		self.path_start = last_step

	def score(self, grid):
		next_step = self.path_start
		score = 0
		wildcards = 1
		while next_step and next_step.next():
			cell_value = grid[next_step.y][next_step.x]
			next_value = grid[next_step.next().y][next_step.next().x]
			if next_value == 0 and wildcards > 0:
				wildcards = wildcards - 1
			elif next_value == 0:
				break
			if cell_value == next_value:
				score = score + 3
			elif cell_value > next_value:
				score = score + 1
			else:
				break
			next_step = next_step.next()
		return score

class Cell(object):
        x = 0
        y = 0
        _next = None

        def __init__(self, x, y, next):
                self.x = x
                self.y = y
                self._next = next

        def next(self):
                return self._next
