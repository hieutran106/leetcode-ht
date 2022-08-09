import unittest
from .solution import Solution, Solution2

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution2()

    def test_case1(self):
        actual = self.s.isMonotonic([1, 2, 2, 3])
        self.assertEqual(actual, True)

    def test_case2(self):
        actual = self.s.isMonotonic([6,5,4,4])
        self.assertEqual(actual, True)

    def test_case3(self):
        actual = self.s.isMonotonic([1,3,2])
        self.assertEqual(actual, False)

    def test_case4(self):
        actual = self.s.isMonotonic([1,2,4,5])
        self.assertEqual(actual, True)

    def test_case5(self):
        actual = self.s.isMonotonic([1,1,1])
        self.assertEqual(actual, True)

    def test_case6(self):
        actual = self.s.isMonotonic([11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5])
        self.assertEqual(actual, False)

    def test_case7(self):
        actual = self.s.isMonotonic([4, 4, 4, 4, 3, 2, 1, 1, 1, 1, 0 , -1 , 5])
        self.assertEqual(actual, False)

    def test_case8(self):
        actual = self.s.isMonotonic([4, 4, 4, 4, 3, 2, 1, 1, 1, 1, 0 , -1, -2])
        self.assertEqual(actual, True)

if __name__ == '__main__':
    unittest.main()

