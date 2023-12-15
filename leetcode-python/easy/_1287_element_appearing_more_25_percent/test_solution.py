import unittest
from .solution import Solution
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = len(arr) // 4 + 1
        res = arr[0]
        count = 0

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
                if count >= threshold:
                    res = arr[i]
                    break
            else:
                count = 1

        return res


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10])
        self.assertEqual(actual, 6)

    def test_case_2(self):
        actual = self.s.findSpecialInteger(arr=[1, 1])
        self.assertEqual(actual, 1)

    def test_case_3(self):
        actual = self.s.findSpecialInteger(arr=[2])
        self.assertEqual(actual, 2)

    def test_case_4(self):
        actual = self.s.findSpecialInteger(arr=[1, 2, 3, 3])
        self.assertEqual(actual, 3)

    def test_case_5(self):
        actual = self.s.findSpecialInteger(arr=[1, 1, 2, 2, 3, 3, 3, 3])
        self.assertEqual(actual, 3)


if __name__ == '__main__':
    unittest.main()
