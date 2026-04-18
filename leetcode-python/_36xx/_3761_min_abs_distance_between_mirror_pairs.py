import unittest
from typing import List

# Date: 2026-04-18
# Problem: 3761 min_abs_distance_between_mirror_pairs
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            y = 0
            while x > 0:
                y = y * 10 + x % 10
                x = x // 10
            return y
        d = {}
        ans = float("inf")
        for i, n in enumerate(nums):
            if n in d:
                ans = min(ans, i - d[n])
            r = reverse(n)
            d[r] = i

        return ans if ans != float("inf") else -1
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minMirrorPairDistance(nums = [12,21,45,33,54])
        self.assertEqual(1, actual)
        
    def test_case_2(self):
        actual = self.s.minMirrorPairDistance(nums = [120,21])
        self.assertEqual(1, actual)

    def test_case_3(self):
        actual = self.s.minMirrorPairDistance(nums = [21,120])
        self.assertEqual(-1, actual)

if __name__ == '__main__':
    unittest.main()

