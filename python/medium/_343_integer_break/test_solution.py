import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.integerBreak(2)
        self.assertEqual(1, actual)

    def test_case2(self):
        actual = self.s.integerBreak(10)
        self.assertEqual(36, actual)


if __name__ == '__main__':
    unittest.main()

