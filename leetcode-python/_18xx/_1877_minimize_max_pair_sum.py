import unittest
from typing import List

# Date: 2025-19-05
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # sort the input a1<=a2<=a3<=...<=an
        # optimal pair (a1,an), (a2,an-1)...
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        while l < r:
            res = max(res, nums[l] + nums[r])
            l += 1
            r -= 1
        return res
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minPairSum(nums = [3,5,2,3])
        self.assertEqual(7, actual)
        
    def test_case_2(self):
        actual = self.s.minPairSum(nums = [3,5,4,2,4,6])
        self.assertEqual(8, actual)

if __name__ == '__main__':
    unittest.main()

