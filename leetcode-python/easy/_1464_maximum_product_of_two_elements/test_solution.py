import unittest
from .solution import Solution
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n - 1):
            for j in range(i+1, n):
                value = (nums[i] -1)*(nums[j] - 1)
                res = max(res, value)
        return res
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maxProduct(nums = [3,4,5,2])
        self.assertEqual(12, actual)
        
    def test_case_2(self):
        actual = self.s.maxProduct(nums = [1,5,4,5])
        self.assertEqual(16, actual)

    def test_case_3(self):
        actual = self.s.maxProduct(nums = [3, 7])
        self.assertEqual(12, actual)

    def test_case_4(self):
        actual = self.s.maxProduct(nums = [1, 1])
        self.assertEqual(0, actual)

if __name__ == '__main__':
    unittest.main()

