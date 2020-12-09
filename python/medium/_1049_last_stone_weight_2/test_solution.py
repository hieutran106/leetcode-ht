import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.lastStoneWeightII([2,7,4,1,8,1])
        self.assertEqual(1, actual)

    def test_case2(self):
        actual = self.s.lastStoneWeightII([5, 5])
        self.assertEqual(0, actual)

    def test_case3(self):
        actual = self.s.lastStoneWeightII([6, 1])
        self.assertEqual(5, actual)

    def test_case4(self):
        actual = self.s.lastStoneWeightII([2, 3, 10])
        self.assertEqual(5, actual)

    def test_case5(self):
        actual = self.s.lastStoneWeightII([2, 2, 10, 10])
        self.assertEqual(0, actual)

    def test_case7(self):
        actual = self.s.lastStoneWeightII([2, 3, 10, 10])
        self.assertEqual(1, actual)

    def test_case8(self):
        actual = self.s.lastStoneWeightII([2, 7, 4, 1])
        self.assertEqual(0, actual)

    def test_case9(self):
        actual = self.s.lastStoneWeightII([1,1,4,2,2])
        self.assertEqual(0, actual)


if __name__ == '__main__':
    unittest.main()

