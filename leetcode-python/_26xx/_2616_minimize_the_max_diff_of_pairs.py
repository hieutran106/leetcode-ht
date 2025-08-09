import unittest
from typing import List

# Date: 2025-13-06
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # DP LTE
        # sorted nums can help
        nums.sort()
        memo = {}
        def dp(i, curr_p):
            if curr_p == 0:
                return 0
            if i >= len(nums):
                return float("inf")
            if (i, curr_p) in memo:
                return memo[(i, curr_p)]

            # pick i_th
            c1 = float("inf")
            if i < len(nums) - 1:
                c1 = max(abs(nums[i] - nums[i+1]), dp(i + 2, curr_p - 1))
            # do not pick ith
            c2 = dp(i + 1, curr_p)
            res = min(c1, c2)
            memo[(i, curr_p)] = res
            return res

        return dp(0, p)
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minimizeMax(nums = [10,1,2,7,1,3], p = 2)
        self.assertEqual(1, actual)

        
    def test_case_2(self):
        actual = self.s.minimizeMax(nums = [4,2,1,2], p = 1)
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.minimizeMax(nums = [1,2,2,2,2,2,4], p = 1)
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.minimizeMax(nums = [1, 1, 2, 3], p = 2)
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

