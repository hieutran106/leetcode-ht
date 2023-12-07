import math
import unittest
from .solution import Solution
from typing import List

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [None for _ in range(n +1)]
        dp[0] = False

        for i in range(1, n + 1):
            # calculate dp[i]
            int_sqrt = math.isqrt(i)
            for j in range(1, int_sqrt + 1):
                res = dp[i-j*j]
                if res is False:
                    dp[i] = True
                    break
            else:
                dp[i] = False
        return dp[n]


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.winnerSquareGame(n = 1)
        self.assertEqual(True, actual)
        
    def test_case_2(self):
        actual = self.s.winnerSquareGame(n=2)
        self.assertEqual(False, actual)

    def test_case_4(self):
        actual = self.s.winnerSquareGame(n=4)
        self.assertEqual(True, actual)

    def test_case_5(self):
        actual = self.s.winnerSquareGame(n=5)
        self.assertEqual(False, actual)

    def test_case_9(self):
        actual = self.s.winnerSquareGame(n=9)
        self.assertEqual(True, actual)

if __name__ == '__main__':
    unittest.main()

