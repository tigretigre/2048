import random
from Breeder import Breeder
from strategies import GeneticStrategy

gene_code = ""
for i in range(0, 16):
	weight = random.randint(0, (1 << 16) - 1)
	gene_code += "{0:0>16b}".format(weight)
strategy1 = GeneticStrategy(gene_code)

gene_code = ""
for i in range(0, 16):
	weight = random.randint(0, (1 << 16) - 1)
	gene_code += "{0:0>16b}".format(weight)
strategy2 = GeneticStrategy(gene_code)

breeder = Breeder()

print breeder.breed(strategy1, strategy2)
