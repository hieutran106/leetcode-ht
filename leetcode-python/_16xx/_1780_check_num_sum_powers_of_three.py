import unittest
from typing import List
import math


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        p = math.floor(math.log(n) / math.log(3))

        def backtrack(curr_sum: int, i: int):
            if curr_sum == n:
                return True
            if curr_sum > n or i > p:
                return False
            # pick i
            if backtrack(curr_sum + 3 ** i, i + 1):
                return True
            return backtrack(curr_sum, i + 1)

        return backtrack(0, 0)


class Solution3:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        math
        :param n:
        :return:
        """
        while n > 0:
            q = n // 3
            r = n % 3
            if r == 2:
                return False

            n = q
        return True


class Solution2:

    def checkPowersOfThree(self, n: int) -> bool:
        dp = [False] * (n + 1)
        d = {}

        def is_power_of_three(i):
            if i <= 0:
                return False
            return (math.log10(i) / math.log10(3)).is_integer()

        for i in range(1, n + 1):
            if is_power_of_three(i):
                dp[i] = True
                d[i] = set([i])
                continue
            for j in range(1, n // 2):
                if dp[j] is True and dp[i - j] is True:
                    s1 = d[j]
                    s2 = d[i - j]
                    if s1.isdisjoint(s2):
                        # print(f"At {i=}, found smaller problem {j=}, and {(i-j)=}")
                        dp[i] = True
                        d[i] = s1.union(s2)  # join two set and return a new set
                        break

        return dp[n]


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.checkPowersOfThree(12)
        self.assertEqual(True, actual)

    def test_case_2(self):
        actual = self.s.checkPowersOfThree(91)
        self.assertEqual(True, actual)

    def test_case_3(self):
        actual = self.s.checkPowersOfThree(21)
        self.assertEqual(False, actual)

    def test_case_4(self):
        actual = self.s.checkPowersOfThree(2)
        self.assertEqual(False, actual)

    def test_case_5(self):
        actual = self.s.checkPowersOfThree(5)
        self.assertEqual(False, actual)

    def test_case_6(self):
        actual = self.s.checkPowersOfThree(30493)
        self.assertEqual(False, actual)

    def test_case_7(self):
        actual = self.s.checkPowersOfThree(20597)
        self.assertEqual(False, actual)


if __name__ == '__main__':
    unittest.main()
