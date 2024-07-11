import math
import unittest
from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low = 1
        high = position[-1] - position[0]

        def canPlaceBalls(g: int) -> bool:
            # can we place m balls with at least g gap between them
            count = 0
            last_placed = -1
            for i, p in enumerate(position):
                if last_placed == -1 or p - position[last_placed] >= g:
                    count += 1
                    last_placed = i
                if count == m:
                    return True
            # cannot place m balls in n position
            return False

        while low < high:
            mid = low + math.ceil((high - low) /2)
            if canPlaceBalls(mid):
                low = mid
            else:
                high = mid - 1
        return low




class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maxDistance(position=[1, 2, 3, 4, 7], m=3)
        self.assertEqual(actual, 3)

    def test_case_2(self):
        actual = self.s.maxDistance([5, 4, 3, 2, 1, 1000000000], m=2)
        self.assertEqual(actual, 999999999)

    def test_case_3(self):
        actual = self.s.maxDistance([5, 4, 3, 2, 1, 1000000000], m=3)
        self.assertEqual(actual, 4)

    def test_case_4(self):
        actual = self.s.maxDistance([2, 10], m = 2)
        self.assertEqual(actual, 8)


if __name__ == '__main__':
    unittest.main()
