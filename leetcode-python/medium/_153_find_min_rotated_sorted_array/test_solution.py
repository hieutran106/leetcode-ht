import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findMin([3, 4, 5, 1, 2])
        self.assertEqual(1, actual)

    def test_case_2(self):
        actual = self.s.findMin([4, 5, 6, 7, 0, 1, 2])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.findMin([11, 13, 15, 17])
        self.assertEqual(11, actual)

    def test_case_4(self):
        actual = self.s.findMin([3, 4, 5, 6, 7, 0, 1, 2])
        self.assertEqual(0, actual)

    def test_case_5(self):
        actual = self.s.findMin([3])
        self.assertEqual(3, actual)

    def test_case_6(self):
        actual = self.s.findMin([3,1,2])
        self.assertEqual(1, actual)

    def test_case_7(self):
        actual = self.s.findMin([2, 1])
        self.assertEqual(1, actual)

    def test_case_8(self):
        actual = self.s.findMin([1, 2])
        self.assertEqual(1, actual)


if __name__ == '__main__':
    unittest.main()
