import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4)
        self.assertEqual(False, actual)

    def test_case_2(self):
        actual = self.s.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5)
        self.assertEqual(True, actual)

    def test_case_3(self):
        actual = self.s.carPooling(trips=[[5, 0, 1]], capacity=5)
        self.assertEqual(True, actual)

    def test_case_6(self):
        actual = self.s.carPooling(trips=[[5, 0, 1]], capacity=4)
        self.assertEqual(False, actual)

    def test_case_7(self):
        actual = self.s.carPooling(trips=[[9, 3, 6], [8, 1, 7], [6, 6, 8], [8, 4, 9], [4, 2, 9]], capacity=28)
        self.assertEqual(False, actual)

    def test_case_8(self):
        actual = self.s.carPooling(trips=[[2, 1, 5], [3, 5, 7]], capacity=3)
        self.assertEqual(True, actual)


if __name__ == '__main__':
    unittest.main()
