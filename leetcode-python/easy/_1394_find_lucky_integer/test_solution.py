import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        actual = s.findLucky([2, 2, 3, 4])
        self.assertEqual(actual, 2)

    def test_case_2(self):
        s = Solution()
        actual = s.findLucky([1,2,2,3,3,3])
        self.assertEqual(actual, 3)

    def test_case_3(self):
        s = Solution()
        actual = s.findLucky([2, 2, 2, 3, 3])
        self.assertEqual(actual, -1)

    def test_case_4(self):
        s = Solution()
        actual = s.findLucky([5])
        self.assertEqual(actual, -1)

    def test_case_5(self):
        s = Solution()
        actual = s.findLucky([7,7,7,7,7,7,7])
        self.assertEqual(actual, 7)

    def test_case_6(self):
        s = Solution()
        actual = s.findLucky([1, 2, 3, 2])
        self.assertEqual(actual, 2)

    def test_case_7(self):
        s = Solution()
        actual = s.findLucky([3, 3, 4, 7, 6, 3])
        self.assertEqual(actual, 3)

if __name__ == '__main__':
    unittest.main()
