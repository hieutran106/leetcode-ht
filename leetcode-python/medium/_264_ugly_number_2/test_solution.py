import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.nthUglyNumber(6)
        self.assertEqual(actual, 6)

        actual = self.s.nthUglyNumber(7)
        self.assertEqual(actual, 8)

    def test_case11(self):
        actual = self.s.nthUglyNumber(10)
        self.assertEqual(actual, 12)

    def test_case2(self):
        actual = self.s.nthUglyNumber(1)
        self.assertEqual(actual, 1)

    def test_case3(self):
        actual = self.s.nthUglyNumber(11)
        self.assertEqual(actual, 15)

    def test_case4(self):
        actual = self.s.nthUglyNumber(100)
        self.assertEqual(actual, 1536)

    def test_case5(self):
        actual = self.s.nthUglyNumber(500)
        self.assertEqual(actual, 937500)

    def test_case6(self):
        actual = self.s.nthUglyNumber(34)
        self.assertEqual(actual, 100)

    def test_case7(self):
        actual = self.s.nthUglyNumber(1600)
        self.assertEqual(actual, 1399680000)



if __name__ == '__main__':
    unittest.main()

