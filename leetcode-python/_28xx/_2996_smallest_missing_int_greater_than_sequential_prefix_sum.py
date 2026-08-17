import unittest
from typing import List

# Date: 2026-08-11
# Problem: 2996 smallest_missing_int_greater_than_sequential_prefix_sum
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = set(nums)
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                break
            prefix_sum += nums[i]
        print(f"{prefix_sum=}")
        ans = prefix_sum
        while ans in s:
            ans += 1
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.missingInteger(nums = [1,2,3,2,5])
        self.assertEqual(6, actual)
        
    def test_case_2(self):
        actual = self.s.missingInteger(nums = [3,4,5,1,12,14,13])
        self.assertEqual(15, actual)

    def test_case_3(self):
        actual = self.s.missingInteger(nums = [7,9,8,10,12,11,7,13])
        self.assertEqual(14, actual)

if __name__ == '__main__':
    unittest.main()

