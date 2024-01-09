import unittest
from typing import List
import collections


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        res = 0
        for key, value in counter.items():
            if value == 1:
                return -1
            if value % 3 == 0:
                res += value // 3
            elif value % 3 == 2:
                # Chia 3 du 2 ==> co 1 so 2 o cuoi
                res += value // 3 + 1
            elif value %3 == 1:
                # Chia 3 du 1 ==> co 2 so hai o cuoi cung
                op = (value - 4) // 3
                res += op + 2
        return res


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minOperations(nums=[2, 3, 3, 2, 2, 4, 2, 3, 4])
        self.assertEqual(actual, 4)

    def test_case_2(self):
        actual = self.s.minOperations(nums=[2, 1, 2, 2, 3, 3])
        self.assertEqual(actual, -1)

    def test_case_3(self):
        actual = self.s.minOperations(nums=[1, 1])
        self.assertEqual(actual, 1)

    def test_case_4(self):
        actual = self.s.minOperations(nums=[1, 2, 1])
        self.assertEqual(actual, -1)

    def test_case_5(self):
        nums = [14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12]
        actual = self.s.minOperations(nums)
        self.assertEqual(actual, 7)

    def test_case_6(self):
        nums = [1, 1, 1, 1]
        actual = self.s.minOperations(nums)
        self.assertEqual(actual, 2)


if __name__ == '__main__':
    unittest.main()
