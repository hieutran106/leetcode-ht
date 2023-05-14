import unittest
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in reversed(range(0, n-1)):
            if nums[i] == 0:
                dp[i] = 10e4 + 1
                continue
            start = i + 1
            end = min(n, nums[i] + i + 1)
            dp[i] = min(dp[start: end]) + 1

        return dp[0]
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.jump(nums = [2,3,1,1,4])
        self.assertEqual(2, actual)

    def test_case_2(self):
        actual = self.s.jump(nums = [2,3,0,1,4])
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.jump(nums = [0])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.jump(nums = [2, 1])
        self.assertEqual(1, actual)

    def test_case_5(self):
        actual = self.s.jump(nums = [5, 4, 3, 2, 1, 0])
        self.assertEqual(1, actual)

    def test_case_6(self):
        actual = self.s.jump(nums = [4, 4, 3, 2, 1, 0])
        self.assertEqual(2, actual)

if __name__ == '__main__':
    unittest.main()

