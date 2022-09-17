import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.subarraySum(nums=[1, 1, 1], k=2)
        self.assertEqual(actual, 2)

    def test_case_2(self):
        actual = self.s.subarraySum(nums=[1, 2, 3], k=3)
        self.assertEqual(actual, 2)

    def test_case_3(self):
        actual = self.s.subarraySum(nums=[0, 5, 3], k=8)
        self.assertEqual(actual, 2)

    def test_case_5(self):
        actual = self.s.subarraySum(nums=[5], k=9)
        self.assertEqual(actual, 0)

    def test_case_6(self):
        actual = self.s.subarraySum(nums=[1, 2, 3, 1, 2, 3], k=3)
        self.assertEqual(actual, 4)

    def test_case_7(self):
        actual = self.s.subarraySum(nums=[10, 2, 3, 0, 5], k=5)
        self.assertEqual(actual, 4)


if __name__ == '__main__':
    unittest.main()
