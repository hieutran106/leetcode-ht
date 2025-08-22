import unittest
from typing import List

# Date: 2025-22-08
# Problem: 3195 find_the_min_area_to_cover_all_ones
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        vertical = [0] * rows
        horizontal = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    vertical[i] = 1
                    horizontal[j] = 1
        vertical_start = vertical.index(1)
        vertical_end = len(vertical) - 1 - vertical[::-1].index(1)

        horizontal_start = horizontal.index(1)
        horizontal_end = len(horizontal) - 1 - horizontal[::-1].index(1)
        ans = (vertical_end - vertical_start + 1) * (horizontal_end - horizontal_start + 1)
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minimumArea(grid = [[0,1,0],[1,0,1]])
        self.assertEqual(actual, 6)
        
    def test_case_2(self):
        actual = self.s.minimumArea(grid = [[1,0],[0,0]])
        self.assertEqual(actual, 1)

if __name__ == '__main__':
    unittest.main()

