import unittest
from typing import List

from .solution import Solution

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(2, numRows + 1):
            prev = res[-1]
            curr = [1]
            # for loop
            for j in range(1, len(prev)):
                curr.append(prev[j] + prev[j-1])
            curr.append(1)
            res.append(curr)
        return res

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.generate(numRows = 5)
        self.assertEqual([[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], actual)

    def test_case_2(self):
        actual = self.s.generate(numRows = 1)
        self.assertEqual([[1]], actual)

    def test_case_3(self):
        actual = self.s.generate(numRows = 2)
        self.assertEqual([[1], [1, 1]], actual)

if __name__ == '__main__':
    unittest.main()

