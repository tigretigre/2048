
import strategies
from moves import (
    MoveDown,
    MoveLeft,
    MoveRight,
    MoveUp,
)

grid = [
    [0, 2, 2, 4],
    [2, 2, 2, 2],
    [0, 2, 0, 8],
    [2, 0, 4, 8],
]

new_grid, score, zeroes = strategies.move_result(grid, MoveRight)

print '\n'.join(map(repr, new_grid))
print score
