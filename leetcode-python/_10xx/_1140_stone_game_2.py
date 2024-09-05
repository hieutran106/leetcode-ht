import unittest
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        def alice_score(turn, i, m):
            if i == len(piles):
                return 0
            if (turn, i, m) in memo:
                return memo[(turn, i, m)]
            total = 0
            res = float("-inf") if turn == 'alice' else float("inf")
            for j in range(i, min(len(piles), i + 2 * m)):
                next_m = max(m, j - i + 1)
                if turn == 'alice':
                    total += piles[j]
                    res = max(res, total + alice_score('bob', j + 1, next_m))
                else:
                    res = min(res, alice_score('alice', j + 1, next_m))
            memo[(turn, i, m)] = res
            return res

        return alice_score('alice', 0, 1)


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.stoneGameII([2, 7, 9, 4, 4])
        self.assertEqual(actual, 10)

    def test_case_2(self):
        actual = self.s.stoneGameII([1, 2, 3, 4, 5, 100])
        self.assertEqual(actual, 104)

    def test_case_3(self):
        actual = self.s.stoneGameII(piles=[1])
        self.assertEqual(1, actual)

    def test_case_4(self):
        actual = self.s.stoneGameII(piles=[1, 2, 3])
        self.assertEqual(3, actual)

    def test_case_5(self):
        actual = self.s.stoneGameII(piles=[1, 2])
        self.assertEqual(3, actual)

    def test_case_6(self):
        actual = self.s.stoneGameII(piles=[2, 7, 9, 9, 4])
        self.assertEqual(15, actual)

    def test_case_7(self):
        actual = self.s.stoneGameII(
            piles=[2, 7, 9, 9, 4, 10, 2, 6, 7, 8, 10, 12, 14, 16, 18, 2, 7, 9, 9, 4, 10, 2, 6, 7, 8, 10, 12, 14, 16,
                   18])
        self.assertEqual(132, actual)

    def test_case_8(self):
        actual = self.s.stoneGameII(piles=[1, 2, 10000])
        self.assertEqual(3, actual)

    def test_case_9(self):
        actual = self.s.stoneGameII(
            piles=[8270, 7145, 575, 5156, 5126, 2905, 8793, 7817, 5532, 5726, 7071, 7730, 5200, 5369, 5763, 7148, 8287,
                   9449, 7567, 4850, 1385, 2135, 1737, 9511, 8065, 7063, 8023, 7729, 7084, 8407])
        self.assertEqual(98008, actual)


if __name__ == '__main__':
    unittest.main()
