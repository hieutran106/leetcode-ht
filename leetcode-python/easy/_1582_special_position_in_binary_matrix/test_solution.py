import unittest
from .solution import Solution
from typing import List
from collections import Counter

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        candidates = []
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    candidates.append((i, j))
        print(candidates)
        row_counter = Counter(map(lambda x: x[0], candidates))
        col_counter = Counter(map(lambda x: x[1], candidates))
        special = 0
        for c in candidates:
            # only appear 1
            if row_counter[c[0]] == 1 and col_counter[c[1]] == 1:
                special += 1
        return special


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]])
        self.assertEqual(1, actual)

    def test_case_2(self):
        actual = self.s.numSpecial(mat=[[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(3, actual)

    def test_case_3(self):
        actual = self.s.numSpecial(mat=[[1, 0, 0]])
        self.assertEqual(1, actual)

    def test_case_4(self):
        actual = self.s.numSpecial(mat=[[1]])
        self.assertEqual(1, actual)

    def test_case_5(self):
        actual = self.s.numSpecial(mat=[[1], [0], [0]])
        self.assertEqual(1, actual)

    def test_case_6(self):
        actual = self.s.numSpecial(
            mat=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                 [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 1]])
        self.assertEqual(actual, 0)

    def test_case_7(self):
        actual = self.s.numSpecial(
            mat=[[0,0,0,0,0,1,0,0],
                 [0,0,0,0,1,0,0,1],
                 [0,0,0,0,1,0,0,0],
                 [1,0,0,0,1,0,0,0],
                 [0,0,1,1,0,0,0,0]])
        self.assertEqual(actual, 1)


if __name__ == '__main__':
    unittest.main()
