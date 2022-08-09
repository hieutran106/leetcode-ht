import unittest
from .solution import Solution
import os

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.smallestDistancePair([1, 3, 1], 1)
        self.assertEqual(actual, 0)

    def test_case2(self):
        actual = self.s.smallestDistancePair([1, 1, 1], 2)
        self.assertEqual(actual, 0)

    def test_case3(self):
        actual = self.s.smallestDistancePair([1, 6, 1], 3)
        self.assertEqual(actual, 5)

    def test_case4(self):
        actual = self.s.smallestDistancePair([9, 10, 7, 10, 6, 1, 5, 4, 9, 8], 18)
        self.assertEqual(actual, 2)

    def test_possible(self):
        def searchInsert(nums, start, target: int):
            left = start + 1
            right = len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left - start - 1

        actual = searchInsert([1, 1, 3, 4, 6], 1, 4)
        print(actual)
        self.assertEqual(True, True)

    def test_case5(self):
        actual = self.s.smallestDistancePair([1, 1], 1)
        self.assertEqual(actual, 0)

    def test_case6(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        input_file_path = os.path.join(dir_path, 'test_case5_input.txt')
        with open(input_file_path, 'r') as input_file:
            line = input_file.readline()
            input_numbers = list(map(int, line.split(',')))
            actual = self.s.smallestDistancePair(input_numbers, 25000000)
            self.assertEqual(actual, 1)


if __name__ == '__main__':
    unittest.main()

