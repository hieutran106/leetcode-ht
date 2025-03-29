import unittest
from typing import List


#2025-20-03
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # If two numbers are bit DISJOINT, the bitwise AND (&) between them is 0
        ans = 1
        for i in range(0, len(nums)):
            # bitmask to check set bit (bit 1) has been taken in the sub array
            used_bit = nums[i]
            l = 1
            for j in range(i + 1, len(nums)):
                if used_bit & nums[j] == 0:
                    # can join the subarray
                    used_bit = used_bit | nums[j]
                    l += 1
                else:
                    break
            ans = max(ans, l)
        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.longestNiceSubarray(nums = [1,3,8,48,10])
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.longestNiceSubarray(nums=[3,1,5,11,13])
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

