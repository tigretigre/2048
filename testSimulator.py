from Simulator import Simulator

grid = [[2, 2, 2, 2],
	[4, 4, 4, 2],
	[8, 8, 8, 2],
	[16, 16, 16, 2]]
sim = Simulator(grid)
sim.execute("move/2")
print sim._grid
