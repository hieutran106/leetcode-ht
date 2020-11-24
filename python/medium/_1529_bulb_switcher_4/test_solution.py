import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.minFlips("10111")
        self.assertEqual(3, actual)

    def test_case2(self):
        actual = self.s.minFlips("101")
        self.assertEqual(3, actual)

    def test_case3(self):
        actual = self.s.minFlips("00000")
        self.assertEqual(0, actual)

    def test_case4(self):
        actual = self.s.minFlips("00111")
        self.assertEqual(1, actual)


    def test_case5(self):
        actual = self.s.minFlips("11000")
        self.assertEqual(2, actual)


if __name__ == '__main__':
    unittest.main()
