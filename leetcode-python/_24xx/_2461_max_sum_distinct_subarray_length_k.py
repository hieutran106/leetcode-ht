import collections
import unittest
from typing import List, Dict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        def is_valid(n):
            for v in n.values():
                if v > 1:
                    return False
            return True

        count = collections.defaultdict(int)
        ans, l = 0, 0
        window_sum = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            window_sum += nums[r]
            while len(count) == k:
                if is_valid(count):
                    ans = max(ans, window_sum)
                count[nums[l]] -= 1
                window_sum -= nums[l]
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                l += 1

        return ans


#2025-17-03
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3)
        self.assertEqual(15, actual)
        
    def test_case_2(self):
        actual = self.s.maximumSubarraySum(nums = [4,4,4], k = 3)
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.maximumSubarraySum(nums = [1,1,1,1,1,1,2,3], k = 3)
        self.assertEqual(6, actual)

    def test_case_4(self):
        actual = self.s.maximumSubarraySum(nums = [1,2,1,2,1,2,1,3,5], k = 3)
        self.assertEqual(9, actual)


    def test_case_5(self):
        actual = self.s.maximumSubarraySum(nums = [9,9,9,1,2], k = 3)
        self.assertEqual(12, actual)


if __name__ == '__main__':
    unittest.main()

