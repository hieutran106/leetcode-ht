import unittest
from .solution import Solution
from typing import List
import random


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def dp(turn, l, r, alice_score, bob_score):
            if l == r:
                return alice_score > bob_score
            key = (turn, l, r, alice_score, bob_score)

            if key in memo:
                return memo[key]

            if turn == 'alice':
                # alice pick first
                first = dp('bob', l + 1, r, alice_score + piles[l], bob_score)
                last = dp('bob', l, r - 1, alice_score + piles[r], bob_score)
                return first or last

            else:
                # bob pick first
                first = dp('alice', l + 1, r, alice_score, bob_score + piles[l])
                last = dp('alice', l, r - 1, alice_score, bob_score + piles[r])

            result = first or last

            memo[key] = result
            return result

        l = 0
        r = len(piles) - 1

        return dp('alice', l, r, 0, 0)


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.stoneGame([5, 3, 4, 5])
        self.assertEqual(True, actual)

    def test_case_2(self):
        actual = self.s.stoneGame([3, 7, 2, 3])
        self.assertEqual(True, actual)

    def test_case_3(self):
        actual = self.s.stoneGame([1, 4])
        self.assertEqual(True, actual)

    def test_case_4(self):
        actual = self.s.stoneGame([1, 5, 6, 3])
        self.assertEqual(True, actual)

    def test_case_5(self):
        actual = self.s.stoneGame([1, 5, 6, 3])
        self.assertEqual(True, actual)

    def test_case_6(self):
        for i in range(1000):
            n = 10
            input = [0] * n
            total = 0
            for j in range(0, n-1):
                v = random.randint(1, 100)
                total += v
                input[j] = v
            if total %2 == 0:
                input[n-1] = 1
            else:
                input[n-1] = 2

            actual = self.s.stoneGame(input)
            if not actual:
                print("Found a false input")

    def test_case_7(self):
        piles = [91,66,56,43,16,41,91,12,11,29,57,34,47,57,47,98,77,42,23,13,55,4,76,37,87,16,57,49,15,69,54,78,94,78,81,59,48,4,23,66,40,85,35,92,11,81,50,78,24,61,66,76,33,23,1,88,99,55,17,71,72,69,60,36,87,51,36,20,37,17,30,19,20,60,35,60,80,6,35,99,37,93,77,32,22,34,55,46,18,38,86,73,75,100,80,11,46,13,40,57]
        actual = self.s.stoneGame(piles)
        self.assertEqual(True, actual)




if __name__ == '__main__':
    unittest.main()
