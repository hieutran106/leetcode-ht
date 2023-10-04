import unittest
from .solution import Solution
from typing import List


class Solution:
    def canWinNim(self, n: int) -> bool:
        # Memory Limit Exceeded
        dp = [True] * (n)
        for i in range(3, n):
            dp[i] = not(dp[i-1] and dp[i-2] and dp[i-3])
        return dp[n-1]
        # Solution
        if n % 4 == 0:
            return False
        else:
            return True

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.canWinNim(n=4)
        self.assertEqual(False, actual)
        
    def test_case_2(self):
        actual = self.s.canWinNim(n=1)
        self.assertEqual(True, actual)

        actual = self.s.canWinNim(n=2)
        self.assertEqual(True, actual)

        actual = self.s.canWinNim(n=3)
        self.assertEqual(True, actual)

if __name__ == '__main__':
    unittest.main()

