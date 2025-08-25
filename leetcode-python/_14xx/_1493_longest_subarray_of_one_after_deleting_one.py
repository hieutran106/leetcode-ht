import unittest
from typing import List

# Date: 2025-25-08
# Problem: 1493 longest_subarray_of_one_after_deleting_one
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        encode = [] # padding

        l = 0
        for r in range(len(nums) + 1):
            if r == len(nums) or nums[r] != nums[l]:
                encode.append((nums[l], r - l)) # (value, count)
                l = r

        if len(encode) == 1 and encode[0][0] == 1:
            return encode[0][1] - 1

        ans = 0
        for i in range(0, len(encode)):
            v, count = encode[i]
            if v == 1:
                continue
            prev_one = encode[i-1][1] if i > 0  else 0
            next_one = encode[i+1][1] if i < len(encode) -1 else 0

            if count == 1:
                ans = max(ans, prev_one + next_one)
            else:
                ans = max(ans, prev_one, next_one)

        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.longestSubarray(nums = [1,1,0,1])
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.longestSubarray(nums = [0,1,1,1,0,1,1,0,1])
        self.assertEqual(5, actual)

    def test_case_3(self):
        actual = self.s.longestSubarray(nums = [1,1,1])
        self.assertEqual(2, actual)

    def test_case_4(self):
        actual = self.s.longestSubarray(nums = [1])
        self.assertEqual(0, actual)

    def test_case_5(self):
        actual = self.s.longestSubarray(nums = [0])
        self.assertEqual(0, actual)

    def test_case_6(self):
        actual = self.s.longestSubarray(nums = [1, 0, 0, 0, 0])
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

