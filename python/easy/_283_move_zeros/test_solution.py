import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.moveZeroes([0,1,0,3,12])
        self.assertEqual(actual, [1,3,12,0,0])

    def test_case2(self):
        actual = self.s.moveZeroes([1, 0])
        self.assertEqual(actual, [1, 0])

    def test_case3(self):
        actual = self.s.moveZeroes([0,1,0,0,3,12])
        self.assertEqual(actual, [1,3,12,0,0,0])

    def test_case4(self):
        actual = self.s.moveZeroes([0,1,0,0,3,12, 0, 7])
        self.assertEqual(actual, [1,3,12,7, 0, 0,0,0])

    def test_case5(self):
        actual = self.s.moveZeroes([])
        self.assertEqual(actual, [])

    def test_case6(self):
        actual = self.s.moveZeroes([1])
        self.assertEqual(actual, [1])

    def test_case7(self):
        actual = self.s.moveZeroes([0])
        self.assertEqual(actual, [0])

    def test_case8(self):
        actual = self.s.moveZeroes([0, 0, 0, 1, 2, 3])
        self.assertEqual(actual, [1, 2, 3, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()

