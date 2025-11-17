import unittest
from typing import List
import collections
# Date: 2025-11-04
# Problem: 3318 find_x_sum
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            sub_arr = nums[i:i+k]
            counter = collections.Counter(sub_arr)
            # Sort by frequency (descending), then by value (descending)
            sorted_elements = sorted(counter.items(), key = lambda item: (item[1], item[0]), reverse=True)
            x_sum = sum([element * frequency for element,frequency  in sorted_elements[:x]])
            ans.append(x_sum)
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2)
        self.assertEqual(actual, [6, 10, 12])
        
    def test_case_2(self):
        actual = self.s.findXSum(nums = [3,8,7,8,7,5], k = 2, x = 2)
        self.assertEqual(actual, [11,15,15,15,12])

if __name__ == '__main__':
    unittest.main()

