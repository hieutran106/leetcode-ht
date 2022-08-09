import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        nums = [1,3,5,4,7]
        answer = self.s.findLengthOfLCIS(nums)
        self.assertEqual(answer, 3)

    def test_case2(self):
        nums = [2,2,2,2,2]
        answer = self.s.findLengthOfLCIS(nums)
        self.assertEqual(answer, 1)

    def test_case3(self):
        nums = [2]
        answer = self.s.findLengthOfLCIS(nums)
        self.assertEqual(answer, 1)

    def test_case4(self):
        nums = [1,3,5,4,7,8,9,10]
        answer = self.s.findLengthOfLCIS(nums)
        self.assertEqual(answer, 5)

    def test_case5(self):
        nums = nums = [1,3,5,4,7,8,9,10,9,10,1,2,3,4,5,6,7]
        answer = self.s.findLengthOfLCIS(nums)
        self.assertEqual(answer, 7)

if __name__ == '__main__':
    unittest.main()

