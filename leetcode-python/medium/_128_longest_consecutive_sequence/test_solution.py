import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.longestConsecutive([100,4,200,1,3,2])
        self.assertEqual(4, actual)

    def test_case_2(self):
        actual = self.s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
        self.assertEqual(9, actual)

    def test_case_3(self):
        actual = self.s.longestConsecutive([])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.longestConsecutive([1, 5])
        self.assertEqual(1, actual)

    def test_case_5(self):
        actual = self.s.longestConsecutive([1, 5, 6, 10])
        self.assertEqual(2, actual)

    def test_case_6(self):
        actual = self.s.longestConsecutive([1, 6, 5, 10, 7, 15])
        self.assertEqual(3, actual)

    def test_case_7(self):
        actual = self.s.longestConsecutive([0, -1])
        self.assertEqual(2, actual)

    def test_case_8(self):
        actual = self.s.longestConsecutive([0, -1, 3, -2, 4, -3])
        self.assertEqual(4, actual)


    def test_case_9(self):
        actual = self.s.longestConsecutive([0, -1, 1, -2, 2, -3])
        self.assertEqual(6, actual)

if __name__ == '__main__':
    unittest.main()

