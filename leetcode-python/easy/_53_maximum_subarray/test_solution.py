import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(actual, 6)

    def test_case2(self):
        actual = self.s.maxSubArray([1])
        self.assertEqual(actual, 1)

    def test_case3(self):
        actual = self.s.maxSubArray([5, 4, -1, 7, 8])
        self.assertEqual(actual, 23)

    def test_case4(self):
        actual = self.s.maxSubArray([904, 40, 523, 12, -335, -385, -124, 481, -31])
        self.assertEqual(actual, 1479)

if __name__ == "__main__":
    unittest.main()
