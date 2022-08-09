import unittest
from .solution import Solution
import os


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_case3(self):
        actual = self.s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
        self.assertEqual(actual, 15)

    def test_case2(self):
        actual = self.s.shipWithinDays([3, 2, 2, 4, 1, 4], 3)
        self.assertEqual(actual, 6)

    def test_case1(self):
        actual = self.s.shipWithinDays([1, 2, 3, 1, 1], 4)
        self.assertEqual(actual, 3)

    def test_case4(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        input_file_path = os.path.join(dir_path, "input.txt")
        with open(input_file_path, "r") as input_file:
            line = input_file.readline()
            input_numbers = list(map(int, line.split(",")))
            actual = self.s.shipWithinDays(input_numbers, 1)
            self.assertEqual(actual, 250999 + 1)

    def test_case5(self):
        actual = self.s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertEqual(actual, 55)

    def test_case6(self):
        actual = self.s.shipWithinDays([1, 2], 1)
        self.assertEqual(actual, 3)

    def test_case7(self):
        actual = self.s.shipWithinDays([1, 2, 3], 1)
        self.assertEqual(actual, 6)

    def test_case8(self):
        actual = self.s.shipWithinDays([1, 2], 2)
        self.assertEqual(actual, 2)

    def test_case01(self):
        actual = self.s.can_shipped([3, 2, 2, 4, 1, 4], 3, 6)
        self.assertEqual(actual, True, "a")

        actual = self.s.can_shipped([3, 2, 4, 4, 1, 4], 3, 8)
        self.assertEqual(actual, True, "b")

        actual = self.s.can_shipped([3, 2, 4, 4, 1, 4], 3, 6)
        self.assertEqual(actual, False, "c")

        actual = self.s.can_shipped([3, 2, 4, 4, 1, 4], 3, 7)
        self.assertEqual(actual, False, "d")

        actual = self.s.can_shipped([1, 2, 3, 1, 1], 4, 3)
        self.assertEqual(actual, True, "e")

        actual = self.s.can_shipped([1, 2, 3, 1, 1], 4, 2)
        self.assertEqual(actual, False, "f")

        actual = self.s.can_shipped([1, 2], 2, 2)
        self.assertEqual(actual, True, "g")

        actual = self.s.can_shipped([1, 2], 2, 1)
        self.assertEqual(actual, False, "g")


if __name__ == "__main__":
    unittest.main()
