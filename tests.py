import unittest
from hello import (CountOpenSpaces, DiffBetweenAdjacent, DirectionalComparison, WeightedPositions)

class TestGrids(unittest.TestCase):
    
    grid1 = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 32, 16],
            [0, 16, 64, 2]]
            
    grid1up = [[0, 16, 32, 16],
                [0, 0, 64, 2],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    grid1left = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [32, 16, 0, 0],
                [16, 64, 2, 0]]
                
    grid2 = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [8, 32, 0, 0],
            [16, 64, 0, 0]]
            
    grid2up = [[8, 32, 0, 0],
                [16, 64, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    grid2right = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 8, 32],
                [0, 0, 16, 64]]
    
    grid3 = [[0, 0, 0, 0],
            [0, 0, 0, 4],
            [0, 0, 8, 8],
            [0, 0, 0, 16]]
    grid3right = [[0, 0, 0, 0],
                [0, 0, 0, 4],
                [0, 0, 0, 16],
                [0, 0, 0, 16]]
    grid3down = [[0, 0, 0, 0],
                [0, 0, 0, 4],
                [0, 0, 0, 8],
                [0, 0, 8, 16]]
    grid3left = [[0, 0, 0, 0],
                [4, 0, 0, 0],
                [16, 0, 0, 0],
                [16, 0, 0, 0]]
    
    def test_count_open_spaces_1(self):
        
                
        function = CountOpenSpaces()
        
        score1 = function.score(self.grid1up)
        score2 = function.score(self.grid1left)
        self.assertGreater(score2, score1, "Score left should be greater than up")
        
    def test_count_open_spaces_2(self):
        function = CountOpenSpaces()
        
        score_right = function.score(self.grid2right)
        score_up = function.score(self.grid2up)
        
        self.assertGreater(score_right, score_up, "Score right should be greater than up")
        
    def test_count_open_spaces_3(self):
        function = CountOpenSpaces()
        
        score_right = function.score(self.grid3right)
        score_down = function.score(self.grid3down)
        score_left = function.score(self.grid3left)
        
        self.assertGreater(score_right, score_down, "Score right should be greater than down")
        self.assertGreater(score_right, score_left, "Score right should be greater than left")

    def test_diff_between_adjacent_1(self):
        function = DiffBetweenAdjacent()
        
        score_up = function.score(self.grid1up)
        score_left = function.score(self.grid1left)
        self.assertGreater(score_left, score_up, "Score left should be greater than up")
        
    def test_diff_between_adjacent_2(self):
        function = DiffBetweenAdjacent()
        
        score_right = function.score(self.grid2right)
        print score_right
        score_up = function.score(self.grid2up)
        print score_up
        
        self.assertGreater(score_right, score_up, "Score right should be greater than up") 
        
    def test_diff_between_adjacent_3(self):
        function = DiffBetweenAdjacent()
        
        score_right = function.score(self.grid3right)
        score_down = function.score(self.grid3down)
        score_left = function.score(self.grid3left)
        
        self.assertGreater(score_right, score_down, "Score right should be greater than down")
        self.assertGreater(score_right, score_left, "Score right should be greater than left")
                
    def test_directional_comparison_1(self):
        function = DirectionalComparison()
        
        score_up = function.score(self.grid1up)
        score_left = function.score(self.grid1left)
        self.assertGreater(score_left, score_up, "Score left should be greater than up")

    def test_directional_comparison_2(self):
        function = DirectionalComparison()
        
        score_right = function.score(self.grid2right)
        score_up = function.score(self.grid2up)
        
        self.assertGreater(score_right, score_up, "Score right should be greater than up") 
        
    def test_directional_comparison_3(self):
        function = DirectionalComparison()
        
        score_right = function.score(self.grid3right)
        score_down = function.score(self.grid3down)
        score_left = function.score(self.grid3left)
        
        self.assertGreater(score_right, score_down, "Score right should be greater than down")
        self.assertGreater(score_right, score_left, "Score right should be greater than left")
        
    def test_weighted_positions_1(self):
        function = WeightedPositions()
        
        score_up = function.score(self.grid1up)
        score_left = function.score(self.grid1left)
        self.assertGreater(score_left, score_up, "Score left should be greater than up")

    def test_weighted_positions_2(self):
        function = WeightedPositions()
        
        score_right = function.score(self.grid2right)
        score_up = function.score(self.grid2up)
        
        self.assertGreater(score_right, score_up, "Score right should be greater than up") 
        
    def test_weighted_positions_3(self):
        function = WeightedPositions()
        
        score_right = function.score(self.grid3right)
        score_down = function.score(self.grid3down)
        score_left = function.score(self.grid3left)
        
        self.assertGreater(score_right, score_down, "Score right should be greater than down")
        self.assertGreater(score_right, score_left, "Score right should be greater than left")
        
if __name__ == '__main__':
    unittest.main()
