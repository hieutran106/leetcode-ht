import unittest
from .solution import Solution
from typing import List

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        visited = {(0,0)}
        for d in path:
            if d == 'N':
                x = x - 1
            elif d == 'S':
                x = x + 1
            elif d == 'E':
                y = y + 1
            elif d == 'W':
                y = y - 1

            if (x,y) in visited:
                return True

            visited.add((x, y))

        return False

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    
    def test_case_1(self):
        actual = self.s.isPathCrossing(path="NES")
        self.assertEqual(False, actual)
        
    def test_case_2(self):
        actual = self.s.isPathCrossing(path="NESWW")
        self.assertEqual(True, actual)

if __name__ == '__main__':
    unittest.main()

