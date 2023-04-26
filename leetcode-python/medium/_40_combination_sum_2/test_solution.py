import unittest
from typing import List

from .solution import Solution


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i: int, combination: List[int], total):
            if total == target:
                res.append(combination.copy())
                return
            if total > target or i >= len(candidates):
                return
            # take ith number
            combination.append(candidates[i])
            backtrack(i+1, combination, total + candidates[i])
            # do not take i-th number
            combination.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            backtrack(j, combination, total)

        backtrack(0, [], 0)
        return res




class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
        self.assertEqual([
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6]
        ], actual)

    def test_case_2(self):
        actual = self.s.combinationSum2(candidates = [2,5,2,1,2], target = 5)
        self.assertEqual([
            [1, 2, 2],
            [5]
        ], actual)


if __name__ == '__main__':
    unittest.main()
