import unittest
from typing import List

# Date: 2026-07-26
# Problem: 628 max_product_of_three_numbers
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        nums.sort()
        c1 = nums[-1] * nums[-2] * nums[-3]
        c2 = nums[-1] * nums[0] * nums[1]
        return max(c1, c2)

    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maximumProduct(nums = [1,2,3])
        self.assertEqual(actual, 6)
        
    def test_case_2(self):
        actual = self.s.maximumProduct(nums = [1,2,3,4])
        self.assertEqual(actual, 24)

    def test_case_3(self):
        actual = self.s.maximumProduct(nums = [-1,-2,-3])
        self.assertEqual(actual, -6)

    def test_case_4(self):
        actual = self.s.maximumProduct(nums = [-6,-5,1, 2, 3])
        self.assertEqual(actual, 90)

    def test_case_5(self):
        actual = self.s.maximumProduct(nums = [-6,-5,-4,-3,2])
        self.assertEqual(actual, 60)

    def test_case_7(self):
        actual = self.s.maximumProduct(nums = [-6,-5,-4, 0])
        self.assertEqual(actual, 0)

if __name__ == '__main__':
    unittest.main()

