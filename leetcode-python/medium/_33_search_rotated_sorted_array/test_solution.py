import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
        self.assertEqual(4, actual)

    def test_case_2(self):
        actual = self.s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3)
        self.assertEqual(-1, actual)

    def test_case_3(self):
        actual = self.s.search(nums=[1], target=0)
        self.assertEqual(-1, actual)

    def test_case_4(self):
        actual = self.s.search(nums=[1], target=1)
        self.assertEqual(0, actual)

    def test_case_5(self):
        actual = self.s.search(nums=[5, 4], target=4)
        self.assertEqual(1, actual)

    def test_case_6(self):
        actual = self.s.search(nums=[1, 2, 3, 4, 5, 0], target=0)
        self.assertEqual(5, actual)

    def test_case_7(self):
        actual = self.s.search(nums=[5, 1, 3], target=1)
        self.assertEqual(1, actual)

    def test_case_8(self):
        actual = self.s.search(nums=[2, 1], target=1)
        self.assertEqual(1, actual)

    def test_case_9(self):
        actual = self.s.search(nums=[1, 2], target=1)
        self.assertEqual(0, actual)

    def test_case_10(self):
        actual = self.s.search(nums=[5, 1, 2, 3, 4], target=1)
        self.assertEqual(1, actual)

    def test_case_11(self):
        actual = self.s.search(nums=[8, 9, 2, 3, 4], target=9)
        self.assertEqual(1, actual)

    def test_case_12(self):
        actual = self.s.search(nums=[8, 9, 2], target=9)
        self.assertEqual(1, actual)

    def test_case_13(self):
        actual = self.s.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=8)
        self.assertEqual(4, actual)

    def test_case_14(self):
        actual = self.s.search(nums=[8, 9, 1, 4, 6], target=9)
        self.assertEqual(1, actual)


if __name__ == '__main__':
    unittest.main()
