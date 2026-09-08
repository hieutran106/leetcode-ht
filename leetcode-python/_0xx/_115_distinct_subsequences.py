import unittest
from typing import List

# Date: 2026-09-09
# Problem: 115 distinct_subsequences
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def helper(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i] != t[j]:
                ret = helper(i+1, j)
            else:
                ret = helper(i+1, j+1) + helper(i+1, j)
            memo[(i,j)] = ret
            return ret

        ans = helper(0, 0)
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.numDistinct(s = "rabbbit", t = "rabbit")
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.numDistinct(s = "babgbag", t = "bag")
        self.assertEqual(5, actual)

    def test_case_3(self):
        actual = self.s.numDistinct(s = "bbacdac", t = "aa")
        self.assertEqual(1, actual)

    def test_case_4(self):
        actual = self.s.numDistinct(s = "bbacdac", t = "a")
        self.assertEqual(2, actual)

    def test_case_5(self):
        actual = self.s.numDistinct(s="bac", t="a")
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

