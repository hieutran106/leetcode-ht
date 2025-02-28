import collections
import unittest
from typing import List, Dict


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(path: List[int], d: Dict[int, int]):
            if len(path) == n:
                ans.append(path.copy())
                return
            for k, v in d.items():
                if v == 0:
                    continue
                d[k] -= 1
                path.append(k)
                backtrack(path, d)
                path.pop()
                d[k] += 1
        path = []
        d = collections.Counter(nums)
        backtrack(path, d)
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.permuteUnique(nums=[1, 1, 2])
        self.assertEqual(3, len(actual))
        self.assertIn([1, 1, 2], actual)
        self.assertIn([1, 2, 1], actual)
        self.assertIn([2, 1, 1], actual)

    def test_case_2(self):
        actual = self.s.permuteUnique(nums=[1, 2, 3])
        self.assertEqual(6, len(actual))
        self.assertIn([2, 1, 3], actual)
        self.assertIn([3, 1, 2], actual)
        self.assertIn([3, 2, 1], actual)


if __name__ == '__main__':
    unittest.main()
