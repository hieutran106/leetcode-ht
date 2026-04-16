import unittest
from typing import List
import collections


# Date: 2026-04-16
# Problem: 3488 closest_equal_element_queries
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        Make one pass over the array twice, so circular neighbors can be seen naturally.
        Track the last index where each value appeared.
        """
        n, lastSeen = len(nums), {}
        l, r = [n] * n, [n] * n
        for j in range(2 * n):
            idx = j % n
            value = nums[idx]

            if value in lastSeen:
                prev = lastSeen[value]
                prevIdx = prev % n
                dist = j - prev
                r[prevIdx] = min(r[prevIdx], dist)
                l[idx]= min(l[idx], dist)

            lastSeen[value] = j

        ans = []
        for q in queries:
            distance = min(l[q], r[q])
            ans.append(distance if distance < n else -1)

        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.solveQueries(nums=[1, 3, 1, 4, 1, 3, 2], queries=[0, 3, 5])
        self.assertEqual([2, -1, 3], actual)

    def test_case_2(self):
        actual = self.s.solveQueries(nums=[1, 2, 3, 4], queries=[0, 1, 2, 3])
        self.assertEqual([-1, -1, -1, -1], actual)

    def test_case_3(self):
        actual = self.s.solveQueries(nums=[14, 14, 4, 2, 19, 19, 14, 19, 14], queries=[2, 4, 8, 6, 3])
        self.assertEqual([-1, 1, 1, 2, -1], actual)

    def test_case_4(self):
        actual = self.s.solveQueries(nums=[6, 12, 17, 9, 16, 7, 6], queries=[5, 6, 0, 4])
        self.assertEqual([-1, 1, 1, -1], actual)


if __name__ == '__main__':
    unittest.main()
