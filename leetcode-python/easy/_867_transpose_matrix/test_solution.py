import unittest
from .solution import Solution
from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        # Create transpose matrix
        res = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(cols):
            for j in range(rows):
                res[i][j] = matrix[j][i]
        return res

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual([[1,4,7],[2,5,8],[3,6,9]], actual)
        
    def test_case_2(self):
        actual = self.s.transpose(matrix = [[1,2,3],[4,5,6]])
        self.assertEqual([[1,4],[2,5],[3,6]], actual)

    def test_case_3(self):
        actual = self.s.transpose(matrix = [[1]])
        self.assertEqual([[1]], actual)

    def test_case_4(self):
        actual = self.s.transpose(matrix = [[1, 2]])
        self.assertEqual([[1], [2]], actual)

if __name__ == '__main__':
    unittest.main()

