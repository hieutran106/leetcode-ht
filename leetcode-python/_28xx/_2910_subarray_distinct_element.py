import unittest
from typing import List

# Date: 2026-10-15
# Problem: 2910 subarray_distinct_element
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])
                ans += len(s) * len(s)
        return ans


    

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.sumCounts(nums = [1,2,1])
        self.assertEqual(15, actual)
        
    def test_case_2(self):
        actual = self.s.sumCounts(nums=[1, 1])
        self.assertEqual(3, actual)

if __name__ == '__main__':
    unittest.main()

