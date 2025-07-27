import unittest
from typing import List, Dict
import collections

# Date: 2025-27-07
def valid_window(counter: Dict[int, int]):
    for v in counter.values():
        if v > 1:
            return False
    return True

def valid_window_2(couter: Dict[int, int], key: int):
    # optimize version
    return couter[key] <= 1

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)
        ans = 0
        l = 0
        curr_sum = 0
        for r in range(len(nums)):
            counter[nums[r]] += 1
            curr_sum += nums[r]
            while not valid_window_2(counter, nums[r]):
                counter[nums[l]] -= 1
                curr_sum -= nums[l]
                l += 1
            ans = max(ans, curr_sum)
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maximumUniqueSubarray(nums = [4,2,4,5,6])
        self.assertEqual(17, actual)
        
    def test_case_2(self):
        actual = self.s.maximumUniqueSubarray(nums = [5,2,1,2,5,2,1,2,5])
        self.assertEqual(8, actual)

    def test_case_3(self):
        actual = self.s.maximumUniqueSubarray(nums = [1, 1, 2, 3, 1, 2, 3, 4, 1])
        self.assertEqual(10, actual)

    def test_case_4(self):
        actual = self.s.maximumUniqueSubarray(nums = [1, 2, 3, 1])
        self.assertEqual(6, actual)

    def test_case_5(self):
        actual = self.s.maximumUniqueSubarray(nums = [1, 2, 3, 1, 2, 3, 4])
        self.assertEqual(10, actual)

if __name__ == '__main__':
    unittest.main()

