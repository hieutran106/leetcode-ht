import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.findTargetSumWays([1, 1, 1, 1, 1], 3)
        self.assertEqual(actual, 5)

    def test_case2(self):
        actual = self.s.findTargetSumWays([1], 1)
        self.assertEqual(actual, 1)

    def test_case3(self):
        actual = self.s.findTargetSumWays([1, 2], 3)
        self.assertEqual(actual, 1)

    def test_case4(self):
        actual = self.s.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1)
        self.assertEqual(actual, 256)

    def test_case5(self):
        actual = self.s.findTargetSumWays([0, 3], 3)
        self.assertEqual(actual, 2)

    def test_case6(self):
        actual = self.s.findTargetSumWays([2, 0], 0)
        self.assertEqual(actual, 0)

    def test_case7(self):
        actual = self.s.findTargetSumWays([7, 9, 3, 8, 0, 2, 4, 8, 3, 9], 0)
        self.assertEqual(actual, 0)

    def test_case8(self):
        actual = self.s.findTargetSumWays([1, 999], 998)
        self.assertEqual(actual, 1)

    def test_case9(self):
        actual = self.s.findTargetSumWays(
            [
                2,
                107,
                109,
                113,
                127,
                131,
                137,
                3,
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                47,
                53,
            ],
            1000,
        )
        self.assertEqual(actual, 0)

    def test_case10(self):
        actual = self.s.findTargetSumWays([2, 0, 0], 2)
        self.assertEqual(actual, 4)

    def test_case11(self):
        actual = self.s.findTargetSumWays([2], 2)
        self.assertEqual(actual, 1)

    def test_case12(self):
        actual = self.s.findTargetSumWays([0], 0)
        self.assertEqual(actual, 2)


if __name__ == "__main__":
    unittest.main()
