import collections
import unittest
from typing import List

# Date: 2026-04-12
# Problem: 3741 min_distance_between_equal_elements_2
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = collections.defaultdict(list)
        ans = float("inf")
        for i, n in enumerate(nums):
            d[n].append(i)
            if len(d[n]) >= 3:
                ans = min(ans,2*d[n][-1] - 2 * d[n][-3])
        if ans == float("inf"):
            return -1
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minimumDistance(nums = [1,2,1,1,3])
        self.assertEqual(6, actual)
        
    def test_case_2(self):
        actual = self.s.minimumDistance(nums = [1,1,2,3,2,1,2])
        self.assertEqual(8, actual)

    def test_case_3(self):
        actual = self.s.minimumDistance(nums = [1])
        self.assertEqual(-1, actual)

if __name__ == '__main__':
    unittest.main()

