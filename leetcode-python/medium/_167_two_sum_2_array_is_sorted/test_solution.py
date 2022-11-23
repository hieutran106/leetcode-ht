import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.twoSum(numbers = [2,7,11,15], target = 9)
        self.assertEqual([1, 2], actual)


    def test_case_2(self):
        actual = self.s.twoSum(numbers = [2,3,4], target = 6)
        self.assertEqual([1, 3], actual)


    def test_case_3(self):
        actual = self.s.twoSum(numbers = [-1,0], target = -1)
        self.assertEqual([1, 2], actual)

    def test_case_4(self):
        actual = self.s.twoSum(numbers = [1, 2, 3, 3, 6, 7], target = 6)
        self.assertEqual([3, 4], actual)

    def test_case_5(self):
        actual = self.s.twoSum(numbers = [-5, -3, -1, 0, 1, 5], target = -2)
        self.assertEqual([2, 5], actual)

if __name__ == '__main__':
    unittest.main()

