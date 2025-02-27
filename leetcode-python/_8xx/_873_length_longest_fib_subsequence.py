import unittest
from typing import List
import collections


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)

        def check_sequence(n1, n2):
            if n1 + n2 in nums:
                return 1 + check_sequence(n2, n1 + n2)
            else:
                return 0

        ans = 0
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                x1 = arr[i]
                x2 = arr[j]
                if x1 + x2 in nums:
                    count = 3 + check_sequence(x2, x1 + x2)
                    ans = max(ans, count)
        return ans




class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_0(self):
        actual = self.s.lenLongestFibSubseq(arr=[1, 2, 3])
        self.assertEqual(3, actual)

    def test_case_1(self):
        actual = self.s.lenLongestFibSubseq(arr=[1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(5, actual)

    def test_case_2(self):
        actual = self.s.lenLongestFibSubseq(arr=[1, 3, 7, 11, 12, 14, 18])
        self.assertEqual(3, actual)

    def test_case_3(self):
        actual = self.s.lenLongestFibSubseq(arr=[1, 5, 7, 9, 11])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.lenLongestFibSubseq(arr=[2, 4, 5, 6, 7, 8, 11])
        self.assertEqual(3, actual)
        # actual = self.s.lenLongestFibSubseq(arr=[2, 4, 5, 6, 7, 8, 11, 13, 14, 15, 21, 22, 34])
        # self.assertEqual(5, actual)

    def test_case_5(self):
        actual = self.s.lenLongestFibSubseq(arr=[2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50])
        self.assertEqual(5, actual)


if __name__ == '__main__':
    unittest.main()
