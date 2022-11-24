import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maxArea(height = [1,8,6,2,5,4,8,3,7])
        self.assertEqual(49, actual)

    def test_case_2(self):
        actual = self.s.maxArea(height = [1,1])
        self.assertEqual(1, actual)

    def test_case_3(self):
        actual = self.s.maxArea(height = [0, 1, 0, 0, 1, 0])
        self.assertEqual(3, actual)

    def test_case_4(self):
        actual = self.s.maxArea(height = [0, 1, 0, 0, 2, 0])
        self.assertEqual(3, actual)

    def test_case_5(self):
        actual = self.s.maxArea(height = [0, 0])
        self.assertEqual(0, actual)

if __name__ == '__main__':
    unittest.main()

