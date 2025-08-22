import unittest
from typing import List


# Date: 2025-08-20
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1: # edge case
            return 1
        dp = [0] * (n+1) # dp[i] 0 probability that Alice get exact i point
        dp[0] = 1

        prefix_sum = [0] * (n+1)
        prefix_sum[0] = dp[0]

        for i in range(1, n + 1):
            # with optimization
            l = max(i - maxPts, 0)
            r = min(i - 1, k - 1)
            optmz = (prefix_sum[r] - prefix_sum[l-1])/maxPts

            dp[i] = optmz
            prefix_sum[i] = prefix_sum[i-1] + dp[i]

        ans = 0
        for i in range(k, n + 1):
            ans += dp[i]

        return ans

# Date: 2025-18-08
class SolutionTLE:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """
        This solution is Time Limit Exceeded. The inner for loop can be optimized
        """
        dp = [0] * (n+1) # dp[i] 0 probability that Alice get exact i point
        dp[0] = 1

        for i in range(1, n + 1):
            total = 0
            for p in range(1, maxPts + 1):
                if i -p >=0 and i-p <k:
                    total += dp[i-p] * 1/maxPts
            dp[i] = total

        ans = 0
        for i in range(k, n + 1):
            ans += dp[i]
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

    def test_case_5(self):
        actual = self.s.new21Game(n=3, k=0, maxPts=2)
        self.assertAlmostEqual(actual, 1.0, None, "", 10 ** -5)

    def test_case_6(self):
        actual = self.s.new21Game(n=12, k=1, maxPts=10)
        self.assertAlmostEqual(actual, 1.0, None, "", 10 ** -5)

    def test_case_7(self):
        actual = self.s.new21Game(n=21, k=17, maxPts=10)
        self.assertAlmostEqual(actual, 0.732778, None, "", 10 ** -5)

if __name__ == '__main__':
    unittest.main()

