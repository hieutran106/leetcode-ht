import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
        self.assertEqual(actual, [3,3,5,5,6,7])

    def test_case_2(self):
        actual = self.s.maxSlidingWindow(nums = [1], k = 1)
        self.assertEqual(actual, [1])

    def test_case_3(self):
        actual = self.s.maxSlidingWindow(nums = [1, 2, 3, 4], k = 4)
        self.assertEqual(actual, [4])

    def test_case_4(self):
        actual = self.s.maxSlidingWindow(nums=[6, 5, 4, 3, 2, 1], k = 3)
        self.assertEqual(actual, [6, 5, 4, 3])

    def test_case_5(self):
        actual = self.s.maxSlidingWindow(nums = [3, 3, 3, 2, 2, 2], k = 2)
        self.assertEqual(actual, [3, 3, 3, 2, 2])

    def test_case_6(self):
        actual = self.s.maxSlidingWindow(nums=[3, 5, 4, 2, 1, 5, 3], k = 3)
        self.assertEqual(actual, [5, 5, 4, 5, 5])

    def test_case_7(self):
        actual = self.s.maxSlidingWindow(nums=[1,3,1,2,0,5], k=3)
        self.assertEqual(actual, [3,3,2,5]
)

if __name__ == '__main__':
    unittest.main()

