import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):
    """
    Test case
    """

    def setUp(self) -> None:
        self.s = Solution()

    def test_case4(self):
        actual = self.s.lengthOfLIS([4, 5, 1, 6])
        self.assertEqual(actual, 3)

    def test_case5(self):
        actual = self.s.lengthOfLIS([4, 10, 4, 3, 8, 9])
        self.assertEqual(actual, 3)

    def test_case6(self):
        actual = self.s.lengthOfLIS([4, 10, 4, 3, 8])
        self.assertEqual(actual, 2)

    def test_case1(self):
        actual = self.s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
        self.assertEqual(actual, 4)

    def test_case2(self):
        actual = self.s.lengthOfLIS([0, 1, 0, 3, 2, 3])
        self.assertEqual(actual, 4)

    def test_case3(self):
        actual = self.s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7])
        self.assertEqual(actual, 1)


if __name__ == "__main__":
    unittest.main()
