import unittest
from .solution import Solution
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        mapping = set([str(i) for i in range(1, 27)])
        memo = {}

        def dp(pos: int) -> int:
            if pos == n:
                return 1
            if pos in memo:
                return memo[pos]

            res = 0
            if s[pos] in mapping:
                res += dp(pos + 1)
            if pos <= n - 2 and s[pos:pos + 2] in mapping:
                res += dp(pos + 2)
            memo[pos] = res
            return res

        result = dp(0)
        return result


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.numDecodings(s="12")
        self.assertEqual(actual, 2)

    def test_case_2(self):
        actual = self.s.numDecodings(s="226")
        self.assertEqual(actual, 3)

    def test_case_3(self):
        actual = self.s.numDecodings(s="06")
        self.assertEqual(actual, 0)

    def test_case_4(self):
        actual = self.s.numDecodings(s="1")
        self.assertEqual(actual, 1)

    def test_case_5(self):
        actual = self.s.numDecodings(s="0")
        self.assertEqual(actual, 0)

    def test_case_6(self):
        actual = self.s.numDecodings(s="11106")
        self.assertEqual(actual, 2)

    def test_case_7(self):
        actual = self.s.numDecodings(s="27")
        self.assertEqual(actual, 1)


if __name__ == '__main__':
    unittest.main()
