import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.findKthLargest([3,2,1,5,6,4], 2)
        self.assertEqual(actual, 5)

    def test_case2(self):
        actual = self.s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
        self.assertEqual(actual, 4)

    def test_case3(self):
        actual = self.s.findKthLargest([5], 1)
        self.assertEqual(actual, 5)

    def test_case4(self):
        actual = self.s.findKthLargest([7,6,5,4,3,2,1], 2)
        self.assertEqual(actual, 6)

if __name__ == '__main__':
    unittest.main()

