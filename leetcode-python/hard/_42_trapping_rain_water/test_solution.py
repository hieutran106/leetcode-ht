import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])
        self.assertEqual(6, actual)

    def test_case_2(self):
        actual = self.s.trap(height = [4,2,0,3,2,5])
        self.assertEqual(9, actual)

    def test_case_3(self):
        actual = self.s.trap(height = [1])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.trap(height = [0, 1, 2, 1, 0])
        self.assertEqual(0, actual)

    def test_case_5(self):
        actual = self.s.trap(height=[4, 2, 3])
        self.assertEqual(1, actual)

    def test_case_6(self):
        actual = self.s.trap(height=[4, 2, 3, 2, 4])
        self.assertEqual(5, actual)

    def test_case_7(self):
        actual = self.s.trap(height=[5, 2, 3, 2, 4])
        self.assertEqual(5, actual)

if __name__ == '__main__':
    unittest.main()

