import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.threeSum(nums=[-1, 0, 1, 2, -1, -4])
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], actual)

    def test_case_2(self):
        actual = self.s.threeSum(nums=[0, 1, 1])
        self.assertEqual([], actual)

    def test_case_3(self):
        actual = self.s.threeSum(nums=[0, 0, 0])
        self.assertEqual([[0, 0, 0]], actual)

    def test_case_4(self):
        actual = self.s.threeSum(nums=[-1, -1, 2, 100])
        self.assertEqual([[-1, -1, 2]], actual)

    def test_case_4(self):
        actual = self.s.threeSum(nums=[0, 0, 0, 0])
        self.assertEqual([[0, 0, 0]], actual)

    def test_case_5(self):
        actual = self.s.threeSum(nums=[-2,0,0,2,2])
        self.assertEqual([[-2, 0, 2]], actual)


if __name__ == '__main__':
    unittest.main()
