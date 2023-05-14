import unittest
from typing import List

from .solution import Solution

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.rob(nums = [1,2,3,1])
        self.assertEqual(4, actual)

    def test_case_2(self):
        actual = self.s.rob(nums = [2,7,9,3,1])
        self.assertEqual(12, actual)

    def test_case_3(self):
        actual = self.s.rob(nums = [2, 1])
        self.assertEqual(2, actual)
    def test_case_4(self):
        actual = self.s.rob(nums = [1])
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

