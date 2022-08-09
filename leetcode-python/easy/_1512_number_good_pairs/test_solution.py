import unittest
from .solution import Solution, Solution2


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.numIdenticalPairs([1, 2, 3, 1, 1, 3])
        self.assertEqual(actual, 4)

    def test_case2(self):
        actual = self.s.numIdenticalPairs([1, 1, 1, 1])
        self.assertEqual(actual, 6)

    def test_case3(self):
        actual = self.s.numIdenticalPairs([1, 2, 3])
        self.assertEqual(actual, 0)

    def test_case4(self):
        actual = self.s.numIdenticalPairs([1])
        self.assertEqual(actual, 0)


if __name__ == '__main__':
    unittest.main()
