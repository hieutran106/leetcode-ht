import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.canPartition([1,5,1,5])
        self.assertEqual(actual, True)

    def test_case2(self):
        actual = self.s.canPartition([1, 2, 3, 5])
        self.assertEqual(actual, False)

    def test_case3(self):
        actual = self.s.canPartition([1])
        self.assertEqual(actual, False)

    def test_case4(self):
        actual = self.s.canPartition([1, 4, 1])
        self.assertEqual(actual, False)

    def test_case5(self):
        actual = self.s.canPartition([1, 4, 9, 6])
        self.assertEqual(actual, True)

    def test_case6(self):
        actual = self.s.canPartition([1, 2, 3, 1000])
        self.assertEqual(actual, False)

    def test_case7(self):
        actual = self.s.canPartition([9, 5])
        self.assertEqual(actual, False)


if __name__ == "__main__":
    unittest.main()
