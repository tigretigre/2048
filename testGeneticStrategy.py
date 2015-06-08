from strategies import GeneticStrategy
import random

gene_code = ""
for i in range(0, 16):
	weight = random.randint(0, (1 << 16) - 1)
	gene_code += "{0:0>16b}".format(weight)
print gene_code

grid = [[2, 2, 2, 2],
	[4, 4, 4, 2],
	[8, 8, 8, 2],
	[16, 16, 16, 2]]

strategy = GeneticStrategy(gene_code)
print strategy.getMove(grid)
