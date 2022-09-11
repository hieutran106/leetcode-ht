import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]])
        self.assertEqual(3, actual)

    def test_case_2(self):
        actual = self.s.minGroups([[1,3],[5,6],[8,10],[11,13]])
        self.assertEqual(1, actual)

    def test_case_3(self):
        actual = self.s.minGroups([[1, 1], [1, 2]])
        self.assertEqual(2, actual)

    def test_case_4(self):
        actual = self.s.minGroups([[1, 1]])
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

