import unittest
from typing import List


# Date: 2026-08-25
# Problem: 1927 sum_game
class Solution:
    def sumGame(self, num: str) -> bool:
        l, r = 0, 0
        diff = 0  # sum(left) - sum(right)
        n = len(num)
        for i, v in enumerate(num):
            if v != '?':
                if i < n // 2:
                    diff += v
                else:
                    diff -= v
            else:
                if i < n // 2:
                    l += 1
                else:
                    r += 1

        def dfs(turn, d, left, right):
            if left == 0 and right == 0:
                return d == 0
            if turn == 'alice':
                start, end = -9, 9
                if left > 0 and right == 0:
                    start = 0
                if left == 0 and right > 0:
                    end = 0
                # Alice wants to maximize the abs(diff)
                max_value = float("-inf")
                max_number = None
                for i in range(start, end + 1):
                    pass

            else:
                pass

        return True


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.sumGame(num="5023")
        self.assertEqual(False, actual)

    def test_case_2(self):
        actual = self.s.sumGame(num="25??")
        self.assertEqual(True, actual)

    def test_case_3(self):
        actual = self.s.sumGame(num="?3295???")
        self.assertEqual(False, actual)


if __name__ == '__main__':
    unittest.main()
