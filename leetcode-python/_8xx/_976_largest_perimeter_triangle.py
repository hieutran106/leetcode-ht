import unittest
from typing import List

# Date: 2025-09-29
# Problem: 976 largest_perimeter_triangle
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.largestPerimeter(nums = [2,1,2])
        self.assertEqual(5, actual)
        
    def test_case_2(self):
        actual = self.s.largestPerimeter(nums = [1,2,1,10])
        self.assertEqual(0, actual)

if __name__ == '__main__':
    unittest.main()

