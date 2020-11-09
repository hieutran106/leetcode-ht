from typing import List
import unittest

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        current = 1
        order = 1
        idx = 0
        while (True):
            if order > k:
                return current - 1

            if (idx < len(arr) and arr[idx] == current):
                idx = idx + 1
            else:
                order = order + 1

            current = current + 1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = Solution()
        actual = s.findKthPositive([2, 3, 4, 7, 11], 5)
        self.assertEqual(actual, 9)

    def test_case_2(self):
        s = Solution()
        actual = s.findKthPositive([1, 2, 3, 4], 2)
        self.assertEqual(actual, 6)

    def test_case_3(self):
        s = Solution()
        actual = s.findKthPositive([5], 1)
        self.assertEqual(actual, 1)

        actual = s.findKthPositive([5], 2)
        self.assertEqual(actual, 2)

        actual = s.findKthPositive([5], 5)
        self.assertEqual(actual, 6)

    def test_case_4(self):
        s = Solution()
        actual = s.findKthPositive([1], 1)
        self.assertEqual(actual, 2)


if __name__ == '__main__':
    unittest.main()