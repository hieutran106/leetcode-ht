import unittest
from .solution import Solution
from typing import List, Tuple


class Solution:

    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        """
        The optimal strategy is the Alice+Bob value , because it's greedily that Alice takes the most and Bob loses the most.
        If the Alice+Bob value is the same ,then sort the Alice's value, That's most optimal to Alice
        Alice: [10,8,1]
        Bob: [1,5,2]
        Alice would take index 1,because:
        For Alice : she can get 8 , at the mean time she can stop Bob from taking 5.


        """
        map()
        combined_values = sorted(zip(aliceValues, bobValues), key=lambda x: x[0] + x[1], reverse=True)
        alice_score = 0
        bob_score = 0
        for i in range(len(combined_values)):
            if i % 2 == 0:
                alice_score += combined_values[i][0]
            else:
                bob_score += combined_values[i][1]

        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        else:
            return 0


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.stoneGameVI(aliceValues=[1, 3], bobValues=[2, 1])
        self.assertEqual(actual, 1)

    def test_case_2(self):
        actual = self.s.stoneGameVI([1, 2], bobValues=[3, 1])
        self.assertEqual(actual, 0)

    def test_case_3(self):
        actual = self.s.stoneGameVI(aliceValues=[2, 4, 3], bobValues=[1, 6, 7])
        self.assertEqual(actual, -1)

    def test_case_4(self):
        actual = self.s.stoneGameVI(aliceValues=[9, 9, 5, 5, 2, 8, 2, 4, 10, 2, 3, 3, 4],
                                    bobValues=[9, 5, 3, 4, 4, 6, 6, 6, 4, 3, 7, 5, 10])
        self.assertEqual(actual, 1)

    def test_case_5(self):
        actual = self.s.stoneGameVI(aliceValues=[5, 6, 1, 9, 4, 7, 1, 7, 3, 7, 9, 7, 1, 2, 3, 9, 4, 7, 6],
                                    bobValues=[1, 2, 3, 5, 2, 8, 5, 9, 1, 6, 4, 2, 10, 4, 8, 1, 10, 5, 6])
        self.assertEqual(actual, 1)


if __name__ == '__main__':
    unittest.main()
