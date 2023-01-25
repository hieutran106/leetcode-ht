import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.minEatingSpeed([3, 6, 7, 11], 8)
        self.assertEqual(4, actual)

    def test_case2(self):
        actual = self.s.minEatingSpeed([30, 11, 23, 4, 20], 5)
        self.assertEqual(30, actual)

    def test_case3(self):
        actual = self.s.minEatingSpeed([30, 11, 23, 4, 20], 6)
        self.assertEqual(23, actual)

    def test_case4(self):
        actual = self.s.minEatingSpeed([1], 1)
        self.assertEqual(1, actual)

    def test_case5(self):
        actual = self.s.minEatingSpeed([2], 2)
        self.assertEqual(1, actual)

    def test_case6(self):
        actual = self.s.minEatingSpeed([312884470], 968709470)
        self.assertEqual(1, actual)


if __name__ == '__main__':
    unittest.main()
