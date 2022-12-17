import unittest
from .solution import Solution, Solution2

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution2()

    def test_case_1(self):
        actual = self.s.longestMountain(arr = [2,1,4,7,3,2,5])
        self.assertEqual(5, actual)

    def test_case_2(self):
        actual = self.s.longestMountain(arr = [2, 2, 2])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.longestMountain(arr = [2])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.longestMountain(arr = [1, 2, 3, 4, 3, 1, 2, 3, 4, 5, 6, 7, 8, 7,6,6])
        self.assertEqual(10, actual)

if __name__ == '__main__':
    unittest.main()

