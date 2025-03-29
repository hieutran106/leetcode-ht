import unittest
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        dpOdd = [0] * n  # the number of subarray ending at current index with odd sum
        dpEven = [0] * n # the number of subarray ending at current index with even sum
        if arr[0] % 2 == 0:
            dpEven[0] = 1
        else:
            dpOdd[0] = 1
        for i in range(1, n):
            if arr[i] % 2 == 1: # odd
                dpOdd[i] = dpEven[i-1] + 1
                dpEven[i] = dpOdd[i-1]
            else: # even
                dpOdd[i] = dpOdd[i-1]
                dpEven[i] = dpEven[i-1] + 1

        return sum(dpOdd) % (10**9 + 7)


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.numOfSubarrays(arr=[1, 3, 5])
        self.assertEqual(4, actual)

    def test_case_2(self):
        actual = self.s.numOfSubarrays(arr=[2, 4, 6])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.numOfSubarrays(arr=[1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(16, actual)


if __name__ == '__main__':
    unittest.main()
