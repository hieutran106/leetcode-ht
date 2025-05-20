import collections
import unittest
from typing import List

# Date: 2025-21-05, line sweep
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        ongoing_events = collections.defaultdict(int)
        for l,r in queries:
            ongoing_events[l] += 1
            ongoing_events[r+1] -= 1
        for i, n in enumerate(nums):
            if i > 0:
                ongoing_events[i] += ongoing_events[i-1]
            if ongoing_events[i] < n:
                return False
        return True
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.isZeroArray(nums = [1,0,1], queries = [[0,2]])
        self.assertEqual(True, actual)
        
    def test_case_2(self):
        actual = self.s.isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]])
        self.assertEqual(False, actual)

if __name__ == '__main__':
    unittest.main()

