import unittest
from .solution import Solution
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}

        def calculate_score(turn, i):
            if i >= len(stoneValue):
                return 0

            if (turn, i) in memo:
                return memo[(turn, i)]

            max_score = float('-inf')
            min_score = float('inf')
            total = 0

            cutoff_index = -1
            for j in range(i, min(i + 3, len(stoneValue))):
                next_turn = 'Bob' if turn == 'Alice' else 'Alice'
                next_turn_score = calculate_score(next_turn, j + 1)
                total = total + stoneValue[j]

                if turn == 'Alice':
                    score = total + next_turn_score
                    if score > max_score:
                        max_score = score
                        cutoff_index = j + 1
                else:
                    score = next_turn_score
                    if score < min_score:
                        min_score = score
                        cutoff_index = j + 1

            result = max_score if turn == 'Alice' else min_score

            memo[(turn, i)] = result
            return result

        alice_score = calculate_score('Alice', 0)
        bob_score = sum(stoneValue) - alice_score
        if alice_score == bob_score:
            return 'Tie'
        elif alice_score > bob_score:
            return 'Alice'
        else:
            return 'Bob'


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.stoneGameIII(stoneValue=[1, 2, 3, 7])
        self.assertEqual("Bob", actual)

    def test_case_2(self):
        actual = self.s.stoneGameIII(stoneValue=[1, 2, 3, -9])
        self.assertEqual("Alice", actual)

    def test_case_3(self):
        actual = self.s.stoneGameIII(stoneValue=[1, 2, 3, 6])
        self.assertEqual("Tie", actual)

    def test_case_4(self):
        actual = self.s.stoneGameIII(stoneValue=[-1, -2, -3])
        self.assertEqual("Tie", actual)

    def test_case_5(self):
        actual = self.s.stoneGameIII(
            stoneValue=[5, -14, 3, 1, -12, 9, 8, 11, -13, -13, -4, -14, -8, 17, -3, 4, 12, -5, -3, 13, -1, 5, -9])
        self.assertEqual("Alice", actual)

    def test_case_6(self):
        actual = self.s.stoneGameIII(
            stoneValue=[1, 2, 3, 4])
        self.assertEqual("Alice", actual)


if __name__ == '__main__':
    unittest.main()
