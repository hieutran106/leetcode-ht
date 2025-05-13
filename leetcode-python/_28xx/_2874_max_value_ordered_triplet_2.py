import unittest
from typing import List

#2025-03-04
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # build prefix_max
        prefix_max = [nums[0]]
        for i in range(1, len(nums)):
            prefix_max.append(max(nums[i], prefix_max[-1]))
        # build suffix max
        suffix_max = [nums[len(nums) - 1]]
        for i in range(len(nums) -2, -1, -1):
            suffix_max.append(max(nums[i], suffix_max[-1]))
        suffix_max.reverse()
        ans = 0
        for i in range(1, len(nums) - 1):
            val = (prefix_max[i-1] - nums[i]) * suffix_max[i+1] # maximum triplet value at index i
            ans = max(ans, val)

        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maximumTripletValue(nums = [12,6,1,2,7])
        self.assertEqual(77, actual)
        
    def test_case_2(self):
        actual = self.s.maximumTripletValue([1,10,3,4,19])
        self.assertEqual(133, actual)

    def test_case_3(self):
        actual = self.s.maximumTripletValue([1,10,3,4,19])
        self.assertEqual(133, actual)

    def test_case_4(self):
        actual = self.s.maximumTripletValue([1000000,1,1000000])
        self.assertEqual(999999000000, actual)

if __name__ == '__main__':
    unittest.main()

