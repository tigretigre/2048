from math import log, fabs

class FitnessFunction(object):
    def score(self, grid):
        pass
    
class CountOpenSpaces(FitnessFunction):
    '''This counts the open spaces in a grid to assign a score.''' 
    def score(self, grid):
        grid_score = 0
        for row in grid:
            for space in row:
                if space == 0:
                    grid_score += 1
        return grid_score

class DiffBetweenAdjacent(FitnessFunction):
    '''This finds the difference between each score in log base 2.'''
    def score(self, grid):
        grid_score = 0
        for row_index, row in enumerate(grid):
            for column_index, space in enumerate(row):
                space_value = grid[row_index][column_index]
                log_space_value = log(space_value, 2) if space_value > 0 else 0
                for row_direction in [-1, 1]:
                    for column_direction in [-1, 1]:
                        comparison_grid_index = [row_index + row_direction, column_index + column_direction]
                        
                        if any(x in comparison_grid_index for x in [-1, 4]):
                            # checks grid out of bounds
                            continue
                        adjacent_space_value = grid[comparison_grid_index[0]][comparison_grid_index[1]]
                        log_adjacent_space_value = log(adjacent_space_value, 2) if adjacent_space_value > 0 else 0
                        grid_score += fabs(log_space_value - log_adjacent_space_value)
        return grid_score
                        
    
class DirectionalComparison(FitnessFunction):
    '''This assigns a score based on adjacency based on whether a tile is greater or equal to the next tile in a preferred direction.'''
    path_start = None
    
    def __init__(self):
        last_step = None
        for y in range(3, -1, -1):
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
                break;
            elif cell_value == next_value:
                score = score + 3
            elif cell_value > next_value:
                score = score + 1
            else:
                break
            
            next_step= next_step.next()
            
        return score
    
class WeightedPositions(FitnessFunction):
    '''This assigns a weight to each position in a grid and totals the weighted score.'''
    weights = [[2, 32, 512, 8192],
                [4, 64, 1024, 16384],
                [8, 128, 2048, 32768],
                [16, 256, 4096, 65536]]
                
    def score(self, grid):
        grid_score = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] != 0:
                    grid_score += self.weights[y][x] * log(grid[y][x], 2)
        return grid_score
        
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
