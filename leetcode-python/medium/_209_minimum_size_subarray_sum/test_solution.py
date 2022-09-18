import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3])
        self.assertEqual(2, actual)

    def test_case_2(self):
        actual = self.s.minSubArrayLen(target=4, nums=[1, 4, 4])
        self.assertEqual(1, actual)

    def test_case_3(self):
        actual = self.s.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.minSubArrayLen(target=1, nums=[1])
        self.assertEqual(1, actual)

    def test_case_5(self):
        actual = self.s.minSubArrayLen(target=11, nums=[1, 2, 3, 4, 5])
        self.assertEqual(3, actual)

    def test_case_6(self):
        actual = self.s.minSubArrayLen(target=11, nums=[1, 2, 3, 4, 5, 11])
        self.assertEqual(1, actual)



if __name__ == '__main__':
    unittest.main()
