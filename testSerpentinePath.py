from fitness import (SerpentinePath, WeightedFunction)

serpentine_function = SerpentinePath("gene code")
weight_function = WeightedFunction()
grid1 = [[0, 0, 0, 2],
	[0, 0, 0, 4],
	[0, 0, 0, 16],
	[0, 0, 0, 32]]

grid2 = [[0, 0, 0, 16],
	[0, 0, 0, 8],
	[0, 0, 0, 4],
	[0, 0, 0, 2]]

print serpentine_function.score(grid1)
print serpentine_function.score(grid2)
print

print weight_function.score(grid1)
print weight_function.score(grid2)
