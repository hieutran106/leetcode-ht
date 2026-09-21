import unittest
from typing import List

# Date: 2026-09-20
# Problem: 1477 find_two_non_overlapping_sa_target_sum
class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        if len(arr) == 1:
            return -1
        # shortest valid subarray until i-th
        min_till = [float("inf")] * len(arr)
        l, total = 0, 0
        ans = float("inf")
        for r in range(len(arr)):
            total += arr[r]
            
            while total > target:
                total -= arr[l]
                l += 1
            
            if total == target:
                valid_len = r - l + 1
                min_till[r] = min(min_till[r - 1], valid_len)
                ans = min(ans, valid_len + min_till[l-1])
            else:
                min_till[r] = min_till[r-1]

        if ans == float("inf"):
            return -1

        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minSumOfLengths(arr = [3,2,2,4,3], target = 3)
        self.assertEqual(2, actual)
        
    def test_case_2(self):
        actual = self.s.minSumOfLengths(arr = [7,3,4,7], target = 7)
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.minSumOfLengths(arr = [4,3,2,6,2,3,4], target = 6)
        self.assertEqual(-1, actual)

    def test_case_4(self):
        actual = self.s.minSumOfLengths(arr = [1,3, 2, 3, 1, 1, 1, 5, 7], target = 5)
        self.assertEqual(3, actual)

    def test_case_5(self):
        actual = self.s.minSumOfLengths(arr = [9, 4, 1, 2, 2, 9], target = 5)
        self.assertEqual(-1, actual)

    def test_case_6(self):
        actual = self.s.minSumOfLengths(arr=[11], target=11)
        self.assertEqual(-1, actual)

if __name__ == '__main__':
    unittest.main()

