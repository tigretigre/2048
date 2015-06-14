import random
from strategies import GeneticStrategy
from Player import Player

MAX_WEIGHT = (1 << 12) - 1
NUM_BREAKS = 2

class Breeder(object):

    def start(self):
        strategies = []
        strategies.extend(self.generate_random(10))

	for j in range(0, 100):
            for strategy in strategies:
		strategy.score = 0
                for i in range(0, 10):
                    player = Player()
                    player.strategy = strategy
                    skip = True
                    while player.play():
                        if not skip:
                            moves = raw_input('Move? ')
                            if moves == 'y':
                                skip = True

                    print 'Run %d score %d' % (i, player._score)
                    strategy.score += player._score

                print 'Score %d' % strategy.score
                print 'Next strategy...'

            sorted_strategies = sorted(strategies, cmp=lambda x, y: cmp(x.score, y.score), reverse=True)
            print 'Best score: %d' % sorted_strategies[0].score
            print 'Second score: %d' % sorted_strategies[1].score
            print '\n'
            strategies = [sorted_strategies[0], sorted_strategies[1]]
            strategies.extend(self.breed(sorted_strategies[0], sorted_strategies[1], 2))
            strategies.extend(self.generate_random(2))
            strategies.append(self.mutate(strategies[4]))
            strategies.append(self.mutate(strategies[5]))
            print 'New Strategies...'

    def breed(self, candidate1, candidate2, count):
        strategies = []
        for i in range(0, count):
            breaks = []
            for i in range(0, NUM_BREAKS):
                breaks.append(random.randint(0, 255))

            sorted_breaks = sorted(breaks)
            print sorted_breaks
            new_gene_code1 = ''
            new_gene_code2 = ''
            parents = [candidate1, candidate2]
            break_index = 0
            for i in range(0, len(candidate1.gene_code)):
                if i == sorted_breaks[break_index]:
                    if parents[0] == candidate1:
                        parents[0] = candidate2
                        parents[1] = candidate1
                    else:
                        parents[0] = candidate1
                        parents[1] = candidate2
                new_gene_code1 += parents[0].gene_code[i]
                new_gene_code2 += parents[1].gene_code[i]

            print "Child 1: %s" % new_gene_code1
            print "Child 2: %s" % new_gene_code2
            strategies.append(GeneticStrategy(new_gene_code1))
            strategies.append(GeneticStrategy(new_gene_code2))

        return strategies

    def generate_random(self, count):
        strategies = []
        for i in range(0, count):
            gene_code = ''
            for j in range(0, 16):
                weight = random.randint(0, MAX_WEIGHT)
                gene_code += '{0:0>16b}'.format(weight)

            strategies.append(GeneticStrategy(gene_code))

        return strategies

    def mutate(self, strategy):
        mutate_index = random.randint(0, len(strategy.gene_code) - 1)
        new_gene_code = strategy.gene_code
        if(new_gene_code[mutate_index] == '1'):
            new_gene_code = new_gene_code[:mutate_index] + '0' + new_gene_code[mutate_index + 1:]
        else:
            new_gene_code = new_gene_code[:mutate_index] + '1' + new_gene_code[mutate_index + 1:]
        return GeneticStrategy(new_gene_code)
