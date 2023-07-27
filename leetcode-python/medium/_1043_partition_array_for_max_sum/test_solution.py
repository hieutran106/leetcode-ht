import unittest
from typing import List

from .solution import Solution


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]
        for i in range(1, n):
            max_dp = 0
            max_ele = 0 # max value in range [i - k:i]
            for j in range(1, k + 1):
                prev_dp_index = i - j
                if prev_dp_index < - 1:
                    break

                prev_dp_value = dp[prev_dp_index] if prev_dp_index >=0 else 0
                max_ele = max(arr[prev_dp_index + 1], max_ele)
                max_dp = max(prev_dp_value + max_ele * j, max_dp)
            dp[i] = max_dp
        return dp[n-1]


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3)
        self.assertEqual(84, actual)

    def test_case_2(self):
        actual = self.s.maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4)
        self.assertEqual(83, actual)

    def test_case_3(self):
        actual = self.s.maxSumAfterPartitioning(arr = [1], k = 1)
        self.assertEqual(1, actual)

    def test_case_4(self):
        actual = self.s.maxSumAfterPartitioning(arr = [1, 2], k = 1)
        self.assertEqual(3, actual)

    def test_case_5(self):
        actual = self.s.maxSumAfterPartitioning(arr = [1, 2], k = 2)
        self.assertEqual(4, actual)

if __name__ == '__main__':
    unittest.main()

