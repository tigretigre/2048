# 2015.06.08 21:32:53 EDT
# Embedded file name: /cygdrive/c/Users/Jonathan/git/2048/Breeder.py
import random
from strategies import GeneticStrategy
from Player import Player

class Breeder(object):

    def start(self):
        strategies = []
        for j in range(0, 100):
            for i in range(0, 10):
                gene_code = ''
                for j in range(0, 16):
                    weight = random.randint(0, 65535)
                    gene_code += '{0:0>16b}'.format(weight)

                strategies.append(GeneticStrategy(gene_code))

            for strategy in strategies:
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
            strategies = self.breed(sorted_strategies[0], sorted_strategies[1])
            print 'New Strategies...'

    def breed(self, candidate1, candidate2):
        strategies = [candidate1, candidate2]
        for i in range(0, 8):
            breaks = []
            for i in range(0, 4):
                breaks.append(random.randint(0, 255))

            sorted_breaks = sorted(breaks)
            print sorted_breaks
            new_gene_code = ''
            parent = candidate1
            break_index = 0
            for i in range(0, 256):
                if i == sorted_breaks[break_index]:
                    if parent == candidate1:
                        parent = candidate2
                    else:
                        parent = candidate1
                new_gene_code += parent.gene_code[i]

            print new_gene_code
            strategies.append(GeneticStrategy(new_gene_code))

        return strategies
# okay decompyling Breeder.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.06.08 21:32:53 EDT
