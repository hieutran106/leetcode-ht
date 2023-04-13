import unittest

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_subset = []

        def dfs(i: int):
            if i >= len(nums):
                res.append(curr_subset.copy())
                return
            # option to include character at (i)th-index
            curr_subset.append(nums[i])
            dfs(i + 1)
            # option to NOT include character at ith
            curr_subset.pop()
            dfs(i + 1)
        dfs(0)
        return res


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.subsets([1, 2, 3])
        self.assertEqual(actual, [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []])

    def test_case_2(self):
        actual = self.s.subsets([0])
        self.assertEqual(actual, [[0], []])


if __name__ == '__main__':
    unittest.main()
