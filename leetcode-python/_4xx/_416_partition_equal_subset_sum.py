import unittest
from typing import List

#2025-08-04
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        memo = {}
        def dp(i, expect_sum) -> bool:
            if expect_sum == 0:
                return True
            if i >= len(nums) or expect_sum < 0:
                return False
            if (i, expect_sum) in memo:
                return memo[(i, expect_sum)]
            # Pick nums[i]
            pick = dp(i+1, expect_sum - nums[i])
            memo[(i+1, expect_sum - nums[i])] = pick
            if pick:
                return True

            not_pick = dp(i+1, expect_sum)
            memo[(i+1, expect_sum)] = not_pick
            return not_pick
        return dp(0, total // 2)

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.canPartition([1, 5, 1, 5])
        self.assertEqual(actual, True)

    def test_case2(self):
        actual = self.s.canPartition([1, 2, 3, 5])
        self.assertEqual(actual, False)

    def test_case3(self):
        actual = self.s.canPartition([1])
        self.assertEqual(actual, False)

    def test_case4(self):
        actual = self.s.canPartition([1, 4, 1])
        self.assertEqual(actual, False)

    def test_case5(self):
        actual = self.s.canPartition([1, 4, 9, 6])
        self.assertEqual(actual, True)

    def test_case6(self):
        actual = self.s.canPartition([1, 2, 3, 1000])
        self.assertEqual(actual, False)

    def test_case7(self):
        actual = self.s.canPartition([9, 5])
        self.assertEqual(actual, False)

if __name__ == '__main__':
    unittest.main()

