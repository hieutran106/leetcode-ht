import unittest
from .solution2 import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.change(5, [1, 2, 5])
        self.assertEqual(4, actual)

    def test_case2(self):
        actual = self.s.change(3, [2])
        self.assertEqual(0, actual)

    def test_case3(self):
        actual = self.s.change(10, [10])
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

