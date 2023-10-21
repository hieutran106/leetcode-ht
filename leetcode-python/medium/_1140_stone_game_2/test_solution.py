import unittest
from .solution import Solution
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        def alice_score(turn, i, m):
            if i + 2 * m >= len(piles):
                if turn == 'alice':
                    # base case: if Alice can take all stone left
                    return sum(piles[i: min(i + 2 * m, len(piles))])
                else:
                    # Bob will take all stone left, hence Alice's score is 0
                    return 0
            if (turn, i, m) in memo:
                return memo[(turn, i, m)]

            total = 0
            max_alice_score = 0
            min_alice_score = float('inf')
            for j in range(i, i + 2 * m):
                total += piles[j]
                next_m = max(m, j - i + 1)
                if turn == 'alice':
                    score = total + alice_score('bob', j + 1, next_m)
                    max_alice_score = max(max_alice_score, score)
                else:
                    score = alice_score('alice', j + 1, next_m)
                    min_alice_score = min(min_alice_score, score)
                # scores.append(score)

            result = max_alice_score if turn == 'alice' else min_alice_score
            memo[(turn, i, m)] = result
            return result

        return alice_score('alice', 0, 1)


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.stoneGameII(piles=[2, 7, 9, 4, 4])
        self.assertEqual(10, actual)

    def test_case_2(self):
        actual = self.s.stoneGameII(piles=[1, 2, 3, 4, 5, 100])
        self.assertEqual(104, actual)

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
