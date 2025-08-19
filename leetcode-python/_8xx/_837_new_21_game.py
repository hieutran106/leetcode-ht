import unittest
from typing import List

# Date: 2025-18-08
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        memo = {}
        def dp(i: int):
            if i == 0:
                return 1
            if i in memo:
                return memo[i]
            res = 0
            for p in range(1, maxPts + 1):
                if i -p >=0 and i - p <k:
                    res += dp(i-p) * 1/maxPts
            memo[i] = res
            return res

        ans = 0
        for i in range(k, n+1):
            ans += dp(i)
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.new21Game(n = 10, k = 1, maxPts = 10)
        self.assertAlmostEqual(actual, 1.0, None, "", 10 ** -5)
        
    def test_case_2(self):
        actual = self.s.new21Game(n = 6, k = 1, maxPts = 10)
        self.assertAlmostEqual(actual, 0.6, None, "", 10 ** -5)

    def test_case_3(self):
        actual = self.s.new21Game(n = 21, k = 17, maxPts = 10)
        self.assertAlmostEqual(actual, 0.73278, None, "", 10 ** -5)

    def test_case_4(self):
        actual = self.s.new21Game(n = 9811, k = 8776, maxPts = 1096)
        self.assertAlmostEqual(actual, 0.99696, None, "", 10 ** -5)

if __name__ == '__main__':
    unittest.main()

