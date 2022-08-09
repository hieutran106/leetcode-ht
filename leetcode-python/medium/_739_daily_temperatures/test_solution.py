import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
        self.assertEqual(actual, [1, 1, 4, 2, 1, 1, 0, 0])

    def test_case_2(self):
        actual = self.s.dailyTemperatures([30, 40, 50, 60])
        self.assertEqual(actual, [1, 1, 1, 0])

    def test_case_3(self):
        actual = self.s.dailyTemperatures([30, 60, 90])
        self.assertEqual(actual, [1, 1, 0])

    def test_case_4(self):
        actual = self.s.dailyTemperatures([1])
        self.assertEqual(actual, [0])

    def test_case_5(self):
        actual = self.s.dailyTemperatures([1, 1])
        self.assertEqual(actual, [0, 0])


if __name__ == '__main__':
    unittest.main()
