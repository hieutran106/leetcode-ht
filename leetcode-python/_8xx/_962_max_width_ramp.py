import unittest
from typing import List

# Date: 2025-11-07
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # sliding window, neetcode
        # step 1. create array that arr[i] is the max value from the right
        max_right = [nums[-1]]
        for i in range(len(nums) -2 , -1, -1):
            max_right.append(max(nums[i], max_right[-1]))
        max_right.reverse()
        print(max_right)
        l, r = 0, 1
        ans = 0
        while r < len(nums):
            while r < len(nums) and nums[l] <= max_right[r]:
                # valid window, there is numbers from the right greater or equal numbers at l pointer
                ans = max(ans, r - l)
                r += 1
            l += 1
        return ans



class Solution2:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # sliding window, neetcode
        # step 1. create array that arr[i] is the max value from the right
        max_right = [nums[-1]]
        for i in range(len(nums) -2 , -1, -1):
            max_right.append(max(nums[i], max_right[-1]))
        max_right.reverse()
        print(max_right)
        ans = 0
        l = 0
        # Using for loop -- cleaner
        for r in range(len(nums)):
            while nums[l] > max_right[r]:
                l += 1
            ans = max(ans, r - l)
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution2()
    
    def test_case_1(self):
        actual = self.s.maxWidthRamp(nums = [6,0,8,2,1,5])
        self.assertEqual(actual, 4)
        
    def test_case_2(self):
        actual = self.s.maxWidthRamp(nums = [9,8,1,0,1,9,4,0,4,1])
        self.assertEqual(actual, 7)

    def test_case_3(self):
        actual = self.s.maxWidthRamp(nums = [1,8,9,8,1])
        self.assertEqual(actual, 4)

    def test_case_4(self):
        actual = self.s.maxWidthRamp(nums = [3, 2, 1])
        self.assertEqual(actual, 0)

    def test_case_5(self):
        actual = self.s.maxWidthRamp(nums = [9, 7, 1, 0, 1, 10, 9])
        self.assertEqual(actual, 6)

    def test_case_6(self):
        actual = self.s.maxWidthRamp(nums = [0, 1])
        self.assertEqual(actual, 1)

if __name__ == '__main__':
    unittest.main()

