const INTERVAL = 2000

angular.module('2048', ['ngAnimate'])
.controller('board', function($scope, $http, $interval) {
    $scope.tiles = []
    var old_grid = null;
    set_grid(grid);

    promise = $interval(function() {
        $http({method: "GET", url: '/ajax/get-move'}).
            then(function(response) {
                set_grid(response.data.grid, response.data.move);
                grid = response.data.grid;
            });
        //$interval.cancel(promise);
    },
    INTERVAL);

    function set_grid(new_grid, direction) {
        if(direction == null || direction == 'left' || direction == 'right') {
            $scope.tiles = [];
            new_grid.forEach(function(row, row_index, array) {
                row.forEach(function(cell, cell_index, row) {
                    if(cell != 0) {
                        $scope.tiles.push({"value": cell, x: cell_index, y: row_index, "visible": true});
                    }
                });
            });
        } else {
            switch(direction) {
                case 'up':
                    start_row = 0;
                    start_col = 0;
                    step_row = 1;
                    step_col = 1;
                    break;
                case 'down':
                    start_row = 3;
                    start_col = 0;
                    step_row = -1;
                    step_col = 1;
                    break;
                case 'right':
                    start_row = 0;
                    start_col = 3;
                    step_row = 1;
                    step_col = -1;
                    break;
                case 'left':
                    start_row = 0;
                    start_col = 0;
                    step_row = 1;
                    step_col = 1;
                    break;
            }
            switch(direction) {
                case 'up':
                case 'down':
                    for(var i = start_col; i != start_col + 4 * step_col; i += step_col) {
                        var old_grid_row = start_row;
                        for(var j = start_row; j != start_row + 4 * step_row; j += step_row) {
                            if(old_grid_row < 0 || old_grid_row > 3) {
                                $scope.tiles.push({
                                    "value": new_grid[j][i],
                                    "x": i,
                                    "y": j,
                                    "visible": true
                                });
                            } else {
                                var new_value = new_grid[j][i];
                                var old_value = old_grid[old_grid_row][i];

                                if(new_value == old_value) { // Nothing moved
                                    old_grid_row += step_row;
                                    continue;
                                } else if (new_value > old_value) { // The tile was combined with a moving tile, or it coudld be a new tile where the old value was 0
                                    // Find the first tile
                                    while(old_grid_row > 0 && old_grid_row < 4 && old_grid[old_grid_row][i] == 0) {
                                        old_grid_row += step_row;
                                    }
                                    var base_tile_old_row = old_grid_row;
                                    // Find the moving tile in the old grid
                                    do {
                                        old_grid_row += step_row;
                                    } while (old_grid_row > 0 && old_grid_row < 4 && old_grid[old_grid_row][i] == 0);
                                    var moving_tile_old_row = old_grid_row;
                                    // TODO: Remove the tile at the current location and update the moving tile
                                    if(old_grid_row < 0 || old_grid_row > 4) {
                                        $scope.tiles.push({
                                            "value": new_grid[j][i],
                                            "x": i,
                                            "y": j,
                                            "visible": true
                                        });
                                    } else {
                                        $scope.tiles.forEach(function(tile, tile_index, tiles) {
                                            // TODO: It could be a new tile.
                                            // Is the current tile the one in the current location? Remove it
                                            if(tile.x == i && tile.y == base_tile_old_row && tile.value != new_value) {
                                                tile.visible = false;
                                            } else if (tile.x == i && tile.y == base_tile_old_row) {
                                                tile.y = j;
                                            } else
                                            // Is the current tile the one that moved? Move it.
                                            if(tile.x == i && tile.y == moving_tile_old_row) {
                                                tile.y = j;
                                                tile.value = new_grid[j][i];
                                            }
                                        });
                                    }
                                } else if (new_value < old_value) { // A moving tile moved on to this space.
                                    // Don't really know what to do here.
                                }
                            }
                            old_grid_row += step_row;
                        }
                    }
                    break;
                case 'left':
                case 'right':
                    for(var j = start_row; j != start_row + 4 * step_row; j += step_row) {
                        var old_grid_col = start_col;
                        for(var i = start_col; i != start_col + 4 * step_col; i += step_col) {
                            if(old_grid_col < 0 || old_grid_col > 3) {
                                $scope.tiles.push({
                                    "value": new_grid[j][i],
                                    "x": i,
                                    "y": j,
                                    "visible": true
                                });
                            } else {
                                var new_value = new_grid[j][i];
                                var old_value = old_grid[j][old_grid_col];

                                if(new_value == old_value) {
                                    old_grid_col += step_col;
                                    continue;
                                } else if (new_value > old_value) { // The tile was combined with a moving tile, or it coudld be a new tile where the old value was 0
                                    // Find the first tile
                                    while(old_grid_col > 0 && old_grid_col < 4 && old_grid[j][old_grid_col] == 0) {
                                        old_grid_col += step_col;
                                    }
                                    var base_tile_old_col = old_grid_col;
                                    // Find the moving tile in the old grid
                                    do {
                                        old_grid_col += step_col;
                                    } while (old_grid_col > 0 && old_grid_col < 4 && old_grid[j][col_grid_col] == 0);
                                    var moving_tile_old_row = old_grid_row;
                                    // TODO: Remove the tile at the current location and update the moving tile
                                    if(old_grid_col < 0 || old_grid_col > 4) {
                                        $scope.tiles.push({
                                            "value": new_grid[j][i],
                                            "x": i,
                                            "y": j,
                                            "visible": true
                                        });
                                    } else {
                                        $scope.tiles.forEach(function(tile, tile_index, tiles) {
                                            // TODO: It could be a new tile.
                                            // Is the current tile the one in the current location? Remove it
                                            if(tile.y == j && tile.x == base_tile_old_col && tile.value != new_value) {
                                                tile.visible = false;
                                            } else if (tile.y == j && tile.x == base_tile_old_col) {
                                                tile.x = i;
                                            } else
                                            // Is the current tile the one that moved? Move it.
                                            if(tile.y == j && tile.x == moving_tile_old_col) {
                                                tile.x = i;
                                                tile.value = new_grid[j][i];
                                            }
                                        });
                                    }
                                } else if (new_value < old_value) { // A moving tile moved on to this space.
                                    // Don't really know what to do here.
                                }
                            }
                            old_grid_row += step_row;
                        }
                    }
                    break;

            }
        }
        old_grid = new_grid;
    }
});


